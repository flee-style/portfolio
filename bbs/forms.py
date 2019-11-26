from django import forms
from .models import Article

class SearchForm(forms.Form):
    searchtext = forms.CharField(label='検索',max_length=500)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content' : forms.Textarea(),
        }
