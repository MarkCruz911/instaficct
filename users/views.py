"""Users views"""
#from django

from pipes import Template
import profile
from re import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy 
from django.views.generic import DetailView, FormView , UpdateView
from users.models import Profile

#Models
from django.contrib.auth.models import User
from posts.models import Post


#forms
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """User Detail View."""
    template_name='users/detail.html'
    slug_field='username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name: 'user'

    def get_context_data(self, **kwargs):
        """ add user's posts to context. """
        context = super().get_context_data(**kwargs)
        user= self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update Profile View."""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website','biography', 'phone_number', 'picture']
    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile
    def get_success_url(self):
        """Return to users profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username':username})


class LoginView(auth_views.LoginView):
    """Login View."""
    template_name= 'users/login.html'
    redirect_authenticated_user= True



class SignupView(FormView):
    """User signup view."""
    template_name= 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
    
class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view"""
    template_name= 'users/logget_out.html'





