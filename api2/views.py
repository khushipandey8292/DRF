from django.shortcuts import render
from .models import Student1
import io
from .serializers import Student1Serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http  import HttpResponse,JsonResponse

def student_api(request):
    if request.method =='GET':
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