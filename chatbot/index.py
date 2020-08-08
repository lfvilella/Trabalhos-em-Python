"""Chatbot Tutorial:

https://blog.mbeck.com.br/tutorial-chatbot-facebook-messenger-cd59d8e700d6

Here a bot returns how many letters have in your input.
"""

import os

import requests
import traceback
import json

from flask import Flask, request


token = os.environ.get("FB_ACCESS_TOKEN")
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        try:
            data = json.loads(request.data.decode())
            text = data["entry"][0]["messaging"][0]["message"]["text"]
            len_text = len(text)
            sender = data["entry"][0]["messaging"][0]["sender"]["id"]
            payload = {
                "recipient": {"id": sender},
                "message": {"text": f"Your input have {len_text} letters."},
            }
            requests.post(
                "https://graph.facebook.com/v2.6/me/messages/?access_token="
                + token,
                json=payload,
            )
        except Exception:
            print(traceback.format_exc())

    elif request.method == "GET":  # Para a verificação inicial
        if request.args.get("hub.verify_token") == os.environ.get(
            "FB_VERIFY_TOKEN"
        ):
            return request.args.get("hub.challenge")
        return "Wrong Verify Token"

    return "Nothing"


if __name__ == "__main__":
    app.run(debug=True)
