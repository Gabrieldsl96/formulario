from django.urls import path

from . import views

app_name = "produtos"

urlpatterns = [
    path("", views.lista, name="list"),
    path("criar/", views.criar, name="create"),
    path("<int:pk>/editar/", views.editar, name="update"),
    path("<int:pk>/excluir/", views.excluir, name="delete"),
]
