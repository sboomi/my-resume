from cv import db
from datetime import datetime

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    adress1 = db.Column(db.String)
    adress2 = db.Column(db.String)
    postalcode = db.Column(db.Integer)
    dob = db.Column(db.DateTime) #db.DateTime
    country = db.Column(db.String)
    driver_license = db.Column(db.String)
    city = db.Column(db.String)
    phone_number = db.Column(db.String)
    mail = db.Column(db.String)
    
    def __repr__(self):
        return f"About({self.id}, {self.first_name}, {self.last_name}, \
            {self.adress1}, {self.adress2}, {self.postalcode}, {self.city}, \
            {self.phone_number}, {self.mail}, {self.dob}, \
            {self.country}, {self.driver_license})"


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    diploma = db.Column(db.String)
    school = db.Column(db.String)
    location = db.Column(db.String)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"Education({self.id}, {self.start_date}, {self.end_date}, {self.diploma}, \
            {self.school}, {self.location}, {self.description})"



class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    position = db.Column(db.String)
    company = db.Column(db.String)
    location = db.Column(db.String)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"Experience({self.id}, {self.start_date}, {self.end_date}, \
            {self.position}, {self.company}, {self.location}, {self.description})"

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    name = db.Column(db.String)

    def __repr__(self):
        return f"Skills({self.id}, {self.category}, {self.name})"

class Hobbies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"Hobbies({self.id}, {self.name})"

class Certifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    organization = db.Column(db.String)
    completion_date = db.Column(db.DateTime)
    expiration_date = db.Column(db.DateTime)
    certification_id = db.Column(db.String)

    def __repr__(self):
        return f"Certifications({self.id}, {self.name}, {self.organization}, \
            {self.completion_date}, {self.expiration_date}, {self.certification_id})"

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String)
    url = db.Column(db.String)

    def __repr__(self):
        return f"Links({self.id}, {self.website}, {self.url})"