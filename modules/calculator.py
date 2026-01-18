# modules/calculator.py
"""Calculation functions for Korea and China group order cost estimation."""

def calculate_korea(input_price, ongkir, people, rate_kr, jasa_tf_kr, admin_go):
    """
    Calculates total cost for Korea GO.
    item_price_idr = (input_price * 10000) * rate_kr
    shared_fees_idr = (ongkir * rate_kr + jasa_tf_kr) / people
    """
    item_price_idr = (input_price * 10000) * rate_kr
    shared_fees_idr = (ongkir * rate_kr + jasa_tf_kr) / people
    total = item_price_idr + admin_go + shared_fees_idr
    return total, item_price_idr, shared_fees_idr

def calculate_china(input_price, ongkir, people, rate_ch, jasa_tf_ch, admin_go):
    """
    Calculates total cost for China GO.
    item_price_idr = input_price * rate_ch
    shared_fees_idr = (ongkir * rate_ch + jasa_tf_ch) / people
    """
    item_price_idr = input_price * rate_ch
    shared_fees_idr = (ongkir * rate_ch + jasa_tf_ch) / people
    total = item_price_idr + admin_go + shared_fees_idr
    return total, item_price_idr, shared_fees_idr