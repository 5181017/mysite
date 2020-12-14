from django import forms
from polls.models import User

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(ReviewForm, self).__init__(*args, **kwd)
        self.fields["reviewStar"].required = True
        self.fields["title"].required = True
        self.fields["comment"].required = True
    reviewStar = forms.IntegerField()
    title = forms.CharField(max_length=50)
    comment = forms.CharField(max_length=150 , min_length=10)

    class Meta:
        model = User
        fields = ('reviewStar', 'title', 'comment')
