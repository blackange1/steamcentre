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


# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

class NewUserForm(forms.Form):
    email = \
        forms.EmailField(required=True)
    username = \
        forms.CharField(
            min_length=2,
            max_length=50,
        )
    pw1 = \
        forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'uk-input'}),
            min_length=8,
        )
    pw2 = \
        forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'uk-input'}),
            min_length=8,
        )
