from django.urls import path, include
from finance.views import RegisterView, DashboradView, TransactionCreateView, TransactionListView, GoalCreateView
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('', DashboradView.as_view(), name="dashboard"),
    path('transaction/add/', TransactionCreateView.as_view(), name='transaction_add'),
    path('transaction_list/', TransactionListView.as_view(),
         name='transaction_list'),
    path('goal/add/', GoalCreateView.as_view(),
         name='goal_add'),
    #     path('generate-report/', export_transactions, name='export_transactions'),
]
