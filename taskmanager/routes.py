from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # adding new category
    if request.method == "POST":
        #grabs name from form input and creates new entry in Category table
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        #redirects user to categories page after submitting
        return redirect(url_for("categories"))
    return render_template("add_category.html")