from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from base.models import Task , Priority , Category
from base.models import Profile
from .serializers import taskSerializer , profileSerializer , categorySerializer , prioritySerializer
from django.shortcuts import get_object_or_404



class TaskViewSets(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=taskSerializer
    
#@api_view(['GET'])
#def getData(request):
 #   Tasks= Task.objects.all()
  #  serializer=taskSerializer(Tasks , many=True)
   # return Response(serializer.data)


#@api_view(['POST'])
#def addTask(request):
 #    serializer=taskSerializer(data=request.data)
  #   if serializer.is_valid():
   #     serializer.save()
    #    return Response(serializer.data)
     #return Response(serializer.errors)

#@api_view(['GET' , 'PUT', 'DELETE'])
#def taskdetail(request , id):
    
 #   try:
  #      task=Task.objects.get(pk=id)
   # except Task.DoesNotExist:
    #    return Response(status=status.HTTP_404_NOT_FOUND)
    
    #if request.method =='GET':
     #   serializer=taskSerializer(task )
      #  return Response(serializer.data)

    #elif request.method =='PUT':
     #   serializer=taskSerializer(task , data=request.data)
      #  if serializer.is_valid():
       #     serializer.save()
        #    return Response(serializer.data)
        #return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    
  #  elif request.method=='DELETE':
   #     task.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def profileList(request):
    profiles=Profile.objects.all()
    serializer=profileSerializer(profiles , many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addProfile(request):
    serializer=profileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)



@api_view(['GET', 'PUT' , 'DELETE'])
def profileDetail(request , id):
    try :
        profile=Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer=profileSerializer(profile )
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer=profileSerializer(profile , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method=='DELETE':
        profile.delete()
        return Response( {"message":"Profile deleted"})
    
@api_view(['POST'])
def addCategory(request):
     serializer=categorySerializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
     return Response(serializer.errors)

@api_view(['GET', 'PUT' ,'DELETE'])
def categoryDetail(request , id):
    try:
        category=Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer=categorySerializer(category )
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer=categorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method=='DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def addPriority(request ):
    serializer=prioritySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET', 'PUT' , 'DELETE'])
def priorityDetail(request , id):
    try:
        priority=Priority.objects.get(pk=id)
    except Priority.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer=prioritySerializer(priority )
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer=prioritySerializer(priority, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)








