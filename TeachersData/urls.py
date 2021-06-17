
from django.contrib import admin
from django.urls import path,include
from TeachersApp import views
from django.conf.urls.static import static,settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('',include('TeachersApp.urls')),
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
