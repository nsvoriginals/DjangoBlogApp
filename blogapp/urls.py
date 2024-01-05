from django.urls import path,include
from . import views


urlpatterns=[
    path("login",views.login,name="login"),
    path("create",views.register_user,name="create"),
    path("write",views.publish,name="publish"),
    path("read",views.read,name="read"),
    
    
    ]