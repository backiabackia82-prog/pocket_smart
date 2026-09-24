import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def get_home_recommendations(budget, room_type):
    if not api_key:
        return "API Key is missing! Please check your .env file."
    
    try:
        # Initialize updated Gemini client
        client = genai.Client(api_key=api_key)
        prompt = f"Create a budget breakdown for a {room_type} interior within ₹{budget} INR. List items with estimated prices and store suggestions (IKEA, Amazon, Flipkart)."
        
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gemini API Error: {str(e)}"