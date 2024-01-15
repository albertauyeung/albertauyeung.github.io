---
layout: default
route: /2023/07/31/aws-lambda-telegram-whisper.html
date: 2023-07-31
tags:
  - aws
  - openai
  - telegrambot
  - python
  - ai
icon: dot
order: 20230731
visibility: hidden
---

# Creating a Telegram Bot for Speech Recogniton using AWS Lambda and OpenAI's Whisper Model

## Introduction

In this blog post, we explore a combination of two powerful technologies - 1) **AWS Lambda**, which gives us the ability to create an HTTP endpoint without worrying about setting up and maintaining a server, and 2) **OpenAI's [Whisper model](https://platform.openai.com/docs/guides/speech-to-text)**, which is a model capable of transcribing speech audio into the text in the language it is spoken as well as translated into English. The aim is to create a **Telegram bot** for speech recognition.

To follow the steps below to create the Telegram bot, we assume that:
1. You have a [Telegram account](https://telegram.org/), and have either the Telegram app on your phone or on your PC
2. You have an [Amazon AWS account](https://aws.amazon.com/)
3. You have an [OpenAI account](https://platform.openai.com/signup)

## Step 1: Create a New Telegram Bot

Create a [Telegram bot](https://core.telegram.org/bots) by interacting with [@BotFather](https://t.me/botfather). The process is straight-forward as you only need to follow the instructions given by the bot. At the end, you will be given a token to access the Telegram bot [HTTP API](https://core.telegram.org/bots/api). The token is in the format like the one below:

```
1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHI
```

Take note of this token as we will need to use it in the next step.

## Step 2: Create an AWS Lambda Function

On the AWS Management Console, navigate to Lambda page. You can follow the steps below to create a new Lambda function.

1. In the Lambda service dashboard, click on the "Create function" button. Select the "Author from scratch" option and give your function a name, such as "MyLambdaFunction".
2. You can choose the runtime environment based on the programming language you prefer. In this case, we choose "Python 3.10".
3. In the "Advanced settings" section, check the box of "Enable function URL" and choose "NONE" for "Auth type". This will allow the function to be publicly available via a URL.




### Setting the Credentials



## Step 3: Implement the Lambda Function

We will make use of the Telegram bot [HTTP API](https://core.telegram.org/bots/api) directly, instead of using Python packages such as [telepot](https://telepot.readthedocs.io/) or [python-telegram-bot](https://python-telegram-bot.org/)

For speech recognition and language translation, we will use OpenAI's Speech-to-Text API powered by the  and (optionally) ChatGPT. However, it should be easy to swap these with other third-party APIs out there.



## Step 4: Testing



## Advanced Topics


### Using Github Actions for Deployment


### Translation using GPT


## References


