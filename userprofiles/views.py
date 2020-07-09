from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

# Create your views here.
@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
            return redirect('userprofiles:profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
    'p_form':p_form,
    "account_page":"active"
    }
    return render(request, 'users/profile.html', context)
