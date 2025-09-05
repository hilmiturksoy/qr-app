from flask import Flask, render_template, request, send_file
import qrcode
import io, base64

app = Flask(__name__)

# Global değişken (son üretilen QR kodu tutmak için)
last_qr_image = None

@app.route("/", methods=["GET", "POST"])
def index():
    global last_qr_image
    qr_code = None
    if request.method == "POST":
        text = request.form["text"]
        img = qrcode.make(text)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        last_qr_image = buffer.getvalue()  # indirilebilir dosya için sakla
        qr_code = base64.b64encode(last_qr_image).decode("utf-8")

    return render_template("index.html", qr_code=qr_code)

@app.route("/download")
def download_qr():
    global last_qr_image
    if last_qr_image:
        return send_file(
            io.BytesIO(last_qr_image),
            mimetype="image/png",
            as_attachment=True,
            download_name="qrcode.png"
        )
    return "No QR code generated yet.", 404

if __name__ == "__main__":
    app.run(debug=True)
