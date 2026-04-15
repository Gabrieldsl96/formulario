from django import forms

from .models import Produto

INPUT_CLASS = (
    "w-full px-4 py-3 rounded-xl border border-gray-300 "
    "focus:outline-none focus:ring-2 focus:ring-indigo-500 "
    "focus:border-transparent transition text-gray-900 "
    "placeholder-gray-400 bg-white text-sm"
)


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco", "quantidade"]
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "Nome do produto",
                }
            ),
            "descricao": forms.Textarea(
                attrs={
                    "class": INPUT_CLASS + " resize-none",
                    "placeholder": "Descrição do produto (opcional)",
                    "rows": 3,
                }
            ),
            "preco": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "0,00",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "quantidade": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "0",
                    "min": "0",
                }
            ),
        }
        labels = {
            "nome": "Nome",
            "descricao": "Descrição",
            "preco": "Preço (R$)",
            "quantidade": "Quantidade em estoque",
        }
