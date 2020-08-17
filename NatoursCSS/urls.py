from django.urls import path
from NatoursCSS import views

app_name = 'NatoursCSS'

urlpatterns = [

    path('', views.home, name='home_view')

]
