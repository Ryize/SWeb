from django import forms
from .models import News
from captcha.fields import CaptchaField, CaptchaTextInput


class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'custom_field.html'


class NewsForm(forms.ModelForm):
    captcha = CaptchaField(label='Подтвердите, что вы не робот:', widget=CustomCaptchaTextInput)

    class Meta:
        model = News
        fields = ['title', 'content', 'is_publiced', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
