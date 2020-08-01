from django import forms #pack de django para conectar el form
from .models import Pruebabase
class PruebaForm(forms.ModelForm):
   
    class Meta:       
        model = Pruebabase
        fields = [
            'titulo',
            'subtitulo',
            'cantidad',
        ]

        widgets = {
            'titulo': forms.TextInput(
                attrs={#atrivutos
                    'placeholder': 'ingrese el texto'
                }
            )
        }





    #validaciones -----------------asi
    def clean_cantidad(self):#para modificar un campo
        cantidad = self.cleaned_data['cantidad']#recuperar el valor
        if cantidad < 10:
            raise forms.ValidationError('ingrese un num mayor a 10')
        return cantidad


