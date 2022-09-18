from django import forms
from .models import Run
from django.forms import ModelForm

# class AddRunForm(forms.Form):
#     course = forms.CharField(label='course', max_length=100)
#     distance = forms.IntegerField(label='distance', max_value=500)
#     duration = forms.IntegerField(label='duration', max_value=10080)
#     rating = forms.IntegerField(label='rating', max_value=10)
#     review = forms.CharField(label='Please write your review here',
#                              widget=forms.Textarea(attrs={'class':'myform'}))

class AddRunForm(ModelForm):
    class Meta:
        model = Run
        fields = "__all__"