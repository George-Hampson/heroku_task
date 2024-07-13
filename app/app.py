from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)


def get_commit_count():
    result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'],
                            stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()


def get_shortlog():
    result = subprocess.run(['git', 'shortlog', '-s'],
                            stdout=subprocess.PIPE)
    shortlog = result.stdout.decode('utf-8').strip().split('\n')
    shortlog_list = [line.split('\t') for line in shortlog if line]
    return shortlog_list


@app.route('/')
def index():
    commit_count = get_commit_count()
    shortlog_list = get_shortlog()

    return render_template('index.html', version=commit_count,
                           shortlog=shortlog_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
