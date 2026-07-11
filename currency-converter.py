import streamlit as st
import requests

st.title("Currency Converter")

currencies = [
    "NPR",  # Nepalese Rupee
    "INR",  # Indian Rupee
    "USD",  # US Dollar
    "EUR",  # Euro
    "GBP",  # British Pound Sterling
    "JPY",  # Japanese Yen
    "AUD",  # Australian Dollar
    "CAD",  # Canadian Dollar
    "CHF",  # Swiss Franc
    "CNY",  # Chinese Yuan
    "HKD",  # Hong Kong Dollar
    "SGD",  # Singapore Dollar
    "KRW",  # South Korean Won
    "AED",  # UAE Dirham
    "SAR",  # Saudi Riyal
    "QAR",  # Qatari Riyal
    "KWD",  # Kuwaiti Dinar
    "BHD",  # Bahraini Dinar
    "OMR",  # Omani Rial
    "THB",  # Thai Baht
    "MYR",  # Malaysian Ringgit
    "IDR",  # Indonesian Rupiah
    "PHP",  # Philippine Peso
    "VND",  # Vietnamese Dong
    "PKR",  # Pakistani Rupee
    "BDT",  # Bangladeshi Taka
    "LKR",  # Sri Lankan Rupee
    "RUB",  # Russian Ruble
    "ZAR",  # South African Rand
    "BRL",  # Brazilian Real
    "MXN",  # Mexican Peso
    "TRY",  # Turkish Lira
    "SEK",  # Swedish Krona
    "NOK",  # Norwegian Krone
    "DKK",  # Danish Krone
    "NZD",  # New Zealand Dollar
]

from_currency = st.selectbox("Select your source currency:",currencies)
amount = st.number_input("Enter an amount in " + from_currency + ":",min_value=1)
target_currency = st.selectbox("Select your target currency:",currencies)
if st.button("Convert"):
    url="https://api.exchangerate-api.com/v4/latest/" + from_currency
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        target = data['rates'][target_currency] * amount
        st.write(f"{amount} {from_currency} is equal to {target:.2f} {target_currency}.")
    else:
        st.error("Error: Could not connect to the server.")
        