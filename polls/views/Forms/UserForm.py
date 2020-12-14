from django import forms
from polls.models import User

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(UserForm, self).__init__(*args, **kwd)
        self.fields["userID"].required = True
        self.fields["name"].required = True
        self.fields["pw"].required = True

    userID = forms.CharField(max_length=15 , min_length=4)
    name = forms.CharField(max_length=50 , min_length=1)
    pw = forms.CharField(max_length=50 , min_length=6 , widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('userID', 'name', 'pw')
