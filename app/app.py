from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    version = os.getenv('APP_VERSION', 'N/A')
    build_date = os.getenv('BUILD_DATE', 'N/A')
    return render_template('index.html', version=version, build_date=build_date)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
