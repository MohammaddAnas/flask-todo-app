from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# -----------------------------
# Flask App Configuration
# -----------------------------
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# -----------------------------
# Database Model
# -----------------------------
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"{self.sno} - {self.title}"


# -----------------------------
# Home Page
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def hello_world():

    # Add a new todo
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]

        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

        return redirect("/")

    # Search todo
    search = request.args.get("search")

    if search:
        allTodo = Todo.query.filter(
            Todo.title.contains(search) |
            Todo.desc.contains(search)
        ).all()
    else:
        allTodo = Todo.query.all()

    return render_template(
        "index.html",
        allTodo=allTodo,
        search=search
    )


# -----------------------------
# Delete Todo
# -----------------------------
@app.route("/delete/<int:sno>")
def delete(sno):
    abc = Todo.query.filter_by(sno=sno).first()

    db.session.delete(abc)
    db.session.commit()

    return redirect("/")


# -----------------------------
# Update Todo
# -----------------------------
@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):

    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]

        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc

        db.session.add(todo)
        db.session.commit()

        return redirect("/")

    search = request.args.get("search")

    if search:
        allTodo = Todo.query.filter(
            Todo.title.contains(search) |
            Todo.desc.contains(search)
        ).all()
    else:
        allTodo = Todo.query.all()

    todo = Todo.query.filter_by(sno=sno).first()

    return render_template("update.html", todo=todo)


# -----------------------------
# Change Todo Status
# -----------------------------
@app.route("/status/<int:sno>", methods=["POST"])
def status(sno):
    todo = Todo.query.filter_by(sno=sno).first()

    todo.completed = not todo.completed
    db.session.commit()

    return redirect("/")


# -----------------------------
# About Page
# -----------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()