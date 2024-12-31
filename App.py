from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Prank Website</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background-color: #ffcccb; /* Light Pink background */
                }
                .container {
                    text-align: center;
                    padding: 20px;
                    background-color: #ffffff; /* White background for UI */
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #666;
                }
            </style>
        </head>
        <body>

            <div class="container">
                <h1>YOU ARE A GAY</h1>
                <p>Realy You Are A Gay That's Why You Visit My Web!</p>
            </div>

        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)  # Public access
