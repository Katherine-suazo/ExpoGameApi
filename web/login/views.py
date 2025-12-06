from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from login.forms import ContactForm



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            EmailMessage(
                'Suscripcion de contacto para {}'.format(name),
                message,
                'form-response@example.com', # Send from (your website)
                ['katherine.suazo05@inacapmail.cl', email], # Send to (your admin email)
                [],
                reply_to=[email] # Email from the form to get back to
            ).send()

            messages.info(request, 'Enviado')
            return redirect('/contacto/contact')

    else:
        form = ContactForm()
        return render(request, 'login/contacto.html', {'form': form})



def success(request):
  return HttpResponse('Enviado!')