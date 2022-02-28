from pyexpat import model
from django import forms
from HotelLP.models import Cliente, Contacto, Reserva

class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields='__all__'

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'