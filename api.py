from flask import Flask, request, abort
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():
    line_bot_api = LineBotApi('YOUR_CHANNEL_TOKEN')
    handler = WebhookHandler('YOUR_CHANNEL_SECRET_KEY')

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    event = json.loads(body)
    print(event)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    token = event['events'][0]['replyToken']
    if token == "00000000000000000000000000000000":
        pass
    else:
        line_bot_api.reply_message(token, TextSendMessage(
            text=event['events'][0]['message']['text']))
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
