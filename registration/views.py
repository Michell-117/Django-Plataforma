from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail , ProfileForm
from .models import Profile

# Create your views here.
class SingUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') +'?registrer'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'col-md-6', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'col-md-6', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'col-md-6', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'col-md-6', 'placeholder':'Repite la contraseña'})
        return form

        
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('perfil')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

# def login(request):
# 	#if request.method == 'POST':
# 	return render(request, 'registration/login.html')


# def registration(request):
# 	#if request.method == 'POST':
# 	return render(request, 'registration/registro.html')

class preferenciasView(TemplateView):
    template_name = "registration/preferencias.html"
   
class perfilView(TemplateView):
    template_name = "registration/perfil.html"