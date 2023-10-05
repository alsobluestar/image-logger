from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/cat.png')
def show_image():
    remote_address = request.remote_addr
    image_url = "https://placekitten.com/g/200/300"
    image_html = f'<img src="{image_url}" alt="cat.png" />'
    print("REMOTE ADDRESS:", remote_address)
    return image_html


if __name__ == '__main__':
    app.run(debug=True)
