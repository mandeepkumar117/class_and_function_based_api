from django.test import TestCase

# Create your tests here.

# Bilkul 👍 Ab jab image + PDF upload successfully ho gaya, to ab is create() code ko line-by-line aur actual POST flow ke saath samajhte hain.

# Tumhara code:
# class ProductViewSet(viewsets.ModelViewSet):    queryset = Product.objects.all()    serializer_class = ProductSerializer    def create(self, request):        serializer = ProductSerializer(data=request.data)        if serializer.is_valid():            serializer.save()            return Response(                serializer.data,                status=status.HTTP_201_CREATED            )        return Response(            serializer.errors,            status=status.HTTP_400_BAD_REQUEST        )


# 1. class ProductViewSet
# class ProductViewSet(viewsets.ModelViewSet):


# Yahan hum ProductViewSet naam ki class bana rahe hain.
# ProductViewSet
#       ↓
# ModelViewSet

# ModelViewSet DRF ki built-in class hai.

# Iske through hume automatically ye operations milte hain:
# HTTP	Operation
# GET	List
# GET	Single product
# POST	Create
# PUT	Update
# PATCH	Partial update
# DELETE	Delete


# Lekin hum abhi POST/create ko manually samajh rahe hain.
# 2. queryset
# queryset = Product.objects.all()


# Iska matlab:
# Product table ke saare records lekar aao.

# Example database:
# id	product_name	price
# 1	Laptop	55000
# 2	Mobile	25000
# 3	Mouse	800


# Product.objects.all()


# se ye saare products milenge.
# Product.objects.all()
#         ↓
# Database
#         ↓
# All Products

# Product
# Tumhara Django model:
# class Product(models.Model):


# objects
# Django ka manager hai.
# all()
# Saare records select karta hai.
# 3. serializer_class
# serializer_class = ProductSerializer


# Yahan hum DRF ko bata rahe hain:
# Product ke data ke liye ProductSerializer use karo.

# Tumhara serializer:
# class ProductSerializer(serializers.ModelSerializer):


# hai.

# Flow:
# Product Model
#      ↓
# ProductSerializer
#      ↓
# API

# 4. create() method
# def create(self, request):


# Ye hamara POST method hai.

# Jab Postman se:
# POST /api/products/

# request aati hai, to ye method execute hota hai.
# Postman
#    ↓
# POST
#    ↓
# Router
#    ↓
# ProductViewSet
#    ↓
# create()

# 5. request
# def create(self, request):


# request ke andar client/Postman se aaya hua data hota hai.

# Tumne Postman me bheja:
# product_name       = Laptop
# product_category   = Electronics
# product_image      = laptop.jpg
# product_file       = laptop.pdf
# product_price      = 55000
# product_stock      = 10

# Ye data request ke andar available hai.
# 6. request.data
# Ab ye line dekho:
# serializer = ProductSerializer(data=request.data)


# Sabse pehle:
# request.data


# samjho.

# request.data ka matlab:
# Client/Postman ne jo data bheja hai, woh data.

# Example:
# request.data


# roughly:
# {
#     product_name: Laptop,
#     product_category: Electronics,
#     product_image: laptop.jpg,
#     product_file: laptop.pdf,
#     product_price: 55000,
#     product_stock: 10
# }

# 7. Serializer ko data dena
# serializer = ProductSerializer(data=request.data)


# Yahan hum keh rahe hain:
# ProductSerializer, ye jo data client se aaya hai, ise check karo.

# request.data
#      ↓
# ProductSerializer

# Abhi database me save nahi hua hai.

# Ye bahut important hai.
# 8. is_valid()
# if serializer.is_valid():


# Ab serializer incoming data ko validate karega.

# Matlab check karega:
# Data sahi hai?
#        ↓
#    YES / NO

# Example:
# product_name → Laptop          ✅
# product_price → 55000          ✅
# product_stock → 10             ✅
# product_image → valid image    ✅
# product_file → valid file      ✅

