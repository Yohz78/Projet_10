from django.urls import path
from .views import RegisterUserAPIView

urlpatterns = [
    path("signup", RegisterUserAPIView.as_view()),
]
