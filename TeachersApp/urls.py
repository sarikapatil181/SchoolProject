from django.contrib import admin
from django.urls import path,include
from .views  import Teachers_upload
from .views import searchbar,index

urlpatterns = [
   path('',index,name='index'),
   path('csvUpload/',Teachers_upload,name='Teachers_upload'),
   path('search/', searchbar, name='search_result'),
   
]