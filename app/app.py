from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)


def get_commit_count():
    try:
        result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout.decode('utf-8').strip()
        else:
            print("Error in get_commit_count: ", result.stderr.decode('utf-8'))
            return "0"
    except Exception as e:
        print("Exception in get_commit_count: ", e)
        return "0"


def get_shortlog():
    try:
        result = subprocess.run(['git', 'shortlog', '-s'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        if result.returncode == 0:
            shortlog = result.stdout.decode('utf-8').strip().split('\n')
            shortlog_list = [line.split('\t') for line in shortlog if line]
            print("Shortlog List: ", shortlog_list)  # Debugging statement
            return shortlog_list
        else:
            print("Error in get_shortlog: ", result.stderr.decode('utf-8'))
            return []
    except Exception as e:
        print("Exception in get_shortlog: ", e)
        return []


@app.route('/')
def index():
    commit_count = get_commit_count()
    shortlog_list = get_shortlog()
    print("Commit Count: ", commit_count)  # Debugging statement
    print("Shortlog List at Index: ", shortlog_list)  # Debugging statement
    return render_template('index.html', version=commit_count,
                           shortlog=shortlog_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
