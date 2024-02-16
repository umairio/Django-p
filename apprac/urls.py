from django.urls import path

from .views import contact, ibase, index

urlpatterns = [
    path("", index, name="index"),
    path("home", index, name="index"),
    path("home2/", ibase, name="ibase"),
    path("contact", contact, name="contact"),
]
