from django.shortcuts import render
from django.views import View
from . forms import UserRegisteForm

class RegisterView(View):
        def get(self, request):
            form = UserRegisteForm()
            return render(request,'account/register.html',{'form':form})
    
        def post(self, request):
            # return render(request,'account/register.html',{'form':form})
              pass