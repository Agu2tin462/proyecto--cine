from django import forms
from .models import Contacto

<<<<<<< HEAD

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            }
=======
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']
>>>>>>> 25bdb4c8a5ee3bbd8c2ce3b1657651e1be84f04e
