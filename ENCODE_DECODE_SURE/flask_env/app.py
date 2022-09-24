from flask import Flask, request, render_template
app = Flask(__name__)
from deltacode_class import ROT, DayEncoding, Cesar
@app.route("/")
def index():
    return render_template("index.html",
                           name="TITRE")

@app.route('/', methods =["GET", "POST"])
def encoder():
    if request.method == "POST":
        action()
       # coding = request.form.get("coding")
        string = request.form.get("string")
        password = request.form.get("password")
        shift = request.form.get("shift")
        try:
           shift = int(shift)
        except:
           return "Le shift doit être un nombre /!\\"
        return DayEncoding(password=password, string=string, shift=shift).encode()
    return render_template("index.html")

@app.route('/', methods =["GET", "POST"])
def decoder():
    if request.method == "POST":
       # coding = request.form.get("coding")
       string = request.form.get("string")
       password = request.form.get("password")
       shift = request.form.get("shift")
       try:
           shift = int(shift)
       except:
           return "Le shift doit être un nombre /!\\"
       return DayEncoding(password=password, string=string, shift=shift).decode()
    return render_template("index.html")

@app.route('/')
def action():
    return "hey"
if __name__=='__main__':
   app.run()