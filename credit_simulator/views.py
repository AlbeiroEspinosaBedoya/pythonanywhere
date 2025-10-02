from django.shortcuts import render
from .forms import CreditForm

def credit_simulator(request):
    result = None
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            rate = form.cleaned_data['rate'] / 100 / 12  # mensual
            term = form.cleaned_data['term']
            if rate > 0:
                cuota = amount * (rate * (1 + rate) ** term) / ((1 + rate) ** term - 1)
            else:
                cuota = amount / term
            total = cuota * term
            intereses = total - amount
            result = {
                'cuota': round(cuota, 2),
                'total': round(total, 2),
                'intereses': round(intereses, 2),
            }
    else:
        form = CreditForm()
    return render(request, 'credit_simulator/credit_simulator.html', {'form': form, 'result': result})