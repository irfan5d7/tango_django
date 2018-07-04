from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from rango.Forms import UserProfileForm


@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('rango:index')
        else:
            print(form.errors)

    context_dict = {'form': form}

    return render(request, 'profile_registration.html', context_dict)