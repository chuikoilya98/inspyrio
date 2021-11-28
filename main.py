from flask import Flask
from flask import request
from flask import send_file, send_from_directory
import os.path as pt
import os
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def receive_update():
    print(request.json)
    return {"ok": True}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

