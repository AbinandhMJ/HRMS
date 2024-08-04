from django.contrib import admin
from django.urls import path,include,re_path
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('userlogin.urls')),
]
