from django.urls import path

from users.views import ProfileUpdateView

app_name = 'profile'

urlpatterns = [
    path('', ProfileUpdateView.as_view(), name='home')
]


