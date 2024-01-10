from django import forms

class AlfajoresFormulario(forms.Form):

    #Especificar los campos
    alfajor = forms.CharField()
    codigo_alfajor = forms.IntegerField()


class ClientesFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono= forms.IntegerField()