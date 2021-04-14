from django.urls import path
from todos import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
]
