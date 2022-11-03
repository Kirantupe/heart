from flask import Flask, render_template ,request ,jsonify
# from heart_pred import utils
from heart_pred.utils import HeartDisease


app= Flask(__name__)

@app.route("/")
def homeapi():
    return render_template("index.html")
    # return ""

@app.route("/pred_disease",methods=["GET","POST"])
def result_api():     
    
    age = int(request.args.get("age"))
    sex = int(request.args.get("sex"))
    cp = int(request.args.get("cp"))
    trestbps = int(request.args.get("trestbps"))
    chol = int(request.args.get("chol"))
    fbs = int(request.args.get("fbs"))
    restecg = int(request.args.get("restecg"))
    thalach = int(request.args.get("thalach"))
    exang = int(request.args.get("exang"))
    oldpeak = float(request.args.get("oldpeak"))
    slope = int(request.args.get("slope"))
    ca = int(request.args.get("ca"))
    thal = int(request.args.get("thal"))

    obj = HeartDisease(age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal)
    result = obj.predict_heartdisease()
    # return render_template("index.html", prediction= result  )
    if result == 0:
        return render_template("index.html",prediction="You are fit and fine")

    else:
        return render_template("index.html",prediction="Hey need to take care of your health you are having heart disease")
if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 1998, debug=True)
