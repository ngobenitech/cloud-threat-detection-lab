from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud Threat Detection Dashboard Coming Soon"

if __name__ == "__main__":
    app.run(debug=True)
