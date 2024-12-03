from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact  # Import the Contact model


# Create your views here.

def index (request):
    return render (request, 'home.html')

def about (request):
    return render (request, 'about.html')

def service (request):
    return render (request, 'service.html')

def employment (request):
    return render (request, 'employment.html')



# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')

#         if not name or not email or not message:
#             return HttpResponse('Please fill out all required fields.', status=400)

#     # Email content
#         email_subject = f'Contact Form Submission from {name}'
#         email_body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}'

#         try:
          
#             send_mail(
#                 email_subject,
#                 email_body,
#                 settings.DEFAULT_FROM_EMAIL, 
#                 fail_silently=False,
#             )
#             return redirect('success')  

#         except Exception as e:
#             return HttpResponse(f'An error occurred while sending the email: {e}', status=500)

#     return render(request, 'contact.html')



# views.py


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')  # Optional field
        message = request.POST.get('message')

        if not name or not email or not message:
            return HttpResponse('Please fill out all required fields.', status=400)

        # Save the data in the Contact model
        contact_entry = Contact(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )
        contact_entry.save()

        # Send an email
        email_subject = f'Contact Form Submission from {name}'
        email_body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}'

        try:
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],  # Send to your domain email
                fail_silently=False,
            )
            return redirect('success')  # Redirect to success page
        except Exception as e:
            return HttpResponse(f'An error occurred while sending the email: {e}', status=500)

    return render(request, 'contact.html')



def success(request):
    return render(request, 'success.html')