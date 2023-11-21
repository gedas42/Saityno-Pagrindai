from flask import Flask, jsonify, request,make_response, render_template
from flask_restful import Resource, Api
from flask_mysqldb import MySQL 
from flask_cors import CORS
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity, unset_jwt_cookies
import json
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta
from fpdf import FPDF
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf import PageLayout
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
import datetime
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
import io
import random
app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "untold-truth"  # Change this "super secret" with something else!
jwt = JWTManager(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MySQL_PORT'] = '81'
app.config['MYSQL_DB'] = 'accounting'
bcrypt = Bcrypt(app)
mysql = MySQL(app)
CORS(app,origins='*', resources={r"/*": {"origins": "http://localhost:5174"}})
api = Api(app)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# @app.route("/token", methods=["POST"])
# def create_token():
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)
#     # Query your database for username and password
#     user = User.query.filter_by(username=username, password=password).first()
#     if user is None:
#         # the user was not found on the database
#         return jsonify({"msg": "Bad username or password"}), 401
    
#     # create a new token with the user id inside
#     access_token = create_access_token(identity=user.id)
#     return jsonify({ "token": access_token, "user_id": user.id })

# @app.route('/generate-pdf', methods=['GET'])
# def generate_pdf():
#     # Retrieve the necessary data to include in the PDF
#     data = {
#         'name': 'John Doe',
#         'age': 30,
#         'email': 'john@example.com'
#     }

#     # Render a Jinja template with the data
#     rendered_template = render_template('/template.html', data=data)

#     # Generate the PDF from the rendered template
#     pdf = from_string(rendered_template, False)

#     # Create a response with the PDF file
#     response = make_response(pdf)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename=generated.pdf'

#     return response

