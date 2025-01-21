from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = 'home'),
    path('signup', views.SignupPage, name = 'signup'),
    path('login', views.UserLoginView.as_view(), name = 'login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('profile/', views.ProfilePage, name='profile'),
    path('changepasswithprev/', views.Changepasswithprev, name='changepasswithprev'),
    path('changepasswithoutprev/', views.Changepasswithoutprev, name='changepasswithoutprev'),
    path('addmusician/', views.AddMusician.as_view(), name='addmusician'),
    path('addalbum/', views.AddAlbum.as_view(), name='addalbum'),
    path('updatealbum/<int:id>', views.UpdateAlbum.as_view(), name="updatealbum"),
    path('deletealbum/<int:id>', views.DeleteAlbum.as_view(), name="deletealbum"),
    path('updatemusician/<int:id>', views.UpdateMusician.as_view(), name="updatemusician"),
    path('deletemusician/<int:id>', views.DeleteMusician.as_view(), name="deletemusician"),
    path('admin/', admin.site.urls),
]
