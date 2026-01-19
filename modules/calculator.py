# modules/calculator.py
"""Calculation functions for Korea and China group order cost estimation."""

import math

def calculate_korea(input_price, ongkir, people, rate_kr, jasa_tf_kr, admin_go):
    """
    Calculates total cost for Korea GO.
    item_price_idr = (input_price * 10000) * rate_kr
    shared_fees_idr = (ongkir * rate_kr + jasa_tf_kr) / people
    """
    item_price_idr = (input_price * 10000) * rate_kr
    item_price_idr_ceiled = math.ceil(item_price_idr / 10) * 10
    shared_fees_idr = (ongkir * rate_kr + jasa_tf_kr) / people
    shared_fees_idr_ceiled = math.ceil(shared_fees_idr / 10) * 10
    total = item_price_idr_ceiled + admin_go + shared_fees_idr_ceiled
    return total, item_price_idr_ceiled, shared_fees_idr_ceiled
def calculate_china(input_price, ongkir, people, rate_ch, jasa_tf_ch, admin_go):
    """
    Calculates total cost for China GO.
    item_price_idr = input_price * rate_ch
    shared_fees_idr = (ongkir * rate_ch + jasa_tf_ch) / people
    """
    item_price_idr = input_price * rate_ch
    item_price_idr_ceiled = math.ceil(item_price_idr / 10) * 10
    shared_fees_idr = (ongkir * rate_ch + jasa_tf_ch) / people
    shared_fees_idr_ceiled = math.ceil(shared_fees_idr / 10) * 10
    total = item_price_idr_ceiled + admin_go + shared_fees_idr_ceiled
    return total, item_price_idr_ceiled, shared_fees_idr_ceiled