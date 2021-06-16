from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


def password_changed(request):
    messages.add_message(request, messages.INFO, 'Password changed successfully')
    return redirect(reverse('profile:home'))
