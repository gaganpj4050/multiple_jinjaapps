from django.urls import path
from rcb.views import *
app_name='rcb'
urlpatterns=[
    path('virat_print/',virat_print,name='virat_print')
]