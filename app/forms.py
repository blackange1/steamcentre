from django import forms


class LoginForm(forms.Form):
    username = \
        forms.CharField(
            min_length=2,
            max_length=50,
        )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'uk-input'}),
    )
