from django.shortcuts import render
from .models import student
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_detail(request,pk):
    stu = student.objects.get(id=pk)
    print("stuuuu",stu)
    seriaizer = studentSerializer(stu)
    print("seriazierrrr",seriaizer)
    json_data= JSONRenderer().render(seriaizer.data)
    print("json",json_data)
    return HttpResponse(json_data,content_type='application/json')


def student_list(request):
    stu = student.objects.all()
    print("stuuuu",stu)
    seriaizer = studentSerializer(stu,many=True)
    print("seriazierrrr",seriaizer)
    json_data= JSONRenderer().render(seriaizer.data)
    print("json",json_data)
    return HttpResponse(json_data,content_type='application/json')
