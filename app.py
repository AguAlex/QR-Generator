from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

# Main Html Page
@app.route('/')
def index():
    #Takes an arg from the url
    qr_image = request.args.get('qr_image', None)
    return render_template('index.html', qr_image=qr_image)

# Route for generating qr
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    link = request.form['link']
    
    # Generate QR Code and save it
    img = qrcode.make(link)
    file_path = 'static/qrcode.png'
    img.save(file_path)

    return render_template('index.html', qr_image=file_path)

# Route for downloading qr
@app.route('/download_qr')
def download_qr():
    file_path = 'static/qrcode.png'
    return send_file(file_path, as_attachment=True, download_name='qrcode.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
