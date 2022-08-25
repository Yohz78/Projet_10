from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.ProjectDetailAPIView.as_view()),
    path("", views.ProjectCreateAPIView.as_view()),
]