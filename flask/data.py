from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'libraries'

# Initialize MySQL
mysql = MySQL(app)

# Routes for CRUD operations

# Create a new city
@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO cities (name,population) VALUES (%s, %s)', (data['name'],data['population'],))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "City created successfully", "id": cur.lastrowid}), 201

# Get all cities
@app.route('/cities', methods=['GET'])
def get_cities():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cities')
    cities = cur.fetchall()
    cur.close()
    print(cities)
    return jsonify(cities)


# Get a specific city by ID
@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cities WHERE id = %s', (city_id,))
    city = cur.fetchone()
    cur.close()
    if city:
        return jsonify({"id": city[0], "name": city[1]})
    return jsonify({"error": "City not found"}), 404

# Update a city by ID
@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
        cur = mysql.connection.cursor()
        data = request.get_json()
        new_name = data.get('name')
        new_population = data.get('population')

        if new_name is not None or new_population is not None:
            query = 'UPDATE cities SET '
            values = []
            if new_name is not None:
                query += 'name = %s, '
                values.append(new_name)

            if new_population is not None:
                query += 'population = %s, '
                values.append(new_population)

            query = query.rstrip(', ') + ' WHERE id = %s'
            values.append(city_id)

            cur.execute(query, tuple(values))
            mysql.connection.commit()
            cur.close()

            return jsonify({"message": "City updated successfully"})

        return jsonify({"error": "No valid data provided for update"}), 400

# Delete a city by ID
@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM cities WHERE id = %s', (city_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "City deleted successfully"})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
    
