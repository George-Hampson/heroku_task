from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    # Get GitHub commit count from environment variable, defaulting to '0'
    commit_count = os.getenv('GITHUB_COMMIT_COUNT', '0')

    # Render the template 'index.html' and pass variables to it
    return render_template('index.html', version=commit_count)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
