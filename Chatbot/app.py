import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# ✅ Set your API Key here
GOOGLE_API_KEY = "AIzaSyA_g35-Ao1I-UKPxnMnl6RnkAIraW249N4"  # 🔹 Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate AI response
def get_gemini_response(user_message):
    model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model
    response = model.generate_content(user_message)

    if response and hasattr(response, "text"):
        return response.text.strip().replace("\n", "<br>")  # Format output
    else:
        return "Sorry, I couldn't generate a response."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    bot_reply = get_gemini_response(user_input)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
