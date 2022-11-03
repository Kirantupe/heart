# from copyreg import pickle
import pandas as pd
import numpy as np
import json
import pickle
# import config

#["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
class HeartDisease(): 
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
        self.age=age
        self.sex=sex
        self.cp=cp
        self.trestbps=trestbps
        self.chol=chol
        self.fbs=fbs
        self.restecg=restecg
        self.thalach=thalach
        self.exang=exang
        self.oldpeak=oldpeak
        self.slope=slope
        self.ca=ca
        self.thal=thal
        
    # def load_model(self):
    #     with open(r"C:\Users\Kiran\Desktop\myclass\logistic regression\heart_pred")
        
    def load_model(self):
        with open(r"C:\Users\Kiran\Desktop\myclass\logistic regression\heart_pred\model.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open(r"C:\Users\Kiran\Desktop\myclass\logistic regression\heart_pred\columns_dict.json", "r") as f:
            self.json_data = json.load(f)
        
    def predict_heartdisease(self):
    
        self.load_model()  
        array = np.zeros(len(self.json_data['columns ']))
        array[0]=self.age
        array[1]=self.sex
        array[2]=self.cp
        array[3]=self.trestbps
        array[4]=self.chol
        array[5]=self.fbs
        array[6]=self.restecg
        array[7]=self.thalach
        array[8]=self.exang
        array[9]=self.oldpeak
        array[10]=self.slope
        array[11]=self.ca
        array[12]=self.thal
    
        
        result = self.model.predict([array])[0]
        print(result)
        
        # if result == 1:
        #     return "Patient is having heart disease - Precautions needed to be taken."
        # else:
        #     return "Patient is healthy, keep it up."
        
if __name__ == "__main__":
    # if result == 1:
    #         return "Patient is having heart disease - Precautions needed to be taken."
    #     else:
    #         return "Patient is healthy, keep it up."
    age =25
    sex = 1
    cp =2
    trestbps=130
    chol=168
    fbs=1
    restecg=1
    thalach=133
    exang=0
    oldpeak=2
    slope=2
    ca=2
    thal=1
    
    
    heart= HeartDisease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    heart.predict_heartdisease()
   