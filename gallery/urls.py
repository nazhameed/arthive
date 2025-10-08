from django.urls import path
from . import views
from .views import add_child
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-child/', add_child, name='add_child'),
    path('edit_child/<int:child_id>/', views.edit_child, name='edit_child'),
    path('delete_child/<int:child_id>/', views.delete_child, name='delete_child'),
    path('add_artwork/<int:child_id>/', views.add_artwork, name='add_artwork'),
    path('gallery/<int:child_id>/', views.gallery, name='gallery'),
    path('gallery/<int:child_id>/art/<int:artwork_id>/edit/', views.edit_artwork, name='edit_artwork'),
    path('gallery/<int:child_id>/art/<int:artwork_id>/delete/', views.delete_artwork, name='delete_artwork'),
]
