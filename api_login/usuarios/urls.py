from django.urls import path

from .views import(
    RegistroView,
    PerfilView,
    LogoutView,
)

urlpatterns = [

    path(
    "registro/",
    RegistroView.as_view(),
    name= "registro"
    ),

    path(
        "perfil/",
        PerfilView.as_view(),
        name="perfil"
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name= "logout"
        ),

]