import requests
import time # New library! Use this to pause the script.

# --- CONFIGURATION ---
target_price = 88000  # Change this to a price close to the current price to test it!
coin_id = "bitcoin"
currency = "usd"

# --- THE LOOP ---
while True:
    # 1. Fetch the data
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # 2. Extract the specific number (Data Surgery)
        current_price = data[coin_id][currency]
        
        # 3. Print the status
        print(f"Current Price: ${current_price}")
        
        # 4. Check against our target
        if current_price < target_price:
            print("🚨 ALERT! Price is LOW! Time to Buy! 🚨")
            print("🚨 ALERT! Price is LOW! Time to Buy! 🚨")
            print("🚨 ALERT! Price is LOW! Time to Buy! 🚨")
        else:
            print("Price is still high. Waiting...")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

    # 5. Wait for 10 seconds before checking again (So we don't get banned)
    print("Waiting 10 seconds...")
    print("-" * 30) # Prints a divider line
    time.sleep(10)