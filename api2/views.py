from django.shortcuts import render
from .models import Student1
import io
from .serializers import Student1Serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http  import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


#function based

# @csrf_exempt
# def student_api(request):
#     if request.method =='GET':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id',None)
#         if id is not None:
#             stu=Student1.objects.get(id=id)
#             serializer=Student1Serializer(stu)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu=Student1.objects.all()
#         serializer=Student1Serializer(stu,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
    
    
    
#     if request.method=='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=Student1Serializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
    
    
    
#     if request.method=='PUT':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu=Student1.objects.get(id=id)
#         serializer=Student1Serializer(stu,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data updated!!'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
    
    
    
#     if request.method=='DELETE':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu=Student1.objects.get(id=id)
#         stu.delete()
#         res={'msg':'Data deleted!!'}
#         json_data=JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type='application/json')
   
from django.utils.decorators import method_decorator
from django.views import View 
# class based     

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student1.objects.get(id=id)
            serializer=Student1Serializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student1.objects.all()
        serializer=Student1Serializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
  
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=Student1Serializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student1.objects.get(id=id)
        serializer=Student1Serializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data updated!!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student1.objects.get(id=id)
        stu.delete()
        res={'msg':'Data deleted!!'}
        return JsonResponse(res,safe=False)
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        
