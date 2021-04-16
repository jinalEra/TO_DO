from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import rest_framework

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include("todos.urls")),
    path('apis/v1/', include("apis.urls")),
    
]
