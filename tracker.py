from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Отримання IP-адреси користувача
    user_ip = request.remote_addr
    
    # HTML для відображення
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IP Tracker</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            .ip-container {
                font-size: 1.5em;
                color: #333;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the IP Tracker</h1>
        <div class="ip-container">
            Your IP address is: <strong>{{ user_ip }}</strong>
        </div>
    </body>
    </html>
    """
    # Відображення сторінки з IP-адресою
    return render_template_string(html_template, user_ip=user_ip)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
