from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout
from django.http import HttpResponse



def register_page(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request, 'Email is already exist')
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create( email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()
        return render(request ,'alert/signup-alert.html')

    
    return render(request ,'accounts/register.html')









def login_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request, 'Email account not found')
            return render(request ,'alert/login-alert.html')




        user_obj = authenticate(username = email , password = password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')
            
        return HttpResponseRedirect(request.path_info)
    return render(request ,'accounts/login.html')



def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return render(request,'alert/logout.html')
