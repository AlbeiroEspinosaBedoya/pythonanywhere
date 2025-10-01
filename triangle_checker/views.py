from django.shortcuts import render
from .forms import TriangleForm

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def check_triangle(request):
    result = None
    if request.method == 'POST':
        form = TriangleForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['side_a']
            b = form.cleaned_data['side_b']
            c = form.cleaned_data['side_c']
            if is_triangle(a, b, c):
                result = "Las longitudes dadas forman un triangulo."
            else:
                result = "Error: Las longitudes dadas NO forman un triangulo."
    else:
        form = TriangleForm()
    return render(request, 'triangle_checker/check_triangle.html', {'form': form, 'result': result})
