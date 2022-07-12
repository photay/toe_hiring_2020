from django import forms

class DemoForm(forms.Form):
    demo_field = forms.CharField(max_length=2500,required=True)

# TODO: Put your dog questions form here
TRICKS = (('item_key1', 'Sit'),
              ('item_key2', 'Fetch'),
              ('item_key3', 'Stay'),
              ('item_key4', 'Roll Over'))

class DogForm(forms.Form):
	daily_walk = forms.BooleanField(required=False, label="Do you walk your dog daily? ")
	dog_breed = forms.CharField(required=True, label="What breed is your dog? ")
	dog_age = forms.IntegerField(required=True, label="How old is your dog? ", max_value=30, 
		min_value=0)
	dog_tricks = forms.MultipleChoiceField(label="What tricks does your dog know? Select all that apply: ", 
		choices=TRICKS)
	email = forms.CharField(required=True, label="Email Address: ")
