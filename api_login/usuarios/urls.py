from django.urls import path

from usuarios.views import RegistroView


urlpatterns = [
    path("registro/", RegistroView.as_view(), name="registro"),
]