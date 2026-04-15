from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProdutoForm
from .models import Produto


@login_required
def lista(request):
    produtos = Produto.objects.all()
    context = {"produtos": produtos}
    return render(request, "produtos/list.html", context)


@login_required
def criar(request):
    form = ProdutoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Produto cadastrado com sucesso!")
        return redirect("produtos:list")
    context = {"form": form, "titulo": "Cadastrar Produto"}
    return render(request, "produtos/form.html", context)


@login_required
def editar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Produto atualizado com sucesso!")
        return redirect("produtos:list")
    context = {"form": form, "titulo": "Editar Produto", "produto": produto}
    return render(request, "produtos/form.html", context)


@login_required
def excluir(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        messages.success(request, "Produto excluído com sucesso!")
        return redirect("produtos:list")
    context = {"produto": produto}
    return render(request, "produtos/confirm_delete.html", context)
