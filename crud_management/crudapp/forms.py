# from django import forms
# from django.core.exceptions import ValidationError
#
# class StudentForm(forms.Form):
#
#     name = forms.CharField()
#     email = forms.EmailField()
#     age = forms.IntegerField()
#     gender = forms.CharField()
#
#
# def clean_name(self):
#     name = self.cleaned_data.get('name')
#     if name and not name.isupper():
#         raise ValidationError('Name must be in uppercase.')
#     return name