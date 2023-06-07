from django.urls import path
from restapp import views

urlpatterns = [
    path('',views.apiOverview,name='api-overview'),
    path('Bank-list/',views.BankList,name='Bank-list'),
    path('Bank-detail/<str:pk>',views.BankDetail,name='Bank-detail'),
    path('Bank-Create',views.BankCreate,name='Bank-Create'),
    path('Bank-update/<str:pk>',views.BankUpdate,name='Bank-update'),
    path('Bank-delete/<str:pk>',views.BankDelete,name='Bank-delete'),
    path('BankTable/',views.index,name='index'),
    
    path('CustTable/',views.index2,name='index2'),
    path('CustOverview',views.apiOverview1,name='api-overview1'),
    path('Cust-list/',views.CustList,name='Cust-list'),
    path('Cust-detail/<str:pk>',views.CustDetail,name='Cust-detail'),
    path('Cust-Create',views.CustCreate,name='Cust-Create'),
    path('Cust-update/<str:pk>',views.CustUpdate,name='Cust-update'),
    path('Cust-delete/<str:pk>',views.CustDelete,name='Cust-delete'),
]
