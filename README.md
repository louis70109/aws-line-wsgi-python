# AWS-LINE-WSGI-PYTHON

Welcome here!

This is [aws-line-echo-bot](https://github.com/louis70109/aws-line-echo-bot) upgrade version,
using serverless to build a LINE echo bot with WSGI.

> Taiwan user can follow [my topic](https://nijialin.com/2019/11/02/%E7%BA%8C%E7%AF%87-%E2%80%94-serverless-WSGI-flask-chatbot-%E7%9A%84%E9%96%8B%E7%99%BC%E6%8C%87%E5%8D%97/)

# Bebore you start

1. LINE developer account
2. [LINE Message API](https://developers.line.biz/en/docs/messaging-api/getting-started/)

# Quick Start

1. Install serverless via npm

```bash=
$ npm install -g serverless
```

2. Setup your **AWS** ceritficate

```bash=
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
```

3. Clone this project

```bash=
$ serverless install --url https://github.com/louis70109/aws-line-wsgi-python -n <YOUR_FILE_NAME>
$ cd <YOUR_FILE_NAME>/
```

4. Insert you LINE bot secret & key

```python=
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')
```

5. Deploy the webhhok function

```bash=
npm install
pip install -r requirements.txt
serverless deploy
```

6. You may have like this domain

![](https://i.imgur.com/XCiTkb7.png)

7.  Copy and Paste domain in your LINE bot account

![](https://i.imgur.com/nXFcseH.png)

8. Now you can test you chatbot, have fun!
![Echo bot](https://i.imgur.com/Tn1XS13.png)

# Author

Create by NiJia

# License

The project is available as open source under the terms of the MIT License.
