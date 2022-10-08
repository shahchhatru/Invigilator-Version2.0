from django.shortcuts import render,redirect
from django.views import View
from .models import Invigilator
from .form import AddInvigilatorForm
# Create your views here.


class Home(View):
    def get(self,request):
        data=Invigilator.objects.all()
        for i in data:
            print(i)
       
        return render(request,'core/home.html',{'data':data})

class AddInvigilator(View):
    def get(self,request):
        fm=AddInvigilatorForm()
        return render(request,'core/addInvigilator.html',{'form':fm})

    def post(self,request):
        fm=AddInvigilatorForm()
        print(fm)
        print(fm.is_valid())
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core/addInvigilator.html',{'form':fm})

    