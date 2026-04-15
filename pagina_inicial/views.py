from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from produtos.models import Produto


@login_required
def index(request):
    total_produtos = Produto.objects.count()
    context = {
        "titulo": "Dashboard",
        "total_produtos": total_produtos,
    }
    return render(request, "pagina_inicial/index.html", context)
