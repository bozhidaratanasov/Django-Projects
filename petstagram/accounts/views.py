from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from accounts.forms import UserProfileForm, SignUpForm
from django.contrib.auth import login, logout
from accounts.models import UserProfile

def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'pets': user.userprofile.pet_set.all(),
            'form': UserProfileForm(),
            'owns_profile': request.user == user or pk == None,
        }
        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')




def signup_user(request):
    if request.method == "GET":
        context = {
            'form': SignUpForm(),

        }
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()

            login(request, user)
            return redirect('list pets')

        context = {
            'form': form
        }

        return render(request, 'accounts/signup.html', context)

def signout_user(request):
    logout(request)
    return redirect('index')
