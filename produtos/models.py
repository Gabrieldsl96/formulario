from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    descricao = models.TextField(blank=True, verbose_name="Descrição")
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço (R$)"
    )
    quantidade = models.PositiveIntegerField(
        default=0, verbose_name="Quantidade em estoque"
    )
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["-criado_em"]

    def __str__(self):
        return self.nome
