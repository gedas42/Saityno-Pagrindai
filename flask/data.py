from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity, unset_jwt_cookies
from datetime import timedelta
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/Libraries'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
db = SQLAlchemy(app)

# CORS(app, origins='*', resources={r"/*": {"origins": "http://localhost:5173"}})

# DB objects
class city(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    population = db.Column(db.Integer)
    libraries = db.relationship('library', backref='city', lazy=True)

class library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)

class book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    library_id = db.Column(db.Integer, db.ForeignKey('library.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255))
    print_year = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    taken_by = db.Column(db.String(255))

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role = db.Column(db.String(255))

#Login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    singleUser = user.query.filter_by(name=data['name'], password=data['password']).first()

    if data['name'] == singleUser.name and data['password'] == singleUser.password:
        access_token = create_access_token(identity=singleUser.role, fresh=True)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    # Clear the JWT token from the client-side
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp

# Get all cities


@app.route('/api/cities', methods=['GET'])
def get_cities():
    cities = city.query.all()
    city_list = [{"id": city.id, "name": city.name, "population": city.population} for city in cities]
    return jsonify(city_list)

@app.route('/test', methods=['GET'])
def get_hello():
    return  "<p>Hello, World!</p>"

@app.route('/api/cities', methods=['POST'])
@jwt_required()
def create_city():
    data = request.get_json()
    new_city = city(name=data['name'], population=data.get('population'))
    db.session.add(new_city)
    db.session.commit()
    return jsonify({"message": "City created successfully", "id": new_city.id}), 201

@app.route('/api/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    singleCity = city.query.get(city_id)
    if singleCity:
        return jsonify({"id": singleCity.id, "name": singleCity.name, "population": singleCity.population}),200
    return jsonify({"error": "City not found"}), 404

@app.route('/api/cities/<int:city_id>', methods=['PUT'])
@jwt_required()
def update_city(city_id):
    data = request.get_json()
    singleCity = city.query.get(city_id)
    if singleCity:
        if 'name' in data:
            singleCity.name = data['name']
        if 'population' in data:
            singleCity.population = data['population']

        db.session.commit()
        return jsonify({"message": "City updated successfully"})
    return jsonify({"error": "City not found"}), 404

@app.route('/api/cities/<int:city_id>', methods=['DELETE'])
@jwt_required()
def delete_city(city_id):
    singleCity = city.query.get(city_id)

    if singleCity:
        db.session.delete(singleCity)
        db.session.commit()
        return jsonify({"message": "City deleted successfully"})
    return jsonify({"error": "City not found"}), 404

# library reqeusts
# Libraries
@app.route('/api/cities/<int:city_id>/libraries', methods=['POST'])
@jwt_required()
def create_library(city_id):
    data = request.get_json()
    new_library = library(name=data['name'], address=data.get('address'), city_id=city_id)
    db.session.add(new_library)
    db.session.commit()
    return jsonify({"message": "Library created successfully", "id": new_library.id}), 201

@app.route('/api/cities/<int:city_id>/libraries', methods=['GET'])
def get_libraries(city_id):
    libraries = library.query.filter_by(city_id=city_id).all()
    library_list = [{"id": library.id, "name": library.name, "address": library.address, "city_id": library.city_id} for library in libraries]
    return jsonify(library_list)

@app.route('/api/cities/<int:city_id>/libraries/<int:library_id>', methods=['GET'])
def get_library(city_id, library_id):
    singleLibrary = library.query.filter_by(city_id=city_id, id=library_id).first()
    if singleLibrary:
        return jsonify({"id": singleLibrary.id, "name": singleLibrary.name, "address": singleLibrary.address, "city_id": singleLibrary.city_id})
    return jsonify({"error": "Library not found"}), 404

@app.route('/api/cities/<int:city_id>/libraries/<int:library_id>', methods=['PUT'])
@jwt_required()
def update_library(city_id, library_id):
    data = request.get_json()
    singleLibrary = library.query.filter_by(city_id=city_id, id=library_id).first()

    if singleLibrary:
        if 'name' in data:
            singleLibrary.name = data['name']
        if 'address' in data:
            singleLibrary.address = data['address']

        db.session.commit()
        return jsonify({"message": "Library updated successfully"})
    return jsonify({"error": "Library not found"}), 404

@app.route('/api/cities/<int:city_id>/libraries/<int:library_id>', methods=['DELETE'])
@jwt_required()
def delete_library(city_id, library_id):
    singleLibrary = library.query.filter_by(city_id=city_id, id=library_id).first()

    if singleLibrary:
        db.session.delete(singleLibrary)
        db.session.commit()
        return jsonify({"message": "Library deleted successfully"})
    return jsonify({"error": "Library not found"}), 404

#Book routes

@app.route('/api/cities/<int:city_id>/libraries/<int:library_id>/books', methods=['POST'])
@jwt_required()
def create_book(city_id, library_id):
    data = request.get_json()
    new_book = book(
        library_id=library_id,
        name=data['name'],
        author=data.get('author'),
        print_year=data.get('print_year'),
        pages=data.get('pages'),
        taken_by=data.get('taken_by')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book created successfully", "id": new_book.id}), 201

@app.route('/api/cities/<int:city_id>/libraries/<int:library_id>/books', methods=['GET'])
def get_books(city_id, library_id):
    books = book.query.filter_by(library_id=library_id).all()
    book_list = [
        {"id": book.id, "library_id": book.library_id, "name": book.name,
         "author": book.author, "print_year": book.print_year, "pages": book.pages,
         "taken_by": book.taken_by} for book in books
    ]
    return jsonify(book_list)


@app.route('/api/cities/<int:city_id>/libraries/<int:library_id>/books/<int:book_id>', methods=['GET'])
def get_book(city_id, library_id, book_id):
    SingleBook = book.query.filter_by(library_id=library_id, id=book_id).first()
    if SingleBook:
        return jsonify({
            "id": SingleBook.id, "library_id": SingleBook.library_id, "name": SingleBook.name,
            "author": SingleBook.author, "print_year": SingleBook.print_year, "pages": SingleBook.pages,
            "taken_by": SingleBook.taken_by
        })
    return jsonify({"error": "Book not found"}), 404

@app.route('/api/cities/<int:city_id>/libraries/<int:library_id>/books/<int:book_id>', methods=['PUT'])
@jwt_required()
def update_book(city_id, library_id, book_id):
    data = request.get_json()
    SingleBook = book.query.filter_by(library_id=library_id, id=book_id).first()

    if SingleBook:
        if 'name' in data:
            SingleBook.name = data['name']
        if 'author' in data:
            SingleBook.author = data['author']
        if 'print_year' in data:
            SingleBook.print_year = data['print_year']
        if 'pages' in data:
            SingleBook.pages = data['pages']
        if 'taken_by' in data:
            SingleBook.taken_by = data['taken_by']

        db.session.commit()
        return jsonify({"message": "Book updated successfully"})
    return jsonify({"error": "Book not found"}), 404


@app.route('/api/cities/<int:city_id>/libraries/<int:library_id>/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(city_id, library_id, book_id):
    SingleBook = book.query.filter_by(library_id=library_id, id=book_id).first()

    if SingleBook:
        db.session.delete(SingleBook)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully"})
    return jsonify({"error": "Book not found"}), 404



# @app.route('/cities', methods=['POST'])
# def create_city():
#     data = request.get_json()
#     cur = mysql.connection.cursor()
#     cur.execute('INSERT INTO cities (name,population) VALUES (%s, %s)', (data['name'],data['population'],))
#     mysql.connection.commit()
#     cur.close()
#     return jsonify({"message": "City created successfully", "id": cur.lastrowid}), 201
# # Get a specific city by ID

# @app.route('/cities/<int:city_id>', methods=['GET'])
# def get_city(city_id):
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM cities WHERE id = %s', (city_id,))
#     city = cur.fetchone()
#     cur.close()
#     if city:
#         return jsonify({"id": city[0], "name": city[1]})
#     return jsonify({"error": "City not found"}), 404

# # Update a city by ID
# @app.route('/cities/<int:city_id>', methods=['PUT'])
# def update_city(city_id):
#         cur = mysql.connection.cursor()
#         data = request.get_json()
#         new_name = data.get('name')
#         new_population = data.get('population')

#         if new_name is not None or new_population is not None:
#             query = 'UPDATE cities SET '
#             values = []
#             if new_name is not None:
#                 query += 'name = %s, '
#                 values.append(new_name)

#             if new_population is not None:
#                 query += 'population = %s, '
#                 values.append(new_population)

#             query = query.rstrip(', ') + ' WHERE id = %s'
#             values.append(city_id)

#             cur.execute(query, tuple(values))
#             mysql.connection.commit()
#             cur.close()

#             return jsonify({"message": "City updated successfully"})

#         return jsonify({"error": "No valid data provided for update"}), 400

# # Delete a city by ID
# @app.route('/cities/<int:city_id>', methods=['DELETE'])
# def delete_city(city_id):
#     cur = mysql.connection.cursor()
#     cur.execute('DELETE FROM cities WHERE id = %s', (city_id,))
#     mysql.connection.commit()
#     cur.close()
#     return jsonify({"message": "City deleted successfully"})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
    
