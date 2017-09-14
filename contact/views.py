from django.views.generic import (
    FormView,
)

from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMultiAlternatives

from django.conf import settings

from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('core:index')
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        mail = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=email,
            to=[settings.RECIPIENT_EMAIL],
        )
        mail.send()
        return super(ContactView, self).form_valid(form)
