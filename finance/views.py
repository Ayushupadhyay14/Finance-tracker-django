from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from finance.forms import RegisterForm,TransactionForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# it use to create a bussiness logis :


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'finance/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('dashboard')


class DashboradView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'finance/dashboard.html')


class TransactionCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TransactionForm()
        return render(request, 'finance/transaction_form.html',{'form': form})







"""for EXAMPLE PURPOSE CODE IN HTML AND CSS"""
# #functio based viwe in django
# def home(req):
#     return render(req, 'finance/home.html'),

# # class based viwes
# class HomeView(View):
#     def get(sef, request, *args, **kwargs):
#         return HttpResponse("<h1> hellow Ayush Upadhyay</h1>")


# # class based view template :
# class HomeView(View):
#     def get(sef, request, *args, **kwargs):
#         return render(request,'finance/home.html')
