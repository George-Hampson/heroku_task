from flask import Flask, render_template
import os

app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def index():
    # Get GitHub run number from environment variable, defaulting to 'Local'
    github_run_number = os.getenv('GITHUB_RUN_NUMBER', 'Local')

    # Render the template 'index.html' and pass variables to it
    return render_template('index.html', version=github_run_number)

if __name__ == '__main__':
    # Use os.environ.get('PORT') to dynamically set the port from Heroku's environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
