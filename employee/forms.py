from django import forms
from employee.models import employee

class employeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields=['Name','Start_date','End_date','Reason']
        # widgets={'Start_date': forms.Input(type='date')}
        
