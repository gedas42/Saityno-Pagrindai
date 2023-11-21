# from flask import Flask, jsonify, request
# from flask_restful import Resource, Api
# from flask_mysqldb import MySQL 
# from flask_cors import CORS
# import json

# app = Flask(__name__)
# CORS(app)


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MySQL_PORT'] = '81'
# app.config['MYSQL_DB'] = 'users' 

# mysql = MySQL(app)

# api = Api(app)



# def dictfetchall(cursor):
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]



# if __name__ == '__main__':
#     app.run(debug=True)
