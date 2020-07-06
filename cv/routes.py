from flask import Flask, render_template, url_for
from cv import app
from cv.models import About, Education, Experience, Skills, Hobbies, Certifications, Links
from datetime import datetime


@app.route("/")
def hello():
    about = About.query.filter_by(id=0).first()
    experience = Experience.query.order_by(Experience.start_date.desc()).all()
    certifications = Certifications.query.order_by(Certifications.name).all()
    education = Education.query.order_by(Education.start_date.desc()).all()
    hobbies =Hobbies.query.order_by(Hobbies.name).all()
    skills = Skills.query.order_by(Skills.category).all()
    return render_template("index.html", about=about, experience=experience, \
        education=education, certifications=certifications, hobbies=hobbies, \
        skills=skills)