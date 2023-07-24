from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('detail/<int:post_id>', views.post_detail, name='detail'),
    path('meep_like/<int:pk>', views.meep_like, name='like_post'),
    path('search', views.search, name='search'),
    path('new_post/', views.PostCreatView.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('detail/<slug:pk>/Delete/', views.PostDeleteView.as_view(), name='post_delete'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)