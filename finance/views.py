from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
# create this if you haven't
from finance.forms import RegisterForm, TransactionForm, GoalForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Transaction, Goal


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
        return render(request, 'finance/transaction_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
            message.success(request, 'transaction added succesfully')
        return render(request, 'finance/transaction_form.html', {'form': form})


class TransactionListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.all()
        return render(request, 'finance/transaction_list.html', {'transactions': transactions})


class GoalCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = GoalForm()
        return render(request, 'finance/goal_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')
            # message.success(request, 'transaction added succesfully')
        return render(request, 'finance/goal_form.html', {'form': form})
