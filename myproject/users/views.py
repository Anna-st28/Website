from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, PhotographerProfileForm
from .models import PhotographerProfile


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = PhotographerProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = PhotographerProfileForm()
    return render(request, 'users/register.html',
                  {'user_form': user_form, 'profile_form': profile_form})


def specialists(request):
    photographers = PhotographerProfile.objects.all()
    return render(request, 'specialists.html', {'photographers': photographers})


def news():
    return None


def gallery():
    return None
