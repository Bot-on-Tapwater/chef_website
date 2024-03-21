from django.urls import path
from . import views

urlpatterns = [
                  # Chef URLs
                  path('chefs/', views.chef_list, name='chef_list'),
                  path('chef/new/', views.chef_create, name='chef_create'),
                  path('chef/<int:pk>/', views.chef_detail, name='chef_detail'),
                  path('chef/<int:pk>/edit/', views.chef_update, name='chef_update'),
                  path('chef/<int:pk>/delete/', views.chef_delete, name='chef_delete'),

                  # Other URLs
                  path('', views.home_page, name='home_page'),  # Home page
                  path('services/', views.services, name='services'),  # Services page
                  path('contact/', views.contact, name='contact'),  # Contact page
              ]
