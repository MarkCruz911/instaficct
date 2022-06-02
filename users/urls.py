"""users urls."""
#django
from re import template
from django.urls import path


#views
from users import views

urlpatterns = [
    #Posts
    path(
    route= 'profile/<str:username>/',
    view=views.UserDetailView.as_view(),
    name='detail'
    ),
    # Management
    path(
        route= 'login/',
        view= views.LoginView.as_view(), 
        name='login'
    ),

    path(
        route= 'logout/',
        view= views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        route='signup/',
        view= views.SignupView.as_view(),
        name='signup'
    ),

    path(
        route= 'me/profile',
        view= views.UpdateProfileView.as_view(), 
        name='update'
    )
]


