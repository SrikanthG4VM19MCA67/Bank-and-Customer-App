from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .seriaizers import *

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/Bank-list',
        'DetailView':'Bank-detail/<str:pk>',
        'Create':'Bank-Create',
        'Update':'Bank-update/<str:pk>',
        'Delete':'Bank-delete/<str:pk>',
    }
    return Response(api_urls)  

# Customer api-overview:-
@api_view(['GET'])
def apiOverview1(request):
    api_urls={
        'CList':'/Cust-list',
        'CDetailView':'Cust-detail/<str:pk>',
        'CCreate':'Cust-Create',
        'CUpdate':'Cust-update/<str:pk>',
        'CDelete':'Cust-delete/<str:pk>',
    }
    return Response(api_urls)

# LisstView:-
@api_view(['GET'])
def BankList(request):
    bank=Bank.objects.all()
    serializer=BankSerializers(bank,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CustList(request):
    cust=Customer.objects.all()
    serializer=CustomerSerializers(cust,many=True)
    return Response(serializer.data)

# CreateView:-
@api_view(['POST'])
def BankCreate(request):
    serializer=BankSerializers(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def CustCreate(request):
    serializer=CustomerSerializers(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# ReadeView:-
@api_view(['GET'])
def BankDetail(request,pk):
    bank=Bank.objects.get(id=pk)
    serializer=BankSerializers(bank,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def CustDetail(request,pk):
    cust=Customer.objects.get(id=pk)
    serializer=CustomerSerializers(cust,many=False)
    return Response(serializer.data)

# UpdateView:-
@api_view(['POST'])
def BankUpdate(request,pk):
    bank=Bank.objects.all(id=pk)
    serializer=BankSerializers(instance=bank,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def CustUpdate(request,pk):
    cust=Customer.objects.all(id=pk)
    serializer=CustomerSerializers(instance=cust,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# DeleteView:-
@api_view(['DELTE'])
def BankDelete(request,pk):
    bank=Bank.objects.get(id=pk)
    bank.delete()
    return Response('Item deletes Successfully')

@api_view(['DELTE'])
def CustDelete(request,pk):
    cust=Customer.objects.get(id=pk)
    cust.delete()
    return Response('Item deletes Successfully')

def index(request):
    bank=Bank.objects.all()
    data={
        'bank':bank
    }
    return render(request,'index.html',data)

def index2(request):
    cust=Customer.objects.all()
    data={
        'cust':cust
    }
    return render(request,'index2.html',data)
