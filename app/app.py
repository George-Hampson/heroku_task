from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Get GitHub run number from environment variable, defaulting to 'Local'
    github_run_number = os.getenv('GITHUB_RUN_NUMBER', 'Local')
    commit_count = os.getenv('GITHUB_COMMIT_COUNT', '0')

    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Render the template 'index.html' and pass variables to it
    return render_template('index.html', version=github_run_number, 
                           commit_count=commit_count, current_date=current_date)


if __name__ == '__main__':


    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
