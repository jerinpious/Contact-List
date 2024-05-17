# when creating your models know what data that you will need which will allow you to create that data or manipulate that data which is what the api is responsible of doing
from config import db # we are going toi import this from config becuz it is the instance that will give access to the sql alchemy


class Contact(db.Model): # from db it will inherit the model class now what this will do is that it will allow us to craete a database model represented as a python class
     # allow us to define the diffrent fields that using python code
     id = db.Column(db.Integer, primary_key = True)
     first_name = db.Column(db.String(80),unique = False, nullable = False)
     last_name = db.Column(db.String(80),unique = False, nullable = False)
     email = db.Column(db.String(120),unique = True, nullable = False)

     def to_json(self): #take all of teh diffrent fields in the object and then convert them into a python dictionary which we can then convert into JSON
          #When we create an API we communicate using JSON(Javascript Object Notation) we will be sending to the api in JSOn and the API will send the objects in JSON
          return {
               "id":self.id,
               "firstName":self.first_name,
               "lastName":self.last_name,
               "email":self.email,
          }
          

