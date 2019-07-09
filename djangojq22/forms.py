from django import forms
from .models import  *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name","picture"]

class CategoryFormM1(CategoryForm):
    class Meta:
        model = Category
        fields = ["name","likes","picture"]
        widgets = {'likes': forms.NumberInput(attrs={'class': 'slider'})}
    def __init__(self, *args, **kwargs):
        super(CategoryFormM1, self).__init__(*args, **kwargs)
        #self.fields['likes'].widget = forms.HiddenInput()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name","dob","home_group"]
        widgets = {'dob': forms.DateInput(attrs={'class': 'datepicker'}, format='%Y/%m/%d')}

