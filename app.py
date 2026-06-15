from flask import Flask, request, jsonify, render_template
import whisper
import tempfile

app = Flask(__name__)
model = whisper.load_model("tiny.en")  # Only use English tiny model

@app.route("/")
def index():
    return render_template("index.html")  # Serve your HTML page here

@app.route("/transcribe", methods=["POST"])
def transcribe():
    file = request.files["audio"]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        file.save(tmp.name)
        result = model.transcribe(tmp.name)
        return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

