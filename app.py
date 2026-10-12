from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("oficina.html")

if __name__ == "__main__":
    import os
    # Garante que o Flask use a porta fornecida pela nuvem ou a 5000 se for local
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

