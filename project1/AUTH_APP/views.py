from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login ,logout

# Create your views here.
def registerView(request):
    form = UserCreationForm()
    template_name = 'AUTH_APP/registration.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('log_url')
    context = {'form': form}
    return render(request,template_name,context)

def loginView(request):
    template_name = 'AUTH_APP/loginform.html'

    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        print(f'{u}---{p}')
        user = authenticate(username = u, password = p)
        print(f'{user}')
        if user is not  None:
            login(request, user)
            return redirect('show_url')
    context = {}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('log_url')