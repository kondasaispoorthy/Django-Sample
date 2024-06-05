from django.shortcuts import render
from django.http import JsonResponse
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET'])
def StudentList(request):
    list = Students.objects.all().order_by('id')
    serializer = StudentsSerializer(list,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def StudentDetail(request,pk):
    # list = Students.objects.get(id=pk)
    list = get_object_or_404(Students,id=pk)
    serializer = StudentsSerializer(list,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def StudentCreate(request):
    serializer = StudentsSerializer(data=request.data)
    if  serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def StudentUpdate(request,pk):
    #list = Students.objects.get(id=pk)
    list = get_object_or_404(Students,id=pk)
    serializer = StudentsSerializer(instance = list,data=request.data)
    if  serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def StudentDelete(request,pk):
    #list = Students.objects.get(id=pk)
    list = get_object_or_404(Students,id=pk)
    list.delete()
    return Response("Item Deleted Successfully")




