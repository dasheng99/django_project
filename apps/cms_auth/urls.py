from django.urls import path
from . import views

app_name = 'cms_auth'

urlpatterns = [
    path('login',views.login_view,name= 'login')
]