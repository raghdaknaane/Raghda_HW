from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import os
import random, string


def randomword(length):
    letters=string.ascii_letters
    return ''.join(random.choice(letters)for i in range(length))

app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies3.db'
app.config['UPLOAD_FOLDER'] = 'static/upload/'
app.config['MAX_CONTENT'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg', 'gif', 'jfif', 'avif']

db = SQLAlchemy(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Connect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    message = db.Column(db.String(100), unique=False, nullable=False)
    email_user = db.Column(db.String(100), unique=False, nullable=False)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
    director = db.Column(db.String(20), unique=False, nullable=False)
    release_year = db.Column(db.Integer, unique=False, nullable=False)
    filename = db.Column(db.String(100), unique=False, nullable=True)
    name_actors = db.Column(db.String, unique=False, nullable=True)
    video = db.Column(db.String, unique=False, nullable=True)

    def __repr__(self):
        return f"Title: {self.movie_title}, Director: {self.director}"


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    review_text = db.Column(db.String, unique=False, nullable=False)
    rating_movie = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f"Name: {self.name}, Content: {self.review_text}, Rating Movie: {self.rating_movie}"


migrate = Migrate(app, db)


@app.route("/")
def home_movies():
    movies_data = Movies.query.all()
    return render_template("index.html", movies_data=movies_data)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        search = "%{0}%".format(search_value)
        movies_data = Movies.query.filter(Movies.movie_title.like(search)).all()

        return render_template('index.html', movies_data=movies_data, pageTitle='Movies', legend="Search Results")
    else:
        return redirect("/")


@app.route("/add_data")
def add_data():
    return render_template("add_profile.html")



@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/add", methods=["POST", "GET"])
def movie_management():
    if request.method == "POST":
        movie_title = request.form.get("movie_title")
        description = request.form.get("description")
        director = request.form.get("director")
        release_year = request.form.get("release_year")
        name_actors = request.form.get("name_actors")
        file = request.files.get("filename")
        video = request.form.get("video")
        file = request.files.get("filename")
        randomstring = randomword(10)
        if allowed_file(file.filename):
            file_split = file.filename.split(".")
            final_name = f"{file_split[0]}_{randomstring}.{file_split[1]}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], final_name))
        movie_row = Movies(movie_title=movie_title, description=description, director=director,
                           release_year=release_year, filename=final_name, name_actors=name_actors, video=video)
        db.session.add(movie_row)
        db.session.commit()
        return redirect("/")


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='upload/' + filename))


@app.route('/movie_info/<movie_id>')
def movie_info(movie_id):
    movie_specific = Movies.query.get(movie_id)
    reviews_specific = Reviews.query.filter(Reviews.movie_id == movie_id)

    return render_template("movie_info.html", movie_specific=movie_specific, reviews_specific=reviews_specific)


@app.route("/add_review", methods=["POST", "GET"])
def review_management():
    if request.method == "POST":
        name = request.form.get("name")
        review_text = request.form.get("review_text")
        movie_id = request.form.get("movie_id")
        rating_movie = request.form.get("rating_movie")
        review_row = Reviews(name=name, review_text=review_text, movie_id=movie_id, rating_movie=rating_movie)
        db.session.add(review_row)
        db.session.commit()
        return redirect(url_for('movie_info', movie_id=movie_id))


@app.route("/delete/<int:id>")
def erase(id):
    data = Movies.query.get(id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}/{filename}")
    db.session.delete(data)
    reviews_specific = Reviews.query.filter(Reviews.movie_id == id)
    for review in reviews_specific:
        db.session.delete(review)
    db.session.commit()
    return redirect("/")


@app.route('/add_connect')
def connect_us():
    return render_template("connect.html")


@app.route("/add_connect", methods=["POST", "GET"])
def connect_management():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        email_user = request.form.get("email_user")
        connect_row = Connect(name=name, email_user=email_user, message=message)
        db.session.add(connect_row)
        db.session.commit()
        return redirect("/")


@app.route("/alter_movie/<int:id>", methods=["POST", "GET"])
def alter_movie(id):
    if request.method == "POST":
        data = Movies.query.get(id)
        movie_title = request.form.get("movie_title")
        description = request.form.get("description")
        director = request.form.get("director")
        name_actors = request.form.get("name_actors")
        release_year = request.form.get("release_year")
        file = request.files.get("filename")
        video = request.form.get("video")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
        file_name = file.filename
        if movie_title:
            data.movie_title = movie_title
        if description:
            data.description = description
        if director:
            data.director = director
        if name_actors:
            data.name_actors = name_actors

        if release_year:
            data.release_year = release_year
        if file_name:
            data.filename = file_name

        if video:
            data.video = video
        db.session.commit()
        return redirect(url_for("movie_info", movie_id=id))
    else:
        return render_template("alter_movie.html")


if __name__ == "__main__":
    app.run()
