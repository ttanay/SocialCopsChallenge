from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

import datetime

from .forms import UserForm

def get_runtime_string(activation_timestamp):
    now = timezone.now()
    diff = now - activation_timestamp
    total_seconds = diff.total_seconds()
    hours = int(total_seconds / 3600)
    mins = int((total_seconds % 3600) / 60)
    runtime_string = str()
    if hours:
        runtime_string += str(hours) + ' hours '
    runtime_string += str(mins) + ' mins'
    return runtime_string

# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    email_runtime = None
    phone_runtime = None
    if user.email_activation_timestamp:
        email_runtime = get_runtime_string(user.email_activation_timestamp)
    if user.phone_activation_timestamp:
        phone_runtime = get_runtime_string(user.phone_activation_timestamp)
    context = {
        'user': user,
        'email_runtime': email_runtime,
        'phone_runtime': phone_runtime,
    }
    return render(request, 'app/dashboard.html', context)

class UserFormView(View):
    form_class = UserForm
    template_name = 'app/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']

            user.set_password(password)
            user.name = name
            user.phone_number = phone

            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
        data = dict(form.data)
        invalid = []
        for data_object in data:
            if data_object in form.errors:
                print('data_object: ' + data_object)
                print('inavlid: ' + data_object)
                invalid.append(data_object)
        for data_object in  invalid:
            data.pop(data_object)
        data.pop('csrfmiddlewaretoken')
        data.pop('password')
        form.inital = data
        print(form.inital)
        return render(request, self.template_name, {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'app/login.html', {'error_message': 'Your account has been disabled.'})
        else:
            return render(request, 'app/login.html', {'error_message': 'Invalid Login Credentials'})
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'app/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def activate_email(request):
    if request.user.is_authenticated:
        user = request.user
        if user.email_remind_status == False:
            user.email_remind_status = True
            user.email_activation_timestamp = timezone.now()
            user.save()
            data = {"success": True}
            return JsonResponse(data)
    data = {"success": False}
    return JsonResponse(data)

def deactivate_email(request):
    if request.user.is_authenticated:
        user = request.user
        if user.email_remind_status == True:
            user.email_remind_status = False
            user.email_activation_timestamp = None
            user.save()
            data = {"success": True}
            return JsonResponse(data)
    data = {"success": False}
    return JsonResponse(data)

def activate_phone(request):
    if request.user.is_authenticated:
        user = request.user
        if user.phone_remind_status == False:
            user.phone_remind_status = True
            user.phone_activation_timestamp = timezone.now()
            user.save()
            data = {"success": True}
            return JsonResponse(data)
    data = {"success": False}
    return JsonResponse(data)

def deactivate_phone(request):
    if request.user.is_authenticated:
        user = request.user
        if user.phone_remind_status == True:
            user.phone_remind_status = False
            user.phone_activation_timestamp = None
            user.save()
            data = {"success": True}
            return JsonResponse(data)
    data = {"success": False}
    return JsonResponse(data)
