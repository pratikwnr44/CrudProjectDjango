from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrdeerForm
from .models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@login_required(login_url='log_url')
def OrderView(request):
    form = OrdeerForm()
    template_name = 'crud_app/add.html'
    if request.method == 'POST':
        form = OrdeerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='log_url')
def ShowOrder(request):
    data = Order.objects.all()
    template_name = 'CRUD_APP/show.html'
    context = {'data':data}
    return render(request,template_name,context)

def updateOrder(request, pk):
    obj = Order.objects.get(id = pk)
    form = OrdeerForm(instance = obj)
    template_name = 'CRUD_APP/add.html'
    if request.method == 'POST':
        form = OrdeerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form':form}
    return render(request,template_name,context)

def deleteOrder(request, pk):
    obj = Order.objects.get(id = pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'CRUD_APP/confirm.html'
    context = {'data':obj}
    return render(request,template_name,context)

def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'app1/user_list.html', { 'users': users })


