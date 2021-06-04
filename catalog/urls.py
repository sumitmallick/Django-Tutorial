from django.views.generic import RedirectView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name='create'),
    path("edit/<int:pk>/", views.edit, name='edit'),
    path('<int:pk>', views.ContactDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.delete, name='delete')
]