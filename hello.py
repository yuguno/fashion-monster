from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from secret_key import ACCSESS_TOKEN, SECRET_KEY

app = Flask(__name__)

line_bot_api = LineBotApi('VXNRAqHeh3B/E2LoCK1LnNzmYgHXxXJLGBtBJE1r9NdY76HIhvJen/9xc/wT68QfLhi/KXQNmIAGw3EWqPoZQxg30sxWp+UYzVkT9+YfKBpS7ujJvnLpaNcPT5wR4d17of6uUadb/IgJM/oHIVhDTQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('430d63079d498a359bd759a95713831f')


@app.route("/")
def route_dir():
    return """Hello world""""


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
