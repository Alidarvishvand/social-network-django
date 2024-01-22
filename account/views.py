from django.shortcuts import render,redirect
from django.views import View
from . forms import UserRegisteForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from django.contrib import messages
class RegisterView(View):
        form_classes = UserRegisteForm
        template_name = 'account/register.html'
        def get(self, request):
            form = UserRegisteForm()
            return render(request, self.template_name ,{'form':form})
    
        def post(self, request):
            # return render(request,'account/register.html',{'form':form})
              form = UserRegisteForm(request.POST)
              if form.is_valid():
                    cd= form.cleaned_data
                    User.objects.create_user(cd['username'],cd['email'],cd['password'])
                    messages.success(request,'you register successfully','success')
                    return redirect('home:home')
              return render(request, self.template_name ,{'form':form})


class UserLoginView(View):
      form_classes = UserLoginForm
      template_name = 'account/login.html'
      def get(self, request):
            form  = self.form_classes
            return render(request , self.template_name , {'form':form}) 
      
      def post(self,request):
            form = self.form_classes(request.POST)
            if form.is_valid():
                  cd=form.cleaned_data
                  user = authenticate(request, username=cd['username'], password=cd['password'])
                  if user is not None:
                        login(request,user)
                        messages.success(request,'you are login successfully','success')
                        return redirect('home:home')
                  messages.error(request,'you not login','danger')

            return render(request,self.template_name,{'form':form})
                  