from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('forgot-pass',views.forgot,name="forgot"),
    path('reset',views.reset,name="reset")
]