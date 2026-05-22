import requests
import base64
from datetime import datetime
from decouple import config
BASE_URL = (
    "https://sandbox.safaricom.co.ke"
)
def get_access_token():
    consumer_key = config(
        "MPESA_CONSUMER_KEY"
    )
    consumer_secret = config(
        "MPESA_CONSUMER_SECRET"
    )
    response = requests.get(
        f"{BASE_URL}/oauth/v1/generate?grant_type=client_credentials",
        auth=(
            consumer_key,
            consumer_secret
        )
    )
    return (
        response.json()
        ["access_token"]
    )
def stk_push(
    phone,
    amount
):
    token = (
        get_access_token()
    )
    shortcode = config(
        "MPESA_SHORTCODE"
    )
    passkey = config(
        "MPESA_PASSKEY"
    )
    timestamp = (
        datetime.now()
        .strftime(
            "%Y%m%d%H%M%S"
        )
    )
    password = (
        base64.b64encode(
            (
                shortcode
                +
                passkey
                +
                timestamp
            ).encode()
        )
        .decode()
    )
    headers = {
        "Authorization":
        f"Bearer {token}"
    }
    payload = {
        "BusinessShortCode":
        shortcode,
        "Password":
        password,
        "Timestamp":
        timestamp,
        "TransactionType":
        "CustomerPayBillOnline",
        "Amount":
        amount,
        "PartyA":
        phone,
        "PartyB":
        shortcode,
        "PhoneNumber":
        phone,
        "CallBackURL":
        config(
            "MPESA_CALLBACK_URL"
        ),
        "AccountReference":
        "Medicore",
        "TransactionDesc":
        "Hospital Payment"
    }
    response = requests.post(
        f"{BASE_URL}/mpesa/stkpush/v1/processrequest",
        json=payload,
        headers=headers
    )
    return response.json()