from django.shortcuts import render,redirect
from . forms import  UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been created successfully.You are now able to login')
			return redirect('login')
	else:
		form=UserRegisterForm()
	return render(request,'users/register.html',{'form':form})
	
@login_required	

def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
      
      'u_form': u_form,
      'p_form':p_form

    }
    return render(request,'users/profile.html', context)
	


