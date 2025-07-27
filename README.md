# Simple Flask Chatbot

A simple web-based chatbot built with Flask and vanilla JavaScript. This chatbot provides friendly responses to user messages and features a clean, modern interface.

## Features

- 🤖 **Interactive Chat Interface**: Clean, modern chat UI with smooth animations
- 💬 **Smart Responses**: Contextual responses based on user input
- 📱 **Mobile-Friendly**: Responsive design that works on all devices
- ⚡ **Real-time Chat**: Instant message exchange with typing indicators
- 🎨 **Beautiful Design**: Gradient backgrounds and polished UI elements

## What the Bot Can Do

The chatbot recognizes several types of input and responds accordingly:

- **Greetings**: Says hello, hi, hey
- **Goodbyes**: Responds to bye, goodbye, farewell
- **Help Requests**: Provides assistance when asked
- **Weather Questions**: Gives playful responses about weather
- **Time Questions**: Responds to time-related queries
- **General Chat**: Engaging responses to keep the conversation going

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install flask flask-cors
   ```

3. **Run the application**:
   ```bash
   python run.py
   ```

4. **Open your browser** and go to: `http://localhost:8080`

## File Structure

```
├── app.py                 # Main Flask application with chatbot logic
├── run.py                 # Application runner script
├── templates/
│   └── index.html         # Frontend HTML with embedded CSS and JavaScript
└── README.md              # This file
```

## API Endpoints

### `GET /`
Returns the main chat interface (HTML page).

### `POST /chat`
Processes chat messages and returns bot responses.

**Request Body:**
```json
{
  "message": "Hello!"
}
```

**Response:**
```json
{
  "user_message": "Hello!",
  "bot_response": "Hi there! What can I do for you?"
}
```

## Customization

### Adding New Response Types

Edit the `RESPONSES` dictionary in `app.py` to add new categories:

```python
RESPONSES = {
    'new_category': [
        "Response 1",
        "Response 2",
        "Response 3"
    ]
}
```

Then add detection logic in the `get_bot_response()` function:

```python
if any(word in message for word in ['keyword1', 'keyword2']):
    return random.choice(RESPONSES['new_category'])
```

### Styling Changes

The CSS is embedded in `templates/index.html`. You can modify:
- Colors in the gradient backgrounds
- Font sizes and families
- Animation timing and effects
- Layout spacing and sizing

### Advanced Features

To extend the chatbot, consider adding:
- **Database Integration**: Store conversation history
- **AI/ML Integration**: Connect to OpenAI, Hugging Face, or other AI APIs
- **User Authentication**: Add login/signup functionality
- **File Uploads**: Allow users to share images or documents
- **Voice Chat**: Add speech-to-text and text-to-speech

## Example Conversations

```
User: Hello!
Bot: Hello! How can I help you today?

User: What's the weather like?
Bot: I don't have access to real weather data, but I hope it's nice where you are!

User: Can you help me?
Bot: I can help you with basic questions. Try asking me about the weather, time, or just chat!

User: Goodbye!
Bot: Goodbye! Have a great day!
```

## Development

### Running in Debug Mode

The application runs in debug mode by default, which means:
- Automatic reloading when code changes
- Detailed error messages
- Debug console available

### Port Configuration

To change the port, modify the `port` parameter in both `app.py` and `run.py`:

```python
app.run(host='0.0.0.0', port=YOUR_PORT, debug=True)
```

## Technical Details

- **Backend**: Flask (Python web framework)
- **Frontend**: Vanilla HTML, CSS, and JavaScript
- **CORS**: Enabled for cross-origin requests
- **Responsive Design**: Mobile-first approach with CSS media queries
- **Error Handling**: Graceful error handling for API requests

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for any improvements:
- Add new response categories
- Improve the UI/UX design
- Add new features
- Fix bugs or improve performance