@app.route('/api/pdf')
def generate_pdf():
    # Create a new PDF document
    document = Document()

    # Create a new page
    page = Page()

    # Add content to the page
 
    
    # layout: PageLayout = SingleColumnLayout(page)

    # # add a Paragraph
    # layout.add(Paragraph("Hello World!"))
 
    page_layout = SingleColumnLayout(page)
  
    table_001= Table(number_of_rows=5, number_of_columns=3)
	
    table_001.add(Paragraph("[Street Address]"))    
    table_001.add(Paragraph("Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))    
    now = datetime.datetime.now()    
    table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year)))
	
    table_001.add(Paragraph("[City, State, ZIP Code]"))    
    table_001.add(Paragraph("Invoice #", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
    table_001.add(Paragraph("%d" % random.randint(1000, 10000)))   
	
    table_001.add(Paragraph("[Phone]"))    
    table_001.add(Paragraph("Due Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
    table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year))) 
	
    table_001.add(Paragraph("[Email Address]"))    
    table_001.add(Paragraph(" "))
    table_001.add(Paragraph(" "))

    table_001.add(Paragraph("[Company name]"))
    table_001.add(Paragraph(" "))
    table_001.add(Paragraph(" "))

    table_001.set_padding_on_all_cells(int(2),int(2),int(2),int(2))    		
    table_001.no_borders()
    page_layout.add(table_001)
    # Add the page to the document
    document.add_page(page)

    # Generate the PDF content
 
    buffer = io.BytesIO()
    PDF.dumps(buffer, document)
    buffer.seek(0)
    # Create a response with PDF content
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

    return response

# @app.route('/api/pdf', methods=['GET'])
# def generate_pdf():
#     # Create an instance of the FPDF class
#     pdf = FPDF(orientation='P', unit='pt', format='A4')

#     # Add a page to the PDF
#     pdf.add_page()

#     # Set font and size
#     pdf.set_top_margin(10)
#     pdf.set_left_margin(10)
#     pdf.set_right_margin(10)

#     pdf.set_font("Times", "B", 24)
#     pdf.cell(0, 80, "Purchase Receipt", 0, 1, "C")

#     # Write content to the PDF
#     pdf.cell(0, 0, txt="Hello, World!")
#     # Output the PDF as a byte array
#     pdf_bytes = pdf.output(dest='S')
    
#     # Create a response with PDF content
#     response = make_response(pdf_bytes)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

#     return response

# @app.route('/register', methods=['POST'])
# def register():
#     username = request.json['username']
#     password = request.json['password']

#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

#     cursor = mysql.connection.cursor()
#     sql= "INSERT INTO users ('email, `password`) VALUES (%(username)s, %(password)s)"
#     data = {
#         'username': username,
#         'password': hashed_password
#     }
#     cursor.execute(sql,data)
   
#     mysql.connection.commit()
#     cursor.close()

#     return jsonify({'message': 'User registered successfully'}), 201


@app.route('/api/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (username,))
    user = cursor.fetchone()

    if user and password==user[4]:
        access_token = create_access_token(identity=user[0])
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    # Clear the JWT token from the client-side
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp


@app.route('/profile', methods=['PUT'])
@jwt_required()
def profile():
        cur = mysql.connection.cursor()
        data = request.get_json()
        user_id = get_jwt_identity()
        name = data['name']
        surname = data['surname']
        email = data['email']
        code = data['code']
        adress = data['adress']
        nr = data['nr']
        account = data['account']
        
        cur.execute("""UPDATE users SET name=%s, surname=%s, email=%s, code=%s, adress=%s, nr=%s, account=%s WHERE id=%s """,
         (name,surname,email,code,adress,nr,account,user_id,))

        return jsonify({'Method':'PUT', 'message':'users updated successfully'})

@app.route('/profile/get', methods=['GET'])
@jwt_required()
def get():
        cur = mysql.connection.cursor()
        user_id = get_jwt_identity()
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        data = cur.fetchall()
        cur.close()
        print(type(data))
        result = []
        for row in data:
            result.append({
                'name' : row[1],
                'surname' : row[2],
                'email' : row[3],
                'code' : row[5],
                'adress' : row[6],
                'nr' : row[7],
                'account' : row[8],
                # Add more fields as needed
            })
        return jsonify({'user':result,'Method':'GET'})


class Income(Resource):
    @jwt_required()
    def get(self):
        cur = mysql.connection.cursor()
        user_id = get_jwt_identity()
        cur.execute("SELECT * FROM income WHERE owner = %s", (user_id,))
        data = cur.fetchall()
        cur.close()
        print(type(data))
        result = []
        for row in data:
            result.append({
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'adress': row[3],
                'code': row[4],
                'amount': row[5],
                'pvm': row[6],
                'purpose': row[7],
                'owner': row[8],
                'date': row[9],
            })
        return jsonify({'incomes':result,'Method':'GET'})

    @jwt_required()
    def post(self):
        data = request.get_json()
        print(data)
        id = data['id']
        type = data['type']
        purpose = data['purpose']
        owner = get_jwt_identity()

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO income (id,type,purpose,owner) VALUES(%s, %s, %s, %s)", (id,type,purpose,owner))

        return jsonify({'Method':'POST', 'message':'New income created successfully'})

    @jwt_required()
    def put(self):
        data = request.get_json()
        user_id = get_jwt_identity()
        print(data)
        type = data['type']
        purpose = data['purpose']
        
        code = data['code']
        amount = data['amount']
        id = data['id']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE income SET type=%s, purpose=%s, adress=%s, code=%s,amount=%s
        WHERE id=%s 
        """, (type,purpose,code,amount,id))

        return jsonify({'Method':'PUT', 'message':'income updated successfully'})
    
    @jwt_required()
    def patch(self):
        data = request.get_json()
        print(data)
        id = data['id']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM income WHERE id=%s", (id,))
        mysql.connection.commit()


        return jsonify({'Method':'PATCH', 'message':'income daleted successfully'})     
    
         
class User(Resource):
    @jwt_required()
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        data = dictfetchall(cur)
        cur.close()
        print(type(data))

        return jsonify({'users':data,'Method':'GET'})

    def post(self):
        data = request.get_json()
        print(data)
        email = data['email']
        password = data['password']
        surname = data['surname']
        nr = data['nr']
        account = data['account']
        code = data['code']
        adress = data['adress']
        name = data['name']
 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (email,password,name,surname,nr,account,code,adress) VALUES(%s, %s,%s, %s,%s, %s,%s, %s)",
            (email,password,name,surname,nr,account,code,adress))
        return jsonify({'Method':'POST', 'message':'New user created successfully'})

    @jwt_required()
    def put(self):
        data = request.get_json()
        user_id = get_jwt_identity()
        password = data['newpassword']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE users SET password=%s WHERE id=%s """, (password,user_id,))

        return jsonify({'Method':'PUT', 'message':'users updated successfully'})
        


api.add_resource(User, '/api/users/')
api.add_resource(Income, '/api/incomes/')




if __name__ == '__main__':
    app.run(debug=True)
