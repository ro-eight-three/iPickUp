"""
from "manage.py shell"
load this module and run do_stuff() fill up the database with ~random data
"""
import os
import sys
import random
import math
import datetime
from django.contrib.auth.models import User
from sellers.models import Seller
from products.models import Product

from . import gen_data

chance_calls_counter = 0


def chance(chance_factor=2):
    global chance_calls_counter
    chance_calls_counter += 1
    random.seed(
        int(chance_calls_counter * datetime.datetime.now().microsecond *
            math.pi * 1000000))
    return not int(random.random() * 1000) % chance_factor


def gen_seller_name():

    word_list = []

    if chance(5):
        word_list.append('The')

    if chance():
        random_index = random.randint(0, len(gen_data.intensifiers) - 1)
        intensifier = gen_data.intensifiers[random_index]
        word_list.append(intensifier)

    random_index = random.randint(0, len(gen_data.adjectives) - 1)
    adjective = gen_data.adjectives[random_index]
    word_list.append(adjective)

    random_index = random.randint(0, len(gen_data.establishments) - 1)
    establishment = gen_data.establishments[random_index]
    word_list.append(establishment)

    return ' '.join(str(s) for s in word_list)


def gen_product_name():

    word_list = []

    random_index = random.randint(0, len(gen_data.adjectives) - 1)
    adjective = gen_data.adjectives[random_index]
    word_list.append(adjective)

    random_index = random.randint(0, len(gen_data.foods) - 1)
    food = gen_data.foods[random_index]
    word_list.append(food)

    return ' '.join(str(s) for s in word_list)


def gen_seller():
    seller = Seller()
    seller.presentation_name = gen_seller_name()

    username = seller.presentation_name.lower()
    username = username.replace(' ', '_')
    try:
        user = User.objects.create_user(username, '', 'asdfghjkl')
    except Exception as x:
        print("Some error happened: {}".format(x))
        return

    seller.user = user
    seller.save()
    print('created user: {}'.format(seller.presentation_name))
    return seller


def gen_product(seller):
    product = Product()
    product.name = gen_product_name()
    product.seller = seller
    preparation_time = random.randint(1, 6) * 5
    product.save()
    print('created product: {} for seller {}'.format(product.name,
                                                     seller.presentation_name))
    return product


def do_stuff():
    for s in range(22):
        seller = gen_seller()
        if seller:
            for p in range(33):
                gen_product(seller)


def gen_preparation_times():
    for product in Product.objects.all():
        product.preparation_time = random.randint(1, 6) * 5
        product.save()
