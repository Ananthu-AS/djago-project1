from django.shortcuts import render
from .models import employee
from employee.forms import employeeForm
# Create your views here.
def index(request):
    data=employee.objects.all()
    EmpForm=employeeForm()
    if request.method=='POST':
        EmpForm=employeeForm(request.POST)
        if EmpForm.is_valid():
            EmpForm.save()
    return render(request, "index.html",{'data':data,'EmpForm':EmpForm})