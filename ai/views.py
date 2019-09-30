from django.shortcuts import render,redirect
from django.views import View
from . import forms
import json
from django.http import JsonResponse
import numpy as np
import ast
import requests
import cv2
import logging
    
logger = logging.getLogger()

logger.setLevel(logging.INFO)

def message(status_code,data,msg):
    
    return JsonResponse({
        "status_code":200,
        "headers":{},
        "payload":{
            "data":data,
            "msg":msg
        },
    })
    
class CNN(View):

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
        
        cv2.imwrite("a.jpeg",decoded)

        kernel = np.ones((4,4),np.uint8)

        
        decoded = cv2.erode(decoded,kernel,iterations = 1)
        decoded = cv2.resize(decoded, (128, 128), interpolation = cv2.INTER_LANCZOS4)
        decoded = cv2.cvtColor(decoded,cv2.COLOR_GRAY2RGB)
        decoded = decoded.reshape((1, 128, 128, 3))
        
        data =json.dumps({
                "data":{
                    "cnn":decoded.tolist(),
                    "shape":decoded.shape
                }
            }
        )

        result = requests.post(
            'https://wnyx0j0xr2.execute-api.us-west-2.amazonaws.com/cnn',
            data=data
        )

        return ast.literal_eval(result.text)

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
        pass
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
        print(data)
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
            pred_class = np.asarray(data["payload"]["predictions"]).argmax(axis=-1)
            anomalies = self.cnn_anomaly[int(pred_class[0])]

        context = {
            "predict":anomalies,
            "type":data["type"]
        }
        return render(request,"resultado.html",context)


def comments(request):
    data = json.dumps({
        "data":{
                "ok_result":str(request.POST.get("ok_result")),
                "comment":request.POST.get("comment")
            }
        }
    )

    result = requests.post(
        'https://p7j18vju8i.execute-api.us-west-2.amazonaws.com/mongo_api',
        data=data
    )

    return JsonResponse(ast.literal_eval(result.text))
