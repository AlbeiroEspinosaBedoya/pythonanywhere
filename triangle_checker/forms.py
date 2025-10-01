from django import forms

class TriangleForm(forms.Form):
    side_a = forms.FloatField(label='Lado A')
    side_b = forms.FloatField(label='Lado B')
    side_c = forms.FloatField(label='Lado C')