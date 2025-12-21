import streamlit as st # The web framework
import requests

# --- 1. SETUP THE PAGE ---
st.set_page_config(page_title="Crypto Alert", page_icon="🚀")

st.title("🚀 Bitcoin Price Tracker")
st.write("This tool fetches the live price of Bitcoin and alerts you if it's cheap.")

# --- 2. USER INPUTS (The Sidebar) ---
# We put controls in the sidebar so they look neat
with st.sidebar:
    st.header("Settings")
    # Let the user type in their target price!
    target_price = st.number_input("Target Price ($)", value=90000)
    
    # A button to trigger the check
    if st.button("Check Price Now"):
        refresh_clicked = True
    else:
        refresh_clicked = False

# --- 3. THE LOGIC ---
# We only run the expensive API call when the app loads or button is clicked
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    response = requests.get(url)
    data = response.json()
    current_price = data["bitcoin"]["usd"]

    # --- 4. VISUALS ---
    # Create two columns for a dashboard layout
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Current Price", value=f"${current_price}")

    with col2:
        st.metric(label="Target Price", value=f"${target_price}")

    # --- 5. THE DECISION ENGINE ---
    st.divider() # A visual line separator

    if current_price < target_price:
        st.error("🚨 PRICE ALERT! Bitcoin is below your target! BUY NOW!")
        st.balloons() # This is a fun built-in animation!
    else:
        st.success("✅ Price is stable. No action needed.")

except Exception as e:
    st.error(f"Error connecting to API: {e}")