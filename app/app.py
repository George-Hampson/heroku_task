from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    # Get the version from environment variable
    version = os.getenv('VERSION', '0.1.0')

    # Render the template 'index.html' and pass variables to it
    return render_template('index.html', version=version)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
