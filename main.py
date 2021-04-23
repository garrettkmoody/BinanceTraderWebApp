from flask import Flask, render_template, url_for, request, jsonify
import os, io

app = Flask(__name__)

accountBalance = "3126"

users = []


@app.route("/")
def home():
    for i in users:
        print(i)
    return render_template("home.html")


@app.route("/price", methods=['POST'])
def showPrice():
    data = request.form
    print(float([user[1] for user in users if user[2] == data['code']][0]) + 5)
    if doesUserExist(data['code']):
        shareSize = float([user[1] for user in users if user[2] == data['code']][0])
        return render_template("price.html", name=[user[0] for user in users if user[2] == data['code']],
         shareSize=shareSize * accountBalance)
    else:
        print("Enter Valid Code")
        return "hey"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/price", methods=['POST'])
def update():
    headers = request.headers
    if request.method == 'POST' and headers.get("X-Api-Key") == "gthsefh983h94h":
        
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
    for user in users:
        if user[2] == accountKey:
            return True
    
    return False




if __name__ == "__main__":
    f = open("accountInfo.txt", "r")
    Lines = f.readlines()

    for line in Lines:
        name, share, code = line.split()
        users.append((name, share, code))
        print("Here is name: {}\n Here is share: {} ,   {}".format(name,share, code))

    
    app.run(debug=True)