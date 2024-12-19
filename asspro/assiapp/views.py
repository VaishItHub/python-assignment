# from django.shortcuts import render

# # Create your views here.
# # simulation/views.py
# import threading
# from django.http import JsonResponse
# from .models import User, Product, Order
# from random import randint

# def create_user():
#     user = User.objects.create(
#         name=f"User {randint(1, 100)}",
#         email=f"user{randint(1, 100)}@example.com"
#     )
#     return user

# def create_product():
#     product = Product.objects.create(
#         name=f"Product {randint(1, 100)}",
#         price=randint(10, 100)
#     )
#     return product

# def create_order(user, product):
#     order = Order.objects.create(
#         user=user,
#         product=product,
#         quantity=randint(1, 5)
#     )
#     return order

# def simulate_inserts(request):
#     users = []
#     products = []
#     orders = []

#     def insert_data():
#         user = create_user()
#         product = create_product()
#         order = create_order(user, product)
#         users.append(user)
#         products.append(product)
#         orders.append(order)

#     threads = []
#     for _ in range(10):  # Simulate 10 simultaneous insertions for each model
#         t = threading.Thread(target=insert_data)
#         threads.append(t)
#         t.start()

#     for t in threads:
#         t.join()

#     return JsonResponse({
#         'users': [user.name for user in users],
#         'products': [product.name for product in products],
#         'orders': [f"Order {order.id} for {order.user.name}" for order in orders]
#     })
import threading
from django.http import JsonResponse
from .models import User, Product, Order
from random import randint

def create_user():
    user = User.objects.create(
        name=f"User {randint(1, 100)}",
        email=f"user{randint(1, 100)}@example.com"
    )
    return user

def create_product():
    product = Product.objects.create(
        name=f"Product {randint(1, 100)}",
        price=randint(10, 100)
    )
    return product

def create_order(user, product):
    order = Order.objects.create(
        user=user,
        product=product,
        quantity=randint(1, 5)
    )
    return order

def simulate_inserts(request):
    users = []
    products = []
    orders = []

    def insert_data():
        user = create_user()
        product = create_product()
        order = create_order(user, product)
        users.append(user)
        products.append(product)
        orders.append(order)

    threads = []
    for _ in range(10):  # Simulate 10 simultaneous insertions for each model
        t = threading.Thread(target=insert_data)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return JsonResponse({
        'users': [user.name for user in users],
        'products': [product.name for product in products],
        'orders': [f"Order {order.id} for {order.user.name}" for order in orders]
    })
