from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            comments = request.POST.get('comments', '')

            # Creamos el correo
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, comments),
                "no-contestar@inbox.mailtrap.io",
                ["octaviosoto777@gmail.com"],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
            # return render(request, 'contact/contact.html', {'form': form})

    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})