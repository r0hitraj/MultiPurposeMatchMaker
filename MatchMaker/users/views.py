from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm      # imported to use the django's forms
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required   # if we want only login users to access some page
# this is a python decorator


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()         # this saves the user in database
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()       # we have to pass POST request here, for submission of data in database
    return render(request, 'users/register.html', {
        'form': form
    })


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,
                                instance=request.user)
        # passing instance so that form would be filled with current info(which would be updated)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        # passing instance so that form would be filled with current info(which would be updated),
        # request.FILES in case of image(coz there are some files)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        # passing instance so that form would be filled with current info(which would be updated)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        # passing instance so that form would be filled with current info(which would be updated)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context=context)
