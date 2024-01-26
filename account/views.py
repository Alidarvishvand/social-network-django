from typing import Any
from django.http import HttpRequest
from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.views import View
from . forms import UserRegisteForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Post
from django.contrib import messages
from.models import Relation
from django.contrib.auth import views as auth_views

from django.urls import reverse_lazy







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



      def setup(self, request: HttpRequest, *args, **kwargs) :
            self.next  = request.GET.get('next', None)
            return super().setup(request,*args,**kwargs)
      



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
                        if self.next :
                              return redirect(self.next)
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
            is_followin = False
            user= get_object_or_404(User,pk=user_id)
            posts =user.posts.all()
            relation = Relation.objects.filter(from_user = request.user,to_user = user)
            if relation.exists():
                  is_followin  = True
            return render(request,'account/profile.html',{'user':user, 'posts':posts, 'is_following':is_followin})



class UserPasswordResetView(auth_views.PasswordResetView):
	template_name = 'account/password_reset_form.html'
	success_url = reverse_lazy('account:password_reset_done')
	email_template_name = 'account/password_reset_email.html'


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
	template_name = 'account/password_reset_done.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
	template_name = 'account/password_reset_confirm.html'
	success_url = reverse_lazy('account:password_reset_complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
	template_name = 'account/password_reset_complete.html'



class UserFollowView(LoginRequiredMixin,View):
      def get(self,request,user_id):
            user = User.objects.get(id=user_id)
            relation = Relation.objects.filter(from_user=request.user, to_user=user)
            if relation.exists():
                  messages.error(request,'you are already following','danger')
            else :
                  Relation.objects.create(from_user = request.user , to_user = user)
                  messages.success(request,'you follow user','success')

            return redirect('account:profile',user.id)



class UserUnfollowView(LoginRequiredMixin,View):
      def get(self,request,user_id):
            user = User.objects.get(id = user_id )
            relation = Relation.objects.filter(from_user=request.user,to_user =user)
            if relation.exists():
                  relation.delete()
                  messages.success(request, 'you are unfollow user ','success')
            else:
                  messages.error(request,'you are not following this user','danger')
            return redirect('account:profile',user.id)
