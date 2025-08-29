from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . views import TaskViewSets 


router=DefaultRouter()
router.register(r'tasks', TaskViewSets)
urlpatterns = [
    path ("",include (router.urls))
  #  path('' , views.getData),
   # path('add/', views.addTask),
    #path('detail/<int:id>' , views.taskdetail , name='detail'),
    #path('addprofile', views.addProfile),
    #path('profilelist' , views.profileList ,name='profilelist'),
    #path('profiledetail/<int:id>/', views.profileDetail ),
    #path('addcategory', views.addCategory), 
    #path('categorydetail/<int:id>/', views.categoryDetail),
    #path('addpriority', views.addPriority), 
    #path('prioritydetail/<int:id>/', views.priorityDetail)
    ]