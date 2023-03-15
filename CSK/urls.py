from django.urls import path
from CSK.views import *

app_name='something'

urlpatterns=[
    path('Dhoni/',Dhoni,name='Dhoni'),
]