from django import forms

class Contactform(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':6}))    

class Quoteform(forms.Form):
    departure = forms.CharField(max_length=200)
    delivery = forms.CharField(max_length=200)
    weight = forms.IntegerField()
    dimensions = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':6}))
        
        