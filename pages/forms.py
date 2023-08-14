from django import forms
from .models import Clothes, Electronics, Furnutures, Sports, Households

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes 
        fields = '__all__'


class ElectronicsForm(forms.ModelForm):
    class Meta:
        model = Electronics
        fields = '__all__'
        
class FurnuturesForm(forms.ModelForm):
    class Meta:
        model = Furnutures
        fields = '__all__'
        
class SportsForm(forms.ModelForm):
    class Meta:
        model = Sports
        fields = '__all__'
        
class HouseholdsForm(forms.ModelForm):
    class Meta:
        model = Households
        fields = '__all__'
        
  