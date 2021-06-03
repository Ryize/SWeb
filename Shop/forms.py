from django import forms

from News.forms import CustomCaptchaTextInput
from .models import Product, Category_Product
from captcha.fields import CaptchaField, CaptchaTextInput


class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'custom_field.html'

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(empty_label=None, queryset=Category_Product.objects.all())
    captcha = CaptchaField(label='Подтвердите, что вы не робот:', widget=CustomCaptchaTextInput)

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'features': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'warranty': forms.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer_company': forms.TextInput(attrs={'class': 'form-control'}),
            'seller_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'seller': forms.HiddenInput(),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
