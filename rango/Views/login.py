from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)
        import ipdb
        ipdb.set_trace()
        if user :
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('rango:index')

            else:
                return HttpResponse("Your Rango Account is Disabled")

        else:
            print("Invalid login details: {0}, {1}".format(username,password))
            return HttpResponse("Invalid Login Details Supplied")
    else:
        return render(request,'login.html',{})
