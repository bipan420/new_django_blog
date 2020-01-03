from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Account created for {username}!')
    #         return redirect('blog-home')
    # else:
    #     form = UserCreationForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Congratulations {username} !!, Your account has been created. You can login now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'forma':form})

@login_required
def profile(request):
    if request.method == 'POST':
        #here the instance is used to display the current user's information in the form field
        #also in the profile we are also gonna get the files data
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'users/profile.html',context)
