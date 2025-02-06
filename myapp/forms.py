from myapp.models import Product

from django import forms

class Product_form(forms.ModelForm):

    class Meta:

        model=Product

        fields= "__all__"