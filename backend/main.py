# before starting to write any code figure out what are teh diffrent routes or endpoints thta you will be needing for your API 
# Here we are making a CRUD application, and also after figuring out those also breifly mention what the function will be doing 
# how the network server works

#localhosthost:500/create_contact

#Request
#type: DELETE, PUT, PATCH, POST,GET etc..
#json{}

# Response
#status: 404,500,200 etc
#json:{}

from flask import request,jsonify,Flask
from config import app,db
from models import Contact



@app.route("/")
def home():
    return "this is working maybe"

@app.route("/contacts", methods=["GET"]) #decorator
def get_contacts():
    contacts = Contact.query.all()    # this will use the flask ORM and then gets all teh info from the database
    json_contacts = list(map(lambda x: x.to_json(),contacts)) #copntacts is a list of contact objects we know that all the objects have the to_json function 
    #  so here we are going to call the method so that it creates a new list with all the jsons
    # what map does is it will take all teh elements from the contacts list and then applies the function to the them and givesus a new list
    # the function we are using here is called a lambda function which is a shortcut to writing functions lambda is the name x is a variable and we call the the nmethod for teh variable x
    return jsonify({"contacts":json_contacts})
# create

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName") # this line will look for the keyword firstName in the json request 
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message":"you must include a first name, last name and email"}),
            400,
        )
    
    new_contact = Contact(first_name = first_name, last_name = last_name, email= email) # creating a python class corresponding to that entry 
    try:
        db.session.add(new_contact)  # add it to the database session it will be in the staging area like ready to be written to the database
        db.session.commit()     #  anything in the session will be written to the database 
    except Exception as e:
        return jsonify({"message":str(e)}),400
    
    return jsonify({"message":"User created!"}),201


@app.route("/update_contact/<int:user_id>", methods = ["PATCH"]) # we are taking a path parameter to specify which contact to be updated and using the PATCH method as the HTTP method
def update_contact(user_id):   # taking the parameter user id from the request
    contact = Contact.query.get(user_id) # we are searching for the contact withe user id in the database

    if not contact:
        return jsonify({"message":"User does not exist"}),404
    
    data = request.json
    contact.first_name = data.get("firstName",contact.first_name) # modify the contact's firstname to whatever the json data firstname is that is given to us
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    # so how the get function works is it first checks the key name in the json and if it exists it will return that function if not it will just return the second function
    
    db.session.commit()

    return jsonify({"message":"User updated"}),200


@app.route("/delete_contact/<int:user_id>",methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message":"User not found"}),404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message":"User deleted"}), 200



if __name__ == '__main__': # this line helps us to avoid runnning the entire file if we are just importing stuff from this file
    with app.app_context():
        db.create_all() # if the database does not exist this code will create the db for the app accordig the fields that we have already defined


    app.run(debug = True)