from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('skills/', skills, name='skills'),
    path('contact/', contact, name='contact'),

]

