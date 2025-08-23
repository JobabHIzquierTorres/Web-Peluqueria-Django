from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
        required=True,
        min_length=3,
        max_length=100,
        error_messages={
            'required': 'Por favor, introduce tu nombre.',
            'min_length': 'El nombre debe tener mínimo 3 letras.',
            'max_length': 'El nombre debe tener máximo 100 letras',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-transparent',
            'id': 'name',
            'placeholder': 'Nombre',
        })
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        min_length=3,
        max_length=20,
        error_messages={
            'required': 'Por favor, introduce tu email',
            'invalid': 'Introduce un correo electrónico válido',
            'min_length': 'Mínimo 3 caracteres',
            'max_length': 'Máxinmo 100 caracteres'
        },
        widget=forms
        .TextInput(attrs={
            'class': 'form-control bg-transparent',
            'id': 'email',
            'placeholder': 'Introduce tu correo electrónico',
        })
    )

    subject = forms.CharField(
        label='Asunto',
        required=True,
        min_length=3,
        max_length=100,
        error_messages={
            'required': 'Introduzca un asunto.',
            'min_length': 'Mínimo 3 letras.',
            'max_length': 'Máximo 20 letras.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-transparent',
            'id': 'subject',
            'placeholder': 'Introduce un asunto.'
        })
    )

    content = forms.CharField(
        label='Mensaje',
        required=True,
        min_length=10,
        max_length=1000,
        error_messages={
            'required': 'Introduzca su mensaje.',
            'min_length': 'El mensaje debe tener mínimo 10 caracteres',
            'max_length': 'El mensaje debe tener máximo 1000 caracteres',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-transparent',
            'id': 'message',
            'placeholder': 'Introduzca un mensaje...',
        })
    )
