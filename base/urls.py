from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . views import TaskViewSets , ProfileViewSets , CategoryViewSets


router=DefaultRouter()
router.register(r'tasks', TaskViewSets)
router.register(r'profile', ProfileViewSets)
router.register(r'category', CategoryViewSets)


urlpatterns = [
    path ("",include (router.urls))
    ]