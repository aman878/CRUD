from django.contrib import admin  
from django.urls import path  
from Laptop import views  
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('new', views.new),  
    path('show',views.show),  
    path('edit/<id>', views.edit),  
    path('update/<id>', views.update),  
    path('delete/<id>', views.destroy),  
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)