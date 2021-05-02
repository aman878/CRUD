from .models import Laptop
from django import forms  

brands = [
    ('MSI', 'MSI'),
    ('Dell', 'Dell'),
    ('Lenovo', 'Lenovo'),
    ('Gigabyte', 'Gigabyte'),
    ('Others', 'Others')]
stock = [('Yes', 'Yes'), ('No','No')]
processors = [('i3', 'Intel i3'), ('i5', 'Intel i5'), ('i7', 'Intel i7'), ('i9', 'Intel i9'), ('Ryz', 'AMD Ryzen')]
class laptopForm(forms.ModelForm):  
    class Meta:  
        model = Laptop  
        fields = "__all__"  
        widgets = {'picture' : forms.FileInput(attrs={'required':True}), 
        'lbrand' : forms.Select(choices=brands, attrs={'required':True}),
        'lproc' : forms.RadioSelect(choices=processors, attrs={'required':True}),
        'lstock': forms.RadioSelect(choices=stock,attrs={'required':True})}
