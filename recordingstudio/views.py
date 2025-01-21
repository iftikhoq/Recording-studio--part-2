from django.shortcuts import get_object_or_404, render, redirect
from .forms import SignupForm, LoginForm
from django.contrib import messages 
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm 
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView 
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from musician import form as mform, models as mmodels  
from album import form as aform, models as amodels  

def Home(request):
    mdata =  mmodels.Musician.objects.all()
    adata =  amodels.Album.objects.all()
    return render(request, 'index.html', {'mdata': mdata, 'adata': adata})

def SignupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Signup successful! Welcome, {user.username}.')
            return redirect('login')
        else:
            messages.error(request, 'Signup failed. Please correct the errors below.')
    else: 
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form}) 


def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('profile')  
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please fill out form correctly.")
    else:
        form = LoginForm()  
    
    return render(request, 'login.html', {'form': form})


def LogoutPage(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

@login_required
def ProfilePage(request):
    mdata =  mmodels.Musician.objects.all()
    adata =  amodels.Album.objects.all()
    return render(request, 'profile.html', {'mdata': mdata, 'adata': adata})

def Changepasswithprev(request):
    if request.method  ==  'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "You have successfully changed password.")
            return redirect('profile')
        else:
            messages.error(request, "Please fill out form correctly.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepasswithprev.html', {'form': form}) 

def Changepasswithoutprev(request):
    if request.method  ==  'POST':
        form = SetPasswordForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "You have successfully changed password.")
            return redirect('profile')
        else:
            messages.error(request, "Please fill out form correctly.")
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'changepasswithprev.html', {'form': form}) 




### class based view
# @method_decorator(login_required, name='dispatch')

class UserLoginView(LoginView):
    template_name = 'login.html' 
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']= 'Login'
        return context

    def get_success_url(self):
        return self.success_url

@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView):
    model = amodels.Album
    form_class = aform.AlbumForm
    template_name = 'addalbum.html'
    success_url = reverse_lazy('profile')
    
    
    def form_valid(self, form):
        messages.success(self.request, 'Album added successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Could not add album')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return self.success_url

@method_decorator(login_required, name='dispatch')
class AddMusician(CreateView):
    model = mmodels.Musician
    form_class = mform.MusicianForm
    template_name = 'addmusician.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Musician added successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Could not add Musician')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return self.success_url

@method_decorator(login_required, name='dispatch')
class UpdateMusician(UpdateView):
    model = mmodels.Musician
    form_class = mform.MusicianForm
    template_name = 'updatemusician.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request, 'Musician updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Could not update Musician')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return self.success_url
    
@method_decorator(login_required, name='dispatch')
class UpdateAlbum(UpdateView):
    model = amodels.Album
    form_class = aform.AlbumForm
    template_name = 'updatealbum.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = "id"
    
    def form_valid(self, form):
        messages.success(self.request, 'Album updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Could not update Album')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return self.success_url
    
@method_decorator(login_required, name='dispatch')
class DeleteAlbum(DeleteView):
    model = amodels.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = "id"
    
    def get_success_url(self):
        messages.success(self.request, 'Album deleted successfully')
        return self.success_url
    
@method_decorator(login_required, name='dispatch')
class DeleteMusician(DeleteView):
    model = mmodels.Musician
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = "id"
    

    def get_success_url(self):
        messages.success(self.request, 'Musician deleted successfully')
        return self.success_url