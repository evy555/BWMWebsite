from django import forms
from django.core.mail import send_mail, BadHeaderError

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    state = forms.ChoiceField([('NV','NV'),('CA','CA'),('WY','WY')])
    zip_code = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        details = self.cleaned_data
        subjectInfo = 'Information Request - BWM Website'
        full_nameInfo = details['full_name']
        emailInfo = details['email']
        stateInfo = details['state']
        zip_codeInfo = details['zip_code']
        phoneInfo = details['phone']
        messageInfo = details['message']

        emailWithInfo = full_nameInfo + '\n\n' + emailInfo + '\n' + stateInfo + '\n' + zip_codeInfo + '\n' + phoneInfo + '\n\n' + messageInfo

        send_mail(subjectInfo,emailWithInfo,emailInfo, ['josh.evans@bowerswealth.com'], fail_silently=False)
