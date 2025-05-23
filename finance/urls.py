from django.urls import path, include
from finance.views import RegisterView, DashboradView, TransactionCreateView
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('', DashboradView.as_view(), name="dashboard"),
    path('transaction/add/', TransactionCreateView.as_view(), name="transaction_add"),
]
