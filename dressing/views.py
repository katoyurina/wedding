from select import select
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SelectForm
from .models import Select

def party(request):
    return render(request, 'dressing/party.html')

def index(request):
    params = {
        'myform': SelectForm(),   
    }

    if (request.method == 'POST'):
        params['myform'] = SelectForm(request.POST)
               
        if params['myform'].is_valid():
            select = params['myform'].save(commit=False)
            select.save()

            return redirect("dressing:index1")
        
        else:
            return HttpResponse("The form has mistake!")

    # return render(request, "int/index.html", {"form": form})


    return render(request, 'dressing/index.html', params)

def index1(request):
    return render(request, 'dressing/index1.html')