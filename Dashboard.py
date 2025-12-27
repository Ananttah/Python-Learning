import streamlit as st # The web framework
import requests
import pandas as pd # New Library! For handling data tables.

# --- 1. SETUP THE PAGE ---
st.set_page_config(page_title="Crypto Alert", page_icon="🚀")

st.title("🚀 Bitcoin Price Tracker")
st.write("This tool fetches the live price of Bitcoin and alerts you if it's cheap.")

# --- 2. USER INPUTS (The Sidebar) ---
# We put controls in the sidebar so they look neat
with st.sidebar:
    st.header("Settings")

    # We store the user's choice in the variable 'coin_id' for dropdown
    coin_id = st.selectbox("Choose Coin", ["bitcoin", "ethereum", "solana", "dogecoin", "cardano"])

    # Let the user type in their target price!
    target_price = st.number_input("Target Price ($)", value=90000)
    
    # A button to trigger the check
    if st.button("Check Price Now"):
        refresh_clicked = True
    else:
        refresh_clicked = False

# --- 3. FETCH DATA ---
# API 1: Get Current Price (Simple)
current_url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

# API 2: Get History (Complex) - Last 7 days, hourly data
history_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days=7&interval=daily"

try:
# --- GET CURRENT PRICE ---
    response = requests.get(current_url)
    data = response.json()
    current_price = data[coin_id]["usd"]

# --- GET HISTORY FOR CHART ---
    hist_response = requests.get(history_url)
    hist_data = hist_response.json()

# Extract the list of prices via "List Comprehension"
    # The API gives us [[time, price], [time, price]...]. We just want the prices.
    prices = [item[1] for item in hist_data['prices']]

    # --- 4. VISUALS ---
    # Create two columns for a dashboard layout
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label=f"{coin_id.title()} Price", value=f"${current_price}")

    with col2:
        st.metric(label="Target Price", value=f"${target_price}")

    # --- 5. DISPLAY CHART ---
    st.subheader(f"{coin_id.title()} Trend (Last 7 Days)")
    st.line_chart(prices)

    # --- 6. THE DECISION ENGINE ---
    st.divider() # A visual line separator

    if current_price < target_price:
        st.error(f"🚨 PRICE ALERT! {coin_id.title()} is below your target! BUY NOW!")
        st.balloons() # This is a fun built-in animation!
    else:
        st.success(f"✅ {coin_id.title()} Price is stable. No action needed.")

except Exception as e:
    st.error(f"Error connecting to the API: {e}")