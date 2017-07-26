from django.views.generic import (
    FormView,
)

from django.core.urlresolvers import reverse_lazy
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('core:index')
    form_class = ContactForm

    def form_valid(self, form):
        print('Form valid')
        return super(ContactView, self).form_valid(form)
