from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    print("Current working dir:", os.getcwd())
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")

        if not name or name.lower() == "test":
            return render_template("duplicate.html")

        return render_template("success.html")

    except Exception as e:
        print("Error:", e)
        return "Internal Server Error", 500

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
