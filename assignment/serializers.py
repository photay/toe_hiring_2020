from rest_framework import serializers
from .models import DogQuestion

class DogQuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta(object):
		model = DogQuestion
		fields = ('daily_walk','dog_breed', 'dog_age', 'dog_tricks', 'email')