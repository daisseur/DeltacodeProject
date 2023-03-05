from flask import *
import json
from markupsafe import escape
from string import ascii_lowercase
import inspect
from DeltacodeProject.encodings2 import *
app = Flask(__name__, template_folder="templates", static_folder="js")

def get_kwargs(class_):
    keys, _, _, values = inspect.getargvalues(class_)
    kwargs = {}
    for key in keys:
        if key != 'self':
            kwargs[key] = values[key]
    return kwargs

@app.route("/")
def home():
    return render_template("index.html", name="index.html")

# @app.route('/DayEncoding/<hexa>/<password>/<shift>/<string>')
# def encode(hexa, password, shift, string):
#     try:
#         shift = int(shift)
#     except:
#         return "bad arguments"
#     if hexa.lower() in ["yes", "true", "ok"]:
#         hexa = True
#     elif hexa.lower() in ["no", "false", "not"]:
#         hexa = False
#     else:
#         return "bad arguments"
#     res = DayEncoding(password=password, shift=shift, hexa=hexa).encode(string).string
#     print(res)
#     return res

@app.post('/DayEncoding/encode')
def get_dayencoding_encode():
    args = {"password": '', "hexa": True, "shift": 0, "string": ''}
    print(request.is_json)
    request.get_json(force=True)
    # verif
    if not "string" in request.json.keys():
        return "Bad arguments"
    for key in request.json:
        if key not in args.keys():
            return "Bad arguments"
        else:
            args[key] = request.json[key]
    res = DayEncoding(password=args["password"], shift=args["shift"], hexa=args["hexa"]).encode(args["string"])
    dict_res = {}
    for k in res.__init__.__code__.co_varnames[1:]:
        value = eval(f"res.{k}")
        if isinstance(value, str|float|int|list|tuple|bool):
            dict_res[k] = eval(f"res.{k}")
    return jsonify(dict_res)

@app.post('/DayEncoding/decode')
def get_dayencoding_decode():
    args = {"password": '', "hexa": True, "shift": 0, "string": ''}
    print(request.is_json)
    request.get_json(force=True)
    # verif
    if not "string" in request.json.keys():
        return "Bad arguments"
    for key in request.json:
        if key not in args.keys():
            return "Bad arguments"
        else:
            args[key] = request.json[key]
    res = DayEncoding(password=args["password"], shift=args["shift"], hexa=args["hexa"]).decode(args["string"])
    dict_res = {}
    for k in res.__init__.__code__.co_varnames[1:]:
        value = eval(f"res.{k}")
        if isinstance(value, str|float|int|list|tuple|bool):
            dict_res[k] = eval(f"res.{k}")
    return jsonify(dict_res)

@app.post('/ROT/encode')
def get_rot_encode():
    args = {"password": '', "hexa": True, "shift": 0, "string": ''}
    print(request.is_json)
    request.get_json(force=True)
    # verif
    if not "string" in request.json.keys():
        return "Bad arguments"
    for key in request.json:
        if key not in args.keys():
            return "Bad arguments"
        else:
            args[key] = request.json[key]
    res = ROT(password=args["password"], shift=args["shift"], hexa=args["hexa"]).encode(args["string"])
    dict_res = {}
    for k in res.__init__.__code__.co_varnames[1:]:
        value = eval(f"res.{k}")
        if isinstance(value, str|float|int|list|tuple|bool):
            dict_res[k] = eval(f"res.{k}")
    return jsonify(dict_res)

@app.post('/ROT/decode')
def get_rot_decode():
    args = {"password": '', "string": ''}
    print(request.is_json)
    request.get_json(force=True)
    # verif
    if not "string" in request.json.keys():
        return "Bad arguments"
    for key in request.json:
        if key not in args.keys():
            return "Bad arguments"
        else:
            args[key] = request.json[key]
    res = ROT(password=args["password"]).decode(args["string"])
    dict_res = {}
    for k in res.__init__.__code__.co_varnames[1:]:
        value = eval(f"res.{k}")
        if isinstance(value, str|float|int|list|tuple|bool):
            dict_res[k] = eval(f"res.{k}")
    return jsonify(dict_res)

@app.post('/Cesar/encode')
def get_cesar_encode():
    args = args = {"rot": 0, "string": ''}
    print(request.is_json)
    request.get_json(force=True)
    # verif
    if not "string" in request.json.keys():
        return "Bad arguments"
    for key in request.json:
        if key not in args.keys():
            return "Bad arguments"
        else:
            args[key] = request.json[key]
    res = Cesar(rot=args["rot"]).encode(args["string"])
    dict_res = {}
    for k in res.__init__.__code__.co_varnames[1:]:
        value = eval(f"res.{k}")
        if isinstance(value, str|float|int|list|tuple|bool):
            dict_res[k] = eval(f"res.{k}")
    return jsonify(dict_res)

@app.post('/Cesar/decode')
def get_cesar_decode():
    args = {"rot": 0, "string": ''}
    print(request.is_json)
    request.get_json(force=True)
    # verif
    if not "string" in request.json.keys():
        return "Bad arguments"
    for key in request.json:
        if key not in args.keys():
            return "Bad arguments"
        else:
            args[key] = request.json[key]
    res = Cesar(rot=args["rot"]).decode(args["string"])
    dict_res = {}
    for k in res.__init__.__code__.co_varnames[1:]:
        value = eval(f"res.{k}")
        if isinstance(value, str|float|int|list|tuple|bool):
            dict_res[k] = eval(f"res.{k}")
    return jsonify(dict_res)

@app.post('/Custom/encode')
def get_custom_encode():
    args = {"password": '', "string": '', "custom": ascii_lowercase}
    print(request.is_json)
    request.get_json(force=True)
    # verif
    if not "string" in request.json.keys():
        return "Bad arguments"
    for key in request.json:
        if key not in args.keys():
            return "Bad arguments"
        else:
            args[key] = request.json[key]
    res = Custom(password=args["password"], custom=args["custom"]).encode(args["string"])
    dict_res = {}
    for k in res.__init__.__code__.co_varnames[1:]:
        value = eval(f"res.{k}")
        if isinstance(value, str|float|int|list|tuple|bool):
            dict_res[k] = eval(f"res.{k}")
    return jsonify(dict_res)

@app.post('/Custom/decode')
def get_custom_decode():
    args = {"password": '', "string": '', "custom": ascii_lowercase}
    print(request.is_json)
    request.get_json(force=True)
    # verif
    if not "string" in request.json.keys():
        return "Bad arguments"
    for key in request.json:
        if key not in args.keys():
            return "Bad arguments"
        else:
            args[key] = request.json[key]
    res = Custom(password=args["password"], custom=args["custom"]).decode(args["string"])
    dict_res = {}
    for k in res.__init__.__code__.co_varnames[1:]:
        value = eval(f"res.{k}")
        if isinstance(value, str|float|int|list|tuple|bool):
            dict_res[k] = eval(f"res.{k}")

    return jsonify(dict_res)

app.run("192.168.1.7", 5000, debug=True)