# web app
# flask, django(网页) 建立serve


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, AudioSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('LXFSCNEMDQ2crh1zWQwWO3rZjliuoMs5khVYyTOVAWea8qNuVun90gl1JxKFx5I6wF73IwYKd1wjJXTU9S4dldMFPnqddxWZdQg+bT6Qdfj2atH6ZdFVeJ1yqyM6xI3ZdAKf/RSahg3l67FDYTegNgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('69899e0ab3c12f53255a0f4b8a683551')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "Sorry, I don't what you are talking about. "

    if "voice" in msg:
        audio_message = AudioSendMessage(
            original_content_url='https://example.com/original.m4a',
            duration=240000
        )
        line_bot_api.reply_message(
            event.reply_token,
            audio_message)
        return

    if "hi" in msg:
        r = "Hello"
    elif "Hi" in msg:
        r = "Hello"
    elif msg == "Did you have a meal":
        r = "No"
    elif "book" in msg:
        r = " how many people, what time"
    elif "who" in msg:
        r = " Robt"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))




if __name__ == "__main__":
    app.run()


