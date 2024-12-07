from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_date():
    # Отримуємо поточну дату
    today = datetime.now().strftime('%Y-%m-%d')  # Формат дати: РРРР-ММ-ДД
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Календар</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }}
            .date {{
                font-size: 2em;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <h1>Сьогоднішня дата:</h1>
        <div class="date">{today}</div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)