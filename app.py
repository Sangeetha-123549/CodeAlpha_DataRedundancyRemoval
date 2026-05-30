from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# Home page
@app.route("/")
def home():
    print("Current working dir:", os.getcwd())
    print("Templates folder content:", os.listdir("templates"))
    return render_template("index.html")

# Form submit route (if you use form)
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")

        if not name:
            return render_template("duplicate.html")

        # Simple duplicate logic (demo)
        if name.lower() == "test":
            return render_template("duplicate.html")

        return render_template("success.html")

    except Exception as e:
        print("Error:", e)
        return "Internal Server Error"

# Optional routes
@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/duplicate")
def duplicate():
    return render_template("duplicate.html")


# IMPORTANT for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
