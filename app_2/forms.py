from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'
    
    
class PriceForm(forms.Form):
    nazwa_spółki = forms.ChoiceField(choices=[('kgh', 'KGH'), ('pkn', 'PKN'), 
                                              ('sen', 'SEN')])
    data_początkowa = forms.DateField(widget = DateInput())
    data_końcowa = forms.DateField(widget = DateInput())
