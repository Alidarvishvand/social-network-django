from django.shortcuts import render,redirect
from django.views import View
from . forms import UserRegisteForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Post
from django.contrib import messages
class RegisterView(View):
        form_classes = UserRegisteForm
        template_name = 'account/register.html'


        def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                  return redirect('home:home')
            return super().dispatch(request,*args, **kwargs)
        
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


      def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                   return redirect('home:home')
            return super().dispatch(request,*args,**kwargs)



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
      

class UserLogOutView(LoginRequiredMixin,View):
      login_url =  '/account/login/'
      def get (self, request):
            logout(request)
            messages.success(request,"you are log out")
            return redirect('home:home')
      


class UserProfileView(LoginRequiredMixin,View):
      def get (self, request,user_id):
            user = User.objects.get(pk=user_id)
            posts = Post.objects.filter(user=user)
            return render(request,'account/profile.html',{'user':user, 'posts':posts})
      