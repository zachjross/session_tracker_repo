from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .models import Client
from .forms import ClientForm

# Create your views here.
@login_required
def index(request):
    """The home page for session calculator app."""
    clients = Client.objects.filter(owner=request.user).all()
    context = {'clients': clients}
    return render(request, 'session_tracker/index.html', context=context)

@login_required
def new_client(request):
    """Add a new client"""
    if request.method != 'POST':
        form = ClientForm()
    else:
        form = ClientForm(data=request.POST)
        if form.is_valid:
            new_client = form.save(commit=False)
            new_client.owner = request.user
            new_client.save()      
        return redirect('session_tracker:index')
    
    context = {'form': form}
    return render(request, 'session_tracker/new_client.html', context=context)

@login_required
def subtract_session(request, client_id):
    """Subtract a session from a client"""
    if request.method == 'POST':
        client = Client.objects.get(id=client_id)
        client.sessions -= 1
        if client.sessions < 1:
            client.sessions = 0
        client.save()
    return HttpResponseRedirect('/')

@login_required
def add_session(request, client_id):
    """Add a session for a client"""
    if request.method == 'POST':
        client = Client.objects.get(id=client_id)
        client.sessions += 1
        client.save()
    return HttpResponseRedirect('/')








