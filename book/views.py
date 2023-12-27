from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from book.models import Books

from book.forms import BookForms,RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout

from django.utils.decorators import method_decorator



#decorator
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"....login in required.....")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

#list all books
@method_decorator(signin_required,name="dispatch")

class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        return render(request,"booklist_view.html",{"data":qs})

#http://127.0.0.1:8000/books/id
@method_decorator(signin_required,name="dispatch")

class GetidView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render(request,"bookid.html",{"data":qs})
    
#http://127.0.0.1:8000/books/id/remove
@method_decorator(signin_required,name="dispatch")

class DeleteView(View):
    def get(self,request,*args,**kwargs): 
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id).delete()
        return redirect("booklist-all")
    
#http://127.0.0.1:8000/books/create
@method_decorator(signin_required,name="dispatch")

class CreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookForms()
        return render(request,"book-create.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookForms(request.POST,files=request.FILES)#files=req.files for disply img option
        if form.is_valid():
            form.save()
            messages.success(request," data created successfully....")
            return redirect("booklist-all")
        else:
            messages.ERROR(request," data creation failed ...")
            return render(request,"book-create.html",{"form":form})

#http://127.0.0.1:8000/books/id/update
@method_decorator(signin_required,name="dispatch")

class UpdateView(View):
    def get(self,request,*args,**kwargs):
        form=BookForms()
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookForms(instance=obj)
        return render(request,"book-update.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookForms(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request," data updated successfully....")
            return redirect("booklist-all")
        else:
            messages.error(request," data updation failed....")
            return render(request,"book-update.html",{"form":form})
        
#registrationform signup view

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()  #import regform along with bookform in view.py
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"registraion form created successfully...........")
            return render(request,"register.html",{"form":form})
        else:
            messages.error(request,"registraion form failed to create ...........")
            return render(request,"register.html",{"form":form})
    
#LOGIN VIEW
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
             uname=form.cleaned_data.get("username")
             paswd=form.cleaned_data.get("password")
             print("......",uname,paswd)
             user_object=authenticate(request,username=uname,password=paswd)
             if user_object:
                print("valid credentials")
                #start session
                login(request,user_object)
                print(request.user)  #fetch user details
                return redirect("booklist-all") 
             else:
                print("invalid credentials")
             return render(request,"login.html",{"form":form})
        else:
            return render(request,"login.html",{"form":form})


#signout
@method_decorator(signin_required,name="dispatch")

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")



            
        

