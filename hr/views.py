from django.shortcuts import redirect, render

# from employee.forms import employeeForm
from employee.models import employee

# Create your views here.
def index(request):
    data=employee.objects.all()
    return render(request, "hr.html",{'data':data})

def approve(request,id):
    st=employee.objects.get(id=id)
    st.Status=1
    st.save()
    return redirect('hr')

def reject(request,id):
    st=employee.objects.get(id=id)
    st.Status=2
    st.save()
    return redirect('hr')