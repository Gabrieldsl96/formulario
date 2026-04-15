from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pagina_inicial.urls", namespace="pagina_inicial")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("produtos/", include("produtos.urls", namespace="produtos")),
]
