from flask import Flask, render_template
import random
import logging

app = Flask(__name__)
events = []   # 👈 global event tracker

USER_NAME = "Bertram Russell"

# 👉 Setup logging (writes to file)
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def analyze_logs(logs):
    error_count = sum(1 for log in logs if "Error" in log)

    if error_count > 3:
        events.append("🚨 High failure detected")
        return "🚨 High failure rate detected"
    elif error_count > 0:
        return "⚠️ Some errors detected"
    else:
        return "✅ System healthy"

@app.route("/")
def home():
    logs = []
    status = "Healthy ✅"

    for _ in range(5):
        if random.random() > 0.7:
            msg = "Error: Something failed!"
            logging.error(msg)   # 👈 write real log
            logs.append(msg)
        else:
            msg = "App running fine"
            logging.info(msg)
            logs.append(msg)

    if any("Error" in log for log in logs):
        status = "Error ❌"

    # 👉 Read logs from file (REAL logs)
    try:
        with open("app.log", "r") as f:
            log_lines = f.readlines()[-20:]  # last 20 logs
    except:
        log_lines = []

    ai_result = analyze_logs(log_lines)

    return render_template(
        "index.html",
        name=USER_NAME,
        status=status,
        ai_result=ai_result,
        logs=log_lines
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)