# To:
# serializer.is_valid()


# returns:
# True

# 9. Agar data valid hai
# if serializer.is_valid():


# Agar:
# True

# hai to andar ka code chalega:
# serializer.save()


# 10. serializer.save()
# Ye bahut important line hai.
# serializer.save()


# Iska matlab:
# Validated data ko database me save karo.

# Flow:
# request.data
#      ↓
# Serializer
#      ↓
# is_valid()
#      ↓
# True
#      ↓
# save()
#      ↓
# Product Database

# Example database me new row:
# id	product_name	category	price	stock
# 1	Laptop	Electronics	55000	10


# Image:
# media/products/images/laptop.jpg

# PDF:
# media/products/files/laptop.pdf

# Aur database me un files ka path store hota hai.
# 11. Response()
# Ab:
# return Response(    serializer.data,    status=status.HTTP_201_CREATED)


# Database me save hone ke baad client ko response bhej rahe hain.
# 12. serializer.data
# serializer.data


# ka matlab:
# Jo product successfully create hua hai, uska serialized/API-friendly data.

# Example:
# {
#     "id": 1,
#     "product_name": "Laptop",
#     "product_category": "Electronics",
#     "product_image": "/media/products/images/laptop.jpg",
#     "product_file": "/media/products/files/laptop.pdf",
#     "product_price": "55000.00",
#     "product_stock": 10
# }

# Ye Postman ko response me milega.
# 13. HTTP_201_CREATED
# status=status.HTTP_201_CREATED


# 201 ka meaning:
# New resource successfully create ho gaya.

# Isliye POST successful hone par:
# 201 Created

# milta hai.
# 14. Agar data invalid ho
# Ab ye part:
# return Response(    serializer.errors,    status=status.HTTP_400_BAD_REQUEST)


# Ye tab chalega jab:
# serializer.is_valid()


# returns:
# False

# Example agar price galat data ho:
# product_price = abc

# to serializer kahega:
# Invalid data

# Aur:
# serializer.errors


# me error details milengi.

# Response:
# 400 Bad Request

# Complete flow
# Ab poora create() ek baar flow me dekho:
#                 POST Request
#                      ↓
#               /api/products/
#                      ↓
#               ProductViewSet
#                      ↓
#                   create()
#                      ↓
#               request.data
#                      ↓
#              ProductSerializer
#                      ↓
#              serializer.is_valid()
#                 ↙             ↘
#              True             False
#               ↓                 ↓
#     serializer.save()    serializer.errors
#               ↓                 ↓
#           Database          400 Bad Request
#               ↓
#       serializer.data
#               ↓
#        201 Created

# Ek real example
# Postman se:
# product_name = Laptop
# product_category = Electronics
# product_image = laptop.jpg
# product_file = laptop.pdf
# product_price = 55000
# product_stock = 10

# Step 1
# request.data


# ↓

# Postman ka data mila.
# Step 2
# ProductSerializer(data=request.data)


# ↓

# Data serializer ko diya.
# Step 3
# serializer.is_valid()


# ↓

# Data valid hai? ✅
# Step 4
# serializer.save()


# ↓

# Database me Product create.
# Step 5
# serializer.data


# ↓

# Created product ka data.
# Step 6
# Response(..., status=201)


# ↓

# Postman ko response.
# Sabse important 4 lines yaad rakho
# serializer = ProductSerializer(data=request.data)


# Data serializer ko do
# serializer.is_valid()


# Data check karo
# serializer.save()


# Database me save karo
# serializer.data


# Response ke liye serialized data lo

# Yahi DRF POST ka core flow hai.



# =====put and patch=======

# put main sare data ko send karna hota hai.ye compusory hai
# And patch main single data ko bhi send kar sakte.

# how to update data from postman.
# 1) phale data ko Get method se data ko get karo
# baad main method ko change kardo or phir body ko
# select karo or phir form_data ko select karo