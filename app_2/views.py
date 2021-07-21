from django.shortcuts import render, redirect

from .models import Price
from .forms import PriceForm


def show(request):
    
    if request.method == 'POST':
        form = PriceForm(request.POST)

        if form.is_valid():
            
            temp = request.POST['nazwa_spółki']
            start_date = request.POST['data_początkowa']
            end_date = request.POST['data_końcowa']
            
            if temp == 'kgh':
                prices = Price.objects.using('new').filter(Data__range = 
                        [start_date, end_date]).values('Data', 'Cena_KGH')   
                               
            elif temp == 'pkn':
                prices = Price.objects.using('new').filter(Data__range = 
                        [start_date, end_date]).values('Data', 'Cena_PKN')
                                
            else:
                prices = Price.objects.using('new').filter(Data__range = 
                        [start_date, end_date]).values('Data', 'Cena_SEN')
            
            context = {'prices' : prices, 'temp' : temp}
            return render(request, 'app_2/result.html', context)

    else:
        form = PriceForm()

    context = {'form' : form}
    return render(request, 'app_2/form.html', context)


