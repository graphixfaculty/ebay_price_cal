import streamlit as st
import math
from forex_python.converter import CurrencyRates

m=st.markdown('<style>div.stTitle {font-size:40px;}</style>',unsafe_allow_html=True)
m=st.markdown('<style>p {font-size:26px;}</style>',unsafe_allow_html=True)

# Create a currency converter
cr = CurrencyRates()

# Create Streamlit application
st.title('Price Calculator')

# Input fields
cost = st.number_input('Enter the cost', value=0)
shipping_fee = st.number_input('Enter the shipping fee', value=6500)
profit = st.number_input('Enter the mini profit', value=5000)
fee_rate = st.number_input('Enter the fee rate', value=.18)
sell_price = st.number_input('Enter the Sell Price', value=0)

# Get the current exchange rate from USD to JPY
exchange_rate = cr.get_rate('USD', 'JPY')

# Calculate the price
price = math.floor((cost + shipping_fee + profit) / (exchange_rate * 0.96) / (1 - fee_rate))

# Display the result
st.write('Break-Even price: ', price)

# Calculate the price
profit2 = math.floor((sell_price - price) * exchange_rate + profit)

# Display the result
st.write('Profit price: ', profit2)

st.write('YEN/USD: ', exchange_rate)

# CAD Cal
st.title('CAD Cal')
cad = st.number_input('Enter CAD', value=0)
# Get the current exchange rate from USD to JPY
cadexchange_rate = cr.get_rate('USD', 'CAD')
caddollar = math.floor(cad / cadexchange_rate)
caddollarprofit = caddollar - price
yencaddollarprofit = math.floor(caddollarprofit * exchange_rate)
st.write('USD price: ', caddollar)
st.write('USD Profit: ', caddollarprofit)
st.write('YEN Profit: ', yencaddollarprofit)
st.write('USD/CAD: ', cadexchange_rate)

# GBP Cal
st.title('GBP Cal')
gbp = st.number_input('Enter GBP', value=0)
# Get the current exchange rate from USD to JPY
gbpexchange_rate = cr.get_rate('USD', 'GBP')
gbpdollar = math.floor(gbp / gbpexchange_rate)
gbpdollarprofit = gbpdollar - price
yengbpdollarprofit = math.floor(gbpdollarprofit * exchange_rate)
st.write('USD price: ', gbpdollar)
st.write('USD Profit: ', gbpdollarprofit)
st.write('YEN Profit: ', yengbpdollarprofit)
st.write('USD/GBP: ', gbpexchange_rate)
