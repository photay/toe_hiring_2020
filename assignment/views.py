from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .serializers import DogQuestionSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import *
from django.views import View
from assignment.models import *
from assignment.forms import *

# Rest Api class
class DogQuestionViewSet(viewsets.ModelViewSet):
    """docstring for DogQuestionViewSet"""
    queryset = DogQuestion.objects.all()
    serializer_class = DogQuestionSerializer


class Index(FormView):
    template_name = "index.html"

    #TODO: Changes this to your new form
    form_class= DogForm
    success_url= '/success/'

    def get_context_data(self,**kwargs):
        form = self.form_class(initial=self.initial)
        context = super(Index,self).get_context_data(**kwargs)
        return context


    def post(self, request, *args, **kargs):
        print("posted")
        form = self.get_form()

        #TODO: Process form data here by saving to DB and sending Email

        if form.is_valid():
            obj = DogQuestion.objects.create(**form.cleaned_data)
            latest_dog = DogQuestion.objects.last()

            # send_email
            subject = 'Your dog information'
            message = f'''These are your answers to the questions we provided:
            Do you walk your dog daily? {latest_dog.daily_walk}
            What is the breed of your dog? {latest_dog.dog_breed}
            How old is your dog? {latest_dog.dog_age} 
            What tricks does your dog know? Select all that apply:
            {latest_dog.dog_tricks} 
            '''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [latest_dog.email]
            send_mail(subject, message, email_from, recipient_list, fail_silently =False)

            return HttpResponseRedirect(self.get_success_url())


class Success(TemplateView):
    template_name='success.html'
