from django.urls import path

from app import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/edit/", views.EditView.as_view(), name="edit"),
]
