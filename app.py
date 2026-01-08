from flask import Flask, render_template
from markdown import markdown
from pathlib import Path

app = Flask(__name__)

def render_md(filename):
    text = Path(f"content/{filename}").read_text()
    return markdown(text)

@app.route("/")
def home():
    content = render_md("index.md")
    return render_template("base.html", content=content)

@app.route("/projects")
def projects():
    content = render_md("projects.md")
    return render_template("base.html", content=content)

if __name__ == "__main__":
    app.run(debug=True)
