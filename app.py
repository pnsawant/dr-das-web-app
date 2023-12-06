from flask import Flask, render_template, redirect, url_for
 
app = Flask(__name__)

# app name 
@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/teaching")
def teaching():
    return render_template('teaching.html')

@app.route("/research")
def research():
    return render_template('research.html')

@app.route("/publications")
def publications():
    return render_template('publications.html')

@app.route("/students")
def students():
    return render_template('students.html')

@app.route("/events")
def events():
    return render_template('events.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/contactform")
def contactform():
    return render_template('contact-form.html')

if __name__ == '__main__':
    app.run(debug=False)