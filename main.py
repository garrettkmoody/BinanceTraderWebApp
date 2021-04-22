from flask import Flask, render_template, url_for, request, jsonify
import os, io

app = Flask(__name__)

accountBalance = "5000"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/price", methods=['GET'])
def showPrice():
    return render_template("price.html", value=accountBalance)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/price", methods=['POST'])
def update():
    headers = request.headers
    if request.method == 'POST' and doesUserExist(headers.get("X-Api-Key")):
        
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

def doesUserExist(accountKey):
    return True



if __name__ == "__main__":
    f = open("accountInfo.txt", "r")
    Lines = f.readlines()
    for line in Lines:
        name, share = line.split()
        print("Here is name: {}\n Here is share: {} ".format(name,share))

    
    app.run(debug=True)