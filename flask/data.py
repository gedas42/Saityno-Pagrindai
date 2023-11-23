from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/Libraries'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# CORS(app, origins='*', resources={r"/*": {"origins": "http://localhost:5173"}})
# Routes for CRUD operations
class city(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    population = db.Column(db.Integer)


# Create a new city


# Get all cities

@app.route('/cities', methods=['GET'])
def get_cities():
    cities = city.query.all()
    city_list = [{"id": city.id, "name": city.name, "population": city.population} for city in cities]
    return jsonify(city_list)

@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    new_city = city(name=data['name'], population=data.get('population'))
    db.session.add(new_city)
    db.session.commit()
    return jsonify({"message": "City created successfully", "id": new_city.id}), 201

@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    singleCity = city.query.get(city_id)
    if singleCity:
        return jsonify({"id": singleCity.id, "name": singleCity.name, "population": singleCity.population}),200
    return jsonify({"error": "City not found"}), 404

@app.route('/cities/<int:city_id>', methods=['PUT'])
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

@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    singleCity = city.query.get(city_id)

    if singleCity:
        db.session.delete(singleCity)
        db.session.commit()
        return jsonify({"message": "City deleted successfully"})
    return jsonify({"error": "City not found"}), 404
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
    
