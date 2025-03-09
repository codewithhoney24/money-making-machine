import streamlit as st
import random
import time
import requests

# Set page configuration
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
    .big-font { font-size: 22px !important; color: #4CAF50; font-weight: bold; }
    .stButton>button { background-color: #ff5733; color: white; font-size: 18px; border-radius: 10px; padding: 10px; }
    .stSuccess { color: #4CAF50; font-size: 24px; font-weight: bold; }
    .stInfo { color: #1976D2; font-size: 20px; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💰 Money Making Machine 💰")

# Function to generate random money
def generate_money():
    return random.randint(1, 1000)

# Instant Cash Generator Section
st.subheader("🤑 Instant Cash Generator")
if st.button("💵 Generate Money"):
    st.write("💸 Counting your money... Please wait...")  
    time.sleep(3)
    amount = generate_money()
    st.success(f"🎉 Congratulations! You made **${amount}**! 🎉")

# Fallback list for side hustle ideas
fallback_hustles = [
    "Freelancing 🖥️", "Start a YouTube Channel 🎥", "Affiliate Marketing 💰",
    "Online Tutoring 📚", "Sell Handmade Products 🛍️", "Dropshipping 🚀",
    "Write an eBook 📖", "Invest in Stocks 📈", "Create an Online Course 🎓"
]

# Function to fetch side hustle ideas from FastAPI
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json().get("side_hustles", fallback_hustles)
            return random.choice(hustles)  # Randomize from API response
        else:
            return random.choice(fallback_hustles)  # Use fallback list
    except:
        return random.choice(fallback_hustles)  # Use fallback list if API fails

# Side Hustle Generator Section
st.subheader("💼 Side Hustle Ideas")
if st.button("🚀 Generate Hustle Idea"):
    idea = fetch_side_hustle()
    st.success(f"💡 Idea: {idea}")

# Fallback list for money quotes
fallback_quotes = [
    "Money is a tool. Use it wisely. 💡",
    "Invest in your dreams, they will pay off. 💰",
    "The harder you work, the luckier you get. 🍀",
    "Don't work for money, make money work for you. 📈",
    "Every penny saved is a penny earned. 💵",
    "Opportunities multiply as they are seized. 🚀",
    "Wealth consists not in having great possessions, but in having few wants. 💎"
]

# Function to fetch money quotes from FastAPI
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json().get("money_quotes", fallback_quotes)
            return random.choice(quotes)  # Randomize from API response
        else:
            return random.choice(fallback_quotes)  # Use fallback list
    except:
        return random.choice(fallback_quotes)  # Use fallback list if API fails

# Money Motivation Section
st.subheader("💡 Money-Making Motivation")
if st.button("🔥 Get Inspired"):
    quote = fetch_money_quote()
    st.info(f"📜 Quote: {quote}")
