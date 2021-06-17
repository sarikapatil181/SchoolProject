
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static,settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('TeachersApp.urls')),
    #path('csv_upload/',views.Teachers_upload,name='Teachers_upload'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
