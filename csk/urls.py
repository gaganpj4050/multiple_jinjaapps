from django.urls import path
from csk.views import *
app_name='csk'
urlpatterns=[
    path('dhoni_print/',dhoni_print,name='dhoni_print')
]    