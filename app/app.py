from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)


def get_git_shortlog():
    try:
        result = subprocess.run(
            ['git', 'shortlog', '-s'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except FileNotFoundError:
        return "Git not found"


@app.route('/')
def index():
    # Get GitHub run number from environment variable, defaulting to 'Local'
    github_run_number = os.getenv('GITHUB_RUN_NUMBER', 'Local')

    # Get Git shortlog
    git_shortlog = get_git_shortlog()

    # Render the template 'index.html' and pass variables to it
    return render_template(
        'index.html',
        version=github_run_number,
        git_shortlog=git_shortlog
    )


if __name__ == '__main__':
    # Increment version
    with open('VERSION', 'r+') as f:
        version = f.read().strip()
        major, minor, patch = map(int, version.split('.'))
        patch += 1
        new_version = f'{major}.{minor}.{patch}'
        f.seek(0)
        f.write(new_version)
        f.truncate()

    # Build and push Docker image
    subprocess.run(
        ['docker', 'build', '-t', f'flaskapp:{new_version}', '.'],
        check=True
    )
    subprocess.run(
        [
            'docker', 'tag', f'flaskapp:{new_version}',
            'registry.heroku.com/YOUR_HEROKU_APP_NAME/web'
        ],
        check=True
    )
    subprocess.run(
        [
            'docker', 'push',
            'registry.heroku.com/YOUR_HEROKU_APP_NAME/web'
        ],
        check=True
    )

    # Deploy to Heroku
    subprocess.run(
        [
            'heroku', 'container:release', 'web',
            '--app', 'YOUR_HEROKU_APP_NAME'
        ],
        check=True
    )

    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
