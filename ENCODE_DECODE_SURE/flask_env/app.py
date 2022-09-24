from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                           name="TITRE")

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       string = request.form.get("string")
       password = request.form.get("password")
       return f"Nous allons passé à l'execution avec comme mot de passe : {password}<br>Et en encodant : {string}"
    return render_template("form.html")

if __name__=='__main__':
   app.run()