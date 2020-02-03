from django import forms

class DemoForm(forms.Form):
    demo_field = forms.CharField(max_length=2500,required=True)

# TODO: Put your dog questions form here
