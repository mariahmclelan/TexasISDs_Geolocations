# from flask import Flask, render_template, jsonify
# from flask_pymongo import PyMongo

# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/texasSchoolsDB"
# mongo = PyMongo(app)

# @app.route("/")
# def home_page():
#     lats = mongo.db.scores_finances.find({"per student budget": 13087})
#     data = []
#     for doc in lats:
#         # Convert ObjectId to string for each document
#         doc['_id'] = str(doc['_id'])
#         data.append(doc)
    
#     return jsonify(data)

# @app.route("/api/v1.0/texasISDs/perStudentBudget/<perStudentBudget>")
# def perStudentBudget(perStudentBudget):
#     lats = mongo.db.scores_finances.find({"per student budget": {"$gte": perStudentBudget}})
#     data = []
#     for doc in lats:
#         # Convert ObjectId to string for each document
#         doc['_id'] = str(doc['_id'])
#         data.append(doc)
    
#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, jsonify, abort
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/texasSchoolsDB"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    lats = mongo.db.school_info.find({})
    data = []
    for doc in lats:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return jsonify(data)

@app.route("/api/v1.0/texasISDs/perStudentBudget/<perStudentBudget>")
def perStudentBudget(perStudentBudget):
    try:
        perStudentBudget = int(perStudentBudget)  # Convert parameter to integer
    except ValueError:
        abort(400, "Invalid perStudentBudget value")

    try:
        lats = mongo.db.scores_finances.find({"per student budget": {"$gte": perStudentBudget}})
        data = []
        for doc in lats:
            doc['_id'] = str(doc['_id'])
            data.append(doc)
        return jsonify(data)
    except Exception as e:
        print("Error:", e)
        abort(500, "An error occurred while processing the request")

if __name__ == "__main__":
    app.run(debug=True)
