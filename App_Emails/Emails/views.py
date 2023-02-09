from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
# Create your views here.
def home (request):
    return render (request, 'home.html')
def contact (request):
    if request.method == 'POST':
        email_destiny = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('email_template.html', {
            'message': message,
            'email': email_destiny
        })
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            [email_destiny]
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Se ha enviado tu correo.')
        return redirect ('home')