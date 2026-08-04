from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    return render_template("index.html", cpu=cpu, memory=memory)

if __name__ == "__main__":
    app.run(debug=True)