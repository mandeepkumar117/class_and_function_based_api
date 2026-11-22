from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import ProductSerializer

# Create your views here.

# REST API Learning Roadmap
# Hum is order mein padhenge:
# 1. ✅ DRF install & setup
# 2. Response()
# 3. @api_view()
# 4. GET API
# 5. POST API
# 6. Serializer kya hota hai
# 7. Serializer
# 8. ModelSerializer
# 9. PUT
# 10. PATCH
# 11. DELETE
# 12. Status codes
# 13. Validation
# 14. Error handling
# 15. APIView
# 16. Generic API Views
# 17. Authentication
# 18. Permissions
# 19. Pagination
# 20. Filtering/Search
# 21. Relationships
# 22. Complete REST API project

# Common Status Codes
# Code	Meaning	                     Kab use hota hai
# 200	    OK	                     Successful GET
# 201	    Created	                 Successfully new data create
# 204	    No Content	             Successful delete/update without response body
# 400	    Bad Request	             Client ne galat data bheja
# 401	    Unauthorized	         Authentication required/failed
# 403	    Forbidden	             Permission nahi hai
# 404	    Not Found	             Data/resource nahi mila
# 405	    Method Not Allowed	     Wrong HTTP method
# 500	    Internal Server Error	 Server-side problem


@api_view(['GET','POST'])
def home(request):

    return Response({
        "message": "Welcome to REST API"
    })

# yahan se function based api hai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET', 'POST'])
def products(request):

    # GET - All Products
    if request.method == 'GET':

        product = Product.objects.all()

        serializer = ProductSerializer(
            product,
            many=True
        )

        return Response(serializer.data)

    # POST - Create Product
    if request.method == 'POST':

        serializer = ProductSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def product_detail(request, id):

    # Find Product
    try:
        product = Product.objects.get(id=id)

    except Product.DoesNotExist:

        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET - Single Product
    if request.method == 'GET':

        serializer = ProductSerializer(product)

        return Response(serializer.data)

    # PUT - Full Update
    if request.method == 'PUT':

        serializer = ProductSerializer(
            product,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # PATCH - Partial Update
    if request.method == 'PATCH':

        serializer = ProductSerializer(
            product,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE - Delete Product
    if request.method == 'DELETE':

        product.delete()

        return Response(
            {"message": "Product deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )


# ye niche ka bhi same kaam karta hai.ye ek hi function ke through hai

# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def products(request, id=None):

#     # GET - All Products
#     if request.method == 'GET' and id is None:

#         product = Product.objects.all()

#         serializer = ProductSerializer(
#             product,
#             many=True
#         )

#         return Response(serializer.data)

#     # POST - Create Product
#     if request.method == 'POST' and id is None:

#         serializer = ProductSerializer(
#             data=request.data
#         )

#         if serializer.is_valid():

#             serializer.save()

#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     # Find Product for ID-based operations
#     try:
#         product = Product.objects.get(id=id)

#     except Product.DoesNotExist:

#         return Response(
#             {"error": "Product not found"},
#             status=status.HTTP_404_NOT_FOUND
#         )

#     # GET - Single Product
#     if request.method == 'GET':

#         serializer = ProductSerializer(product)

#         return Response(serializer.data)

#     # PUT - Full Update
#     if request.method == 'PUT':

#         serializer = ProductSerializer(
#             product,
#             data=request.data
#         )

#         if serializer.is_valid():

#             serializer.save()

#             return Response(serializer.data)

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     # PATCH - Partial Update
#     if request.method == 'PATCH':

#         serializer = ProductSerializer(
#             product,
#             data=request.data,
#             partial=True
#         )

#         if serializer.is_valid():

#             serializer.save()

#             return Response(serializer.data)

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     # DELETE - Delete Product
#     if request.method == 'DELETE':

#         product.delete()

#         return Response(
#             {"message": "Product deleted successfully"},
#             status=status.HTTP_204_NO_CONTENT
#         )


# yahan se class based api hai

# class ProductViewSet(viewsets.ModelViewSet):

#     queryset = Product.objects.all()

#     serializer_class = ProductSerializer  # sirf ye tin line ki code likh kar complete crued operation kar sakte hai

# class ProductViewSet(viewsets.ModelViewSet):

#     queryset = Product.objects.all()

#     serializer_class = ProductSerializer

#     def create(self, request):

#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():

#             serializer.save()

#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )