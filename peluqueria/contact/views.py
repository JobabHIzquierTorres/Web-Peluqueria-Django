from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .form import ContactForm
from django.core.mail import EmailMessage
import logging
logger = logging.getLogger(__name__)

# Create your views here.


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        content = form.cleaned_data['content']

        email_message = EmailMessage(
            subject=subject,
            body=f'De {name} <{email}>\n\nEscribió:\n\n{content}',
            from_email='no-contestar@inbox.mailtrap.io',
            to=['hola@pficticia.net'],
            reply_to=[email]
        )

        try:
            email_message.send()
            return redirect(self.success_url + '?ok')
        except Exception as e:
            logger.error(f"Error al enviar el correo: {e}")
            return redirect(self.success_url + '?fail')
