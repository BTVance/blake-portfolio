from flask import Flask, render_template
from markdown import markdown
from pathlib import Path

app = Flask(__name__)

def render_md(name):
    path = Path("content") / f"{name}.md"
    html = markdown(path.read_text(), extensions=["fenced_code", "tables"])
    return html

@app.route("/")
def home():
    return render_template("page.html", content=render_md("index"), title="Home")

@app.route("/projects")
def projects():
    return render_template("page.html", content=render_md("projects"), title="Projects")

@app.route("/about")
def about():
    return render_template("page.html", content=render_md("about"), title="About")

if __name__ == "__main__":
    app.run(debug=True)
