from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField(help_text="help me")
    email=forms.EmailField()
    first_name=forms.CharField()








    