
from django.urls import path , include
from django.contrib import admin
from django.urls import path , include

from django.shortcuts import render, redirect

from  contacts.views import *

urlpatterns = [
    path("", CreateContactView.as_view(), name="create_contact"),
    path("hx/companies/add", HxCreateCompanyView.as_view(), name="hx_create_company"),
    ]