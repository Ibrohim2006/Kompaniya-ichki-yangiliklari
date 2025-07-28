from django.urls import path
from authentication.views import RegisterViewSet

urlpatterns = [
    path('register/', RegisterViewSet.as_view({'post': 'register'}), name='register'),
]
