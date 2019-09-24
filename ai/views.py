from django.shortcuts import render,redirect
from django.views import View
from . import forms
import json
import joblib
from django.http import JsonResponse
import numpy as np
import ast
import os
import ast
import requests
import cv2
from keras.models import model_from_json
import pymongo
from django.conf import settings 
from PIL import Image


class CNN(View):
    #model = load_model('./models/models_ECGModel.hdf5')
    model_file = open('./models/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)
    model.load_weights('./models/weights_cnn.h5')
    model._make_predict_function()          # Necessary

    def post(self,request):

        data = self.model_predict(request.FILES["ecg"])
        response = JsonResponse(data)
        response.set_cookie('data',data)
        
        return response

    def get(self,request):
        context = {
            "ecg":forms.FileUploadForm()
        }

        return render(request,"cnn.html",context)

    def model_predict(self,ecg_file):
        
        decoded = cv2.imdecode(np.frombuffer(ecg_file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
        kernel = np.ones((4,4),np.uint8)
        
        decoded = cv2.erode(decoded,kernel,iterations = 1)
        decoded = cv2.resize(decoded, (128, 128), interpolation = cv2.INTER_LANCZOS4)
        decoded = cv2.cvtColor(decoded,cv2.COLOR_GRAY2RGB)
        
        pred = self.model.predict(decoded.reshape((1, 128, 128, 3)))    
        pred_class = pred.argmax(axis=-1)

        """
        data =json.dumps({
                "data":{
                    "cnn":decoded.tolist()
                }
            }
        )
        
        result = requests.post(
            'https://1zwso47y6c.execute-api.us-west-2.amazonaws.com/TT',
            data=data
        )
        
        context = ast.literal_eval(result.text)
        """
        
        return {
            "type":2,
            "status_code":200,
            "headers":{},
            "payload":{
                "predict":str(pred_class[0])
            },
        }    

class RF(View):
    def post(self,request):
        info = forms.RFDataModelSecondForm()
        info.values(request.POST)
        
        data = self.random_forest(info.data_values)
        
        response = JsonResponse(data)
        response.set_cookie('data',data)

        return response

    def get(self,request):

        context = {
            "model1":forms.RFDataModelSecondForm
        }
        return render(request,"rf.html",context)
     
    def random_forest(self,data):

        result = requests.post(
            'https://1zwso47y6c.execute-api.us-west-2.amazonaws.com/TT',
            data=data
        )

        context = ast.literal_eval(result.text)

        return context
    
class ProcessData(View):
    def post(self,request):
        print(request)

    def get(self,request):
        return render(request,"espera.html")

class ShowData(View):
    rf_anomaly = {
        1:"Normal",
        2:"Cambios isquémicos (enfermedad de la arteria coronaria)",
        3:"Infarto de miocardio anterior anterior",
        4:"Infarto de miocardio inferior",
        5:"Taquicardia sinusal",
        6:"Bradicardia sinusal",
        7:"Bloque de rama derecha"
    }
    
    cnn_anomaly = {
        1:"Normal",
        4:"Contracción ventricular prematura (PVC)",
        3:"Ritmo estimulado (PAB)",
        5:"Latido de bloqueo de rama derecha (RBB)",
        2:"Latido de bloqueo de rama izquierda (LBB)",
        0:"Contracción prematura auricular (APC)",
        6:"Latido de escape centricular (VEB)"
    }

    def get(self,request):
        data = ast.literal_eval(request.COOKIES.get('data'))

        if data["type"] == 1:
            anomalies = {}
            predict = data["payload"]["predict"]
            for i in range(2):
                first = predict.index(max(predict))
                anomalies[self.rf_anomaly[first]] = "{:.3f}".format(max(predict)*100)
                predict[first] = -1
            second = max(predict)
            del predict[predict.index(second)]
    
        elif data["type"] == 2:
            anomalies = self.cnn_anomaly[int(data["payload"]["predict"])]

        context = {
            "predict":anomalies,
            "type":data["type"]
        }
        return render(request,"resultado.html",context)


def comments(request):
    mongo = settings.DB_MONGO.arrhytmias.comments
    
    content = {
        "ok":str(request.POST.get("ok_result")),
        "comment":request.POST.get("comment")
    }

    mongo.insert_one(content)
    
    return JsonResponse({
            "status_code":200,
            "headers":{},
            "payload":{
                "data":""
            },
    })