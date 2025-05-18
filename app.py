from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from github_summarizer import github_summarizer, Summary, summary_parser
from output_parsers import GitHubProjectsOutput

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    projects = []

    if request.method == 'POST':
        full_name = request.form.get('fullname')

        if full_name:
            try:
                # Call your function to get summary data (replace this with your actual function)
                summary_output: GitHubProjectsOutput = github_summarizer(full_name)
                projects = summary_output.projects
            except Exception as e:
                print(f"Error: {e}")

    return render_template("index.html", projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
