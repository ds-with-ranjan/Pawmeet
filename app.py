from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random
import re

app = Flask(__name__)
CORS(app)

# Simple chatbot responses
RESPONSES = {
    'greeting': [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Hey! Nice to meet you!",
        "Hello! I'm here to assist you."
    ],
    'goodbye': [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! Take care!",
        "Farewell! Come back anytime!"
    ],
    'help': [
        "I can help you with basic questions. Try asking me about the weather, time, or just chat!",
        "I'm a simple chatbot. You can ask me anything and I'll do my best to respond!",
        "Feel free to ask me questions or just have a conversation!"
    ],
    'weather': [
        "I don't have access to real weather data, but I hope it's nice where you are!",
        "The weather is always perfect for chatting! ☀️",
        "I wish I could check the weather for you, but I'm just a simple chatbot!"
    ],
    'time': [
        "I don't have access to the current time, but time flies when you're having fun!",
        "Time is relative! But right now is always a good time to chat.",
        "I can't tell time, but I can tell you're awesome!"
    ],
    'default': [
        "That's interesting! Tell me more.",
        "I see! What else would you like to talk about?",
        "Hmm, that's a good point. What do you think about it?",
        "I'm not sure I understand completely, but I'm listening!",
        "That's cool! Can you tell me more about that?",
        "Interesting! I'd love to hear your thoughts on that."
    ]
}

def get_bot_response(user_message):
    """Generate a chatbot response based on user input."""
    message = user_message.lower().strip()
    
    # Check for greetings
    if any(word in message for word in ['hello', 'hi', 'hey', 'greetings']):
        return random.choice(RESPONSES['greeting'])
    
    # Check for goodbyes
    if any(word in message for word in ['bye', 'goodbye', 'see you', 'farewell']):
        return random.choice(RESPONSES['goodbye'])
    
    # Check for help requests
    if any(word in message for word in ['help', 'assist', 'support']):
        return random.choice(RESPONSES['help'])
    
    # Check for weather
    if any(word in message for word in ['weather', 'temperature', 'rain', 'sunny']):
        return random.choice(RESPONSES['weather'])
    
    # Check for time
    if any(word in message for word in ['time', 'clock', 'hour', 'minute']):
        return random.choice(RESPONSES['time'])
    
    # Check for questions about the bot
    if any(phrase in message for phrase in ['who are you', 'what are you', 'your name']):
        return "I'm a friendly chatbot! I'm here to chat with you and answer simple questions."
    
    # Default response
    return random.choice(RESPONSES['default'])

@app.route('/')
def index():
    """Main page route."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Chat endpoint to process user messages."""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message.strip():
            return jsonify({'error': 'Empty message'}), 400
        
        bot_response = get_bot_response(user_message)
        
        return jsonify({
            'user_message': user_message,
            'bot_response': bot_response
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)