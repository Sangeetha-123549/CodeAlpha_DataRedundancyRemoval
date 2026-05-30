from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Form submit handling (example logic)
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")

    if not name:
        return render_template("duplicate.html")

    # Simple duplicate check logic (demo)
    if name.lower() == "test":
        return render_template("duplicate.html")
    else:
        return render_template("success.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/duplicate")
def duplicate():
    return render_template("duplicate.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
