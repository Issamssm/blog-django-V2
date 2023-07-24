from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('change_password', views.PasswordChangeView.as_view(template_name='user/updatepassword.html'),name='change_password'),
    path('password_change_done', views.password_success ,name='password_change_done')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)