import json
from flask import Flask
from about_me import me
from mock_data import catalog

app = Flask('class2python')

@app.route("/", methods=['GET']) #root
def home():
    return "This is the home page"

#Create an about endpoint and show your name

@app.route("/about") 
def about():
    return me["first"] + " " + me["last"]

@app.route("/myaddress")
def address():
    return f'{me["address"]["street"]} {me["address"]["number"]}'


 ########################################################### API ENDPOINTS################################################################################################################################

 # Postman -> Test endpoints of REST APIs

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog/count", methods=["GET"])
def get_count():

    #Here... count how many products are in the list catalog
    counts = len(catalog)
    return json.dumps(counts) #return the value

#Request 127.0.0.1:5000/api/product/
@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    return json.dumps(id)


app.run(debug=True)
