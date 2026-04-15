from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(
            attrs={
                "class": (
                    "w-full px-4 py-3 rounded-xl border border-gray-300 "
                    "focus:outline-none focus:ring-2 focus:ring-indigo-500 "
                    "focus:border-transparent transition text-gray-900 "
                    "placeholder-gray-400 bg-white text-sm"
                ),
                "placeholder": "Seu usuário",
                "autofocus": True,
            }
        ),
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": (
                    "w-full px-4 py-3 rounded-xl border border-gray-300 "
                    "focus:outline-none focus:ring-2 focus:ring-indigo-500 "
                    "focus:border-transparent transition text-gray-900 "
                    "placeholder-gray-400 bg-white text-sm"
                ),
                "placeholder": "Sua senha",
            }
        ),
    )
