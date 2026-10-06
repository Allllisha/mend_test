"""Mendスキャン練習用の小さなWebアプリ。

requirements.txt の古いライブラリを実際に import して使うことで、
Reachability（脆弱なコードに到達するか）の分析対象になるようにしている。
動かすことが目的ではなく、スキャンされることが目的。
"""

import jwt
import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

SECRET = "practice-secret"  # 練習用。実案件ではコードに書かない

PAGE = """
<h1>Mend scan practice</h1>
<p>status: {{ status }}</p>
"""


@app.route("/")
def index():
    url = request.args.get("url", "https://example.com")
    resp = requests.get(url, timeout=5)
    return render_template_string(PAGE, status=resp.status_code)


@app.route("/token")
def token():
    encoded = jwt.encode({"user": "arisa"}, SECRET, algorithm="HS256")
    return {"token": encoded}


if __name__ == "__main__":
    app.run(debug=True)
