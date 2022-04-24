from django.shortcuts import render
from django.http import HttpResponse
from .forms import detailsForm
from .models import token

# Create your views here.
def temp(request):
    return HttpResponse("I am a developer")

def details_form(request):
    form = detailsForm()
    if request.method == 'POST':
         form = detailsForm(request.POST, request.FILES)
         if form.is_valid():
            c_name = request.POST["name"]
            form.save()
            t_obj=token.objects.get(name=c_name)
            
            return render(request, 'gettoken/success.html', {'t_obj' : t_obj,})
    context = {"form": form,}
    return render(request, 'gettoken/details.html', context)
        