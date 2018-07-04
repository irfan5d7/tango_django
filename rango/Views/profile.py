from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from rango.Forms import UserProfileForm
from rango.models import UserProfile


@login_required
def profile(request,username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return redirect('rango:index')

    userprofile = UserProfile.objects.get_or_create(user = user)[0]
    form = UserProfileForm({'websie':userprofile.website,'picture':userprofile.picture})

    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES,isinstance = userprofile)
        if form.is_valid():
            form.save(commit = True)
            return redirect('profile',user.username)
        else:
            print(form.error)
    return render(request, 'profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})