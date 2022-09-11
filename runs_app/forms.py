from django import forms

class AddRunForm(forms.Form):
    course = forms.CharField(label='course', max_length=100)
    distance = forms.IntegerField(label='distance', max_value=500)
    duration = forms.IntegerField(label='duration', max_value=10080)
    rating = forms.IntegerField(label='rating', max_value=10)
    review = forms.CharField(label='review', max_length=5000)
