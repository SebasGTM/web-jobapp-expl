from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.job_list, name="jobs_home"),
    path("hello/", views.hello, name="hello"),

    path("list/", views.job_list, name="job_list"),

    path("job/<int:id>", views.job_detail, name="job_detail"),
]