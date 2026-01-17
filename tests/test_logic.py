
def calculate_korea(input_price, ongkir, people, rate_kr, jasa_tf_kr, admin_go):
    # Logic:
    # Item_Price_IDR = (Input_Value * 10000) * rate_kr
    # Shared_Fees_IDR = (Ongkir_Input * rate_kr + jasa_tf_kr) / Number_of_People
    # Total = Item_Price_IDR + admin_go + Shared_Fees_IDR

    item_price_idr = (input_price * 10000) * rate_kr
    shared_fees_idr = (ongkir * rate_kr + jasa_tf_kr) / people
    total = item_price_idr + admin_go + shared_fees_idr
    return total

def calculate_china(input_price, ongkir, people, rate_ch, jasa_tf_ch, admin_go):
    # Logic:
    # Item_Price_IDR = Input_Value * rate_ch
    # Shared_Fees_IDR = (Ongkir_Input * rate_ch + jasa_tf_ch) / Number_of_People
    # Total = Item_Price_IDR + admin_go + Shared_Fees_IDR

    item_price_idr = input_price * rate_ch
    shared_fees_idr = (ongkir * rate_ch + jasa_tf_ch) / people
    total = item_price_idr + admin_go + shared_fees_idr
    return total

def test_korea_calculation():
    # Context
    admin_go = 6000
    rate_kr = 11.75
    jasa_tf_kr = 6000

    # Inputs
    input_price = 1.0 # Means 10,000 Won
    ongkir = 2000
    people = 1

    # Expected:
    # Item = 1.0 * 10000 * 11.75 = 117,500
    # Shared = (2000 * 11.75 + 6000) / 1 = (23,500 + 6000) / 1 = 29,500
    # Total = 117,500 + 6000 + 29,500 = 153,000

    result = calculate_korea(input_price, ongkir, people, rate_kr, jasa_tf_kr, admin_go)
    print(f"KR Result: {result}")
    assert result == 153000

def test_china_calculation():
    # Context
    admin_go = 6000
    rate_ch = 2450
    jasa_tf_ch = 10000

    # Inputs
    input_price = 10 # 10 Yuan
    ongkir = 100
    people = 2

    # Expected:
    # Item = 10 * 2450 = 24,500
    # Shared = (100 * 2450 + 10000) / 2 = (245,000 + 10,000) / 2 = 255,000 / 2 = 127,500
    # Total = 24,500 + 6000 + 127,500 = 158,000

    result = calculate_china(input_price, ongkir, people, rate_ch, jasa_tf_ch, admin_go)
    print(f"CH Result: {result}")
    assert result == 158000

if __name__ == "__main__":
    test_korea_calculation()
    test_china_calculation()
    print("All logic tests passed!")
