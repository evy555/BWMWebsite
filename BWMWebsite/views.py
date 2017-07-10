from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError

from . import forms

class HomePage(TemplateView):
    template_name = 'index.html'


class ConfidentialReview(TemplateView):
    template_name = 'contactus/CIR.html'

class ContactUs(FormView):
    template_name ='contactus/contactusForm.html'
    form_class = forms.ContactForm
    success_url = '/thankyou'

    def form_valid(self, form):
        form.send_email()
        return super(ContactUs, self).form_valid(form)

class ThankYou(TemplateView):
    template_name = 'contactus/thankyou.html'

class PrivacyPolicy(TemplateView):
    template_name = 'legal/privacypolicy.html'
