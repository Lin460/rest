from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from base.models import Task  , Category
from base.models import Profile
from .serializers import taskSerializer , profileSerializer , categorySerializer 
from django.shortcuts import get_object_or_404



class TaskViewSets(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=taskSerializer




class  ProfileViewSets(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=profileSerializer
    
    
class CategoryViewSets(viewsets.ModelViewSet):
 queryset=Category.objects.all()
 serializer_class=categorySerializer











