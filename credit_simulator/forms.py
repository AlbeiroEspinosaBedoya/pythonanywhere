from django import forms

class CreditForm(forms.Form):
    amount = forms.FloatField(label="Monto del crédito", min_value=0, required=True)
    rate = forms.FloatField(label="Tasa de interés anual (%)", min_value=0, required=True)
    term = forms.IntegerField(label="Plazo (meses)", min_value=1, required=True)
