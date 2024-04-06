from django.urls import path
from testapi.views import UserLogin

urlpatterns = [
    path('login', UserLogin.as_view(), name='login'),
]