from django.shortcuts import get_object_or_404
from .models import Payment
from .serializers import GetSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializer = PostSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def update_eid(request, eid):
    payment = get_object_or_404(Payment, eid=eid)

    if request.method == 'GET':
        serializer = PostSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PostSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
