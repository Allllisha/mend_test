"""Mendスキャン練習用の小さなWebアプリ。

requirements.txt の古いライブラリを実際に import して使うことで、
Reachability（脆弱なコードに到達するか）の分析対象になるようにしている。
動かすことが目的ではなく、スキャンされることが目的。

SAST修正練習（2026-10-08）：
- SSRF: ユーザー入力のURLを直接fetchせず、許可リストのキー参照方式に変更
- ハードコードされたシークレット: 環境変数から読み込む方式に変更
"""

import os

import jwt
import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

SECRET = os.environ.get("APP_SECRET", "")

PAGE = """
<h1>Mend scan practice</h1>
<p>status: {{ status }}</p>
"""

# SSRF対策：ユーザーには「キー」だけ選ばせ、URLはサーバー側の固定リストから引く
ALLOWED_TARGETS = {
    "example": "https://example.com",
    "docs": "https://docs.mend.io",
}


@app.route("/")
def index():
    target = request.args.get("target", "example")
    url = ALLOWED_TARGETS.get(target)
    if url is None:
        return {"error": "target not allowed"}, 400
    resp = requests.get(url, timeout=5)
    return render_template_string(PAGE, status=resp.status_code)


@app.route("/token")
def token():
    encoded = jwt.encode({"user": "arisa"}, SECRET, algorithm="HS256")
    return {"token": encoded}


if __name__ == "__main__":
    app.run(debug=True)
