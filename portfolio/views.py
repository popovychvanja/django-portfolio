from django.conf import settings
from django.shortcuts import render, redirect
from .models import Service, PortfolioItem, ContactMessage
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm

def home(request):
    services = Service.objects.all()
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'portfolio/home.html', {
        'services': services,
        'portfolio_items': portfolio_items,
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.sent = True
            contact.save()

            # ----- Send email -----
            subject = f"New contact from {contact.name}"
            html_message = render_to_string('portfolio/email_contact.html', {'contact': contact})
            plain_message = strip_tags(html_message)

            send_mail(
                subject,
                plain_message,
                contact.email,
                [settings.DEFAULT_FROM_EMAIL],
                html_message=html_message,
                fail_silently=False,
            )

            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})
