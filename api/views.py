from django.shortcuts import render
from .models import Student
import io
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http  import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# def student_detail(request,pk):
#     stu=Student.objects.get(id=pk)
#     serializer=StudentSerializer(stu)

#     return JsonResponse(serializer.data)

    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')


# def student_list(request):
#     stu=Student.objects.all()
#     serializer=StudentSerializer(stu,many=True)

#     return JsonResponse(serializer.data,safe=False)

    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    
@csrf_exempt   
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data) 
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata) 
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')