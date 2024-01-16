from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.
@api_view(['GET'])
def overview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
        
    }

    return Response(api_urls)

# List
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    if tasks.exists() :
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    return Response('{}')
    
# Detail View
@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.filter(id=pk)
    if task.exists():
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    else :
        return Response('{}')


# Create
@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Update
@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return HttpResponse(f'Task with id {pk} deleted successfully')
    
