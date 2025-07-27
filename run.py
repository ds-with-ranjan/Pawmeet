#!/usr/bin/env python3
"""
Simple Flask Chatbot Application
Run this script to start the chatbot web server.
"""

from app import app

if __name__ == '__main__':
    print("🤖 Starting Simple Chatbot Server...")
    print("📱 Open your browser and go to: http://localhost:8080")
    print("💬 Start chatting with the bot!")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    app.run(host='0.0.0.0', port=8080, debug=True)