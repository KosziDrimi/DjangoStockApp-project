from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Price
from .forms import PriceForm


@login_required 
def show(request):

    if request.method == 'POST':
        form = PriceForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['nazwa_spółki']
            start_date = form.cleaned_data['data_początkowa']
            end_date = form.cleaned_data['data_końcowa']
          
            prices = Price.objects.filter(Data__range = [start_date, end_date], 
                                          Nazwa_spółki__iexact = name)
       
            context = {'prices' : prices, 'name' : name}
            return render(request, 'app_2/result.html', context)

    else:
        form = PriceForm()

    context = {'form' : form}
    return render(request, 'app_2/form.html', context)


