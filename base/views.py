from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import PlantsProducts

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def plants_view(request, id=-1):
    if request.method == 'GET':
        if int(id) > -1:
            product = get_object_or_404(PlantsProducts, id=id)
            return Response({"id": product.id, "desc": product.type, "price": product.price})
        else:
            res = []
            for productObj in PlantsProducts.objects.all():
                res.append({"id": productObj.id, "desc": productObj.type, "price": productObj.price})
            return Response(res)

    elif request.method == 'POST':
        type = request.data.get('type')
        price = request.data.get('price')
        if type and price:
            product = PlantsProducts.objects.create(type=type, price=price)
            return Response({"id": product.id, "desc": product.type, "price": product.price}, status=status.HTTP_201_CREATED)
        return Response({"error": "Type and price are required"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if int(id) > -1:
            product = get_object_or_404(PlantsProducts, id=id)
            type = request.data.get('type')
            price = request.data.get('price')
            if type:
                product.type = type
            if price:
                product.price = price
            product.save()
            return Response({"id": product.id, "desc": product.type, "price": product.price})
        return Response({"error": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if int(id) > -1:
            product = get_object_or_404(PlantsProducts, id=id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
