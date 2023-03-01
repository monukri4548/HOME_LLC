from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
#from platformdirs import user_config_path
from .forms import CustomerRegistrationForm, LoginForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator



class ProductView(View):
    def get(self, request):
        totalitem = 0
        return render(request, 'app/home.html', {
            'totalitem': totalitem,
        })
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "Your Account Created Successful, To Verifi your account Check your email.")
            return render(request, 'app/customerregistration.html', {'form': form})
        return render(request, 'app/customerregistration.html', {'form': form})
