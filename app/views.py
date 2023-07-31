from django.shortcuts import render

# Create your views here.

def loop(request):
    d={'name':'PRITAM', 'age':23}
    return render(request, 'loop.html', context=d)