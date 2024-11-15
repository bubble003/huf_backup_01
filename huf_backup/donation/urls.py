from django.urls import path
from . import views

urlpatterns = [
    path("", views.make_donation, name='make_donation'),
    # path("",views.test,name='test'),
]