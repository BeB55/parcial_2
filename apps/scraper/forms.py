from django import forms

class ScraperForm(forms.Form):
    palabra = forms.CharField(
        label="Palabra clave",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ej: Python, Django, algoritmos"
        })
    )
    enviar_correo = forms.BooleanField(
        label="Enviar resultados por correo",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
