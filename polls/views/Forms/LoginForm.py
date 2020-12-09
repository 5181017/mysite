from django import forms
from polls.models import User


class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(LoginForm, self).__init__(*args, **kwd)
        self.fields["userID"].required = True
        self.fields["pw"].required = True

    userID = forms.CharField(max_length=15, min_length=4)
    pw = forms.CharField(max_length=50, min_length=6, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('userID', 'pw')