from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)


def get_git_shortlog():
    try:
        result = subprocess.run(['git', 'shortlog', '-s'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)
        shortlog = result.stdout.strip().split('\n')
        return [line.split('\t') for line in shortlog]
    except Exception as e:
        return []


@app.route('/')
def index():
    github_run_number = os.getenv('GITHUB_RUN_NUMBER', 'Local')
    commit_count = os.getenv('GITHUB_COMMIT_COUNT', 'Unknown')
    shortlog_data = get_git_shortlog()
    return render_template('index.html', version=github_run_number,
                           commit_count=commit_count,
                           shortlog_data=shortlog_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
