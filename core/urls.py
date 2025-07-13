
from django.urls import path , include
from django.contrib import admin
from django.urls import path , include

from django.shortcuts import render, redirect

from core.views import *

urlpatterns = [
    path("",  lambda request: redirect("country")),

    path("hx/state", HxStateView.as_view(),  name="hx_state"),
    path("hx/city", HxCityView.as_view(),  name="hx_city"),

    path('countries/', CountryView.as_view(), name="country"),
]
