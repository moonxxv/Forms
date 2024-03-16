from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_smartphone, name="create"),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in')
]
