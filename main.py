from flask import Flask, render_template, url_for, request, jsonify
import os, io

app = Flask(__name__)

accountBalanceInitial = 3129.81
incomingAccBal = 3500
users = [("Garrett", ".680492", "112233"), ("Ryley", ".319508", "3422")]

stringForGoogle = "Garrett .680492 112233\nRyley .319508 3422"


@app.route("/")
def home():
    for i in users:
        print(i)
    return render_template("home.html")


@app.route("/price", methods=['POST'])
def showPrice():
    data = request.form
    if doesUserExist(data['code']):
        shareSize = round(float([user[1] for user in users if user[2] == data['code']][0]) * incomingAccBal, 2)
        percentChange = round((incomingAccBal / accountBalanceInitial - 1) * 100.0,2)
        return render_template("price.html", name=[user[0] for user in users if user[2] == data['code']],
         shareSize=shareSize, percentChange=percentChange)
    else:
        print("Enter Valid Code")
        return "Enter a Valid Code Please"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/update", methods=['POST'])
def update():
    headers = request.headers
    global incomingAccBal
    if request.method == 'POST' and headers.get("X-Api-Key") == "gj353o4jsdfsfj4":
        incomingAccBal = request.json['newbal']
        print(incomingAccBal)
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

# @app.context_processor
# def override_url_for():
#     return dict(url_for=dated_url_for)

# def dated_url_for(endpoint, **values):
#     if endpoint == 'static':
#         filename = values.get('filename', None)
#         if filename:
#             file_path = os.path.join(app.root_path,
#                                  endpoint, filename)
#             values['q'] = int(os.stat(file_path).st_mtime)
#     return url_for(endpoint, **values)

def doesUserExist(accountKey):
    for user in users:
        if user[2] == accountKey:
            return True
    
    return False




if __name__ == "__main__":

    
    f = open("accountInfo.txt", "r")
    Lines = f.readlines()
    if Lines != None: 
        for line in Lines:
            name, share, code = line.split()
            users.append((name, share, code))
            print("Here is name: {}\n Here is share: {} ,   {}".format(name,share, code))
    
    

    
    app.run(debug=True)