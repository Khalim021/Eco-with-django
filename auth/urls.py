from django.urls import path, include

from auth.views import password_changed

urlpatterns = [
    path('password/change/done/', password_changed),
    path('', include('registration.backends.default.urls'))
]
