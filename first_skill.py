import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

from random import randint

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def singalong():
    r = randint(0, 2)
    if ( r == 0):
        welcome_msg = render_template('Singalongready')
    elif ( r == 1):
        welcome_msg = render_template('Singalongready1')
    elif ( r == 2):
        welcome_msg = render_template('Singalongready2')
    return question(welcome_msg)

@ask.intent("HappyBirthdayIntent")
def HappyBirthday(name):
    msg = render_template('happy_birthday_full_cut')
    return statement(msg)


@ask.intent("NoIntent")
def next_round():
    r = randint(0, 2)
    if ( r == 0):
        msg = render_template('no_intent')
    elif ( r == 1):
        msg = render_template('no_intent1')
    elif ( r == 2):
        msg = render_template('no_intent2')
    return statement(msg)

@ask.intent("HappyBirthdayCutIntent")
def HappyBirthdayCut():
    msg = render_template('happy_birthday1')
    return statement(msg)

@ask.intent("Yesterday")
def Yesterday():
    msg = render_template('Yesterday1')
    return statement(msg)

@ask.intent("AMAZON.FallbackIntent")
def fallback():
    fallback_msg = render_template('fallback')
    return statement(fallback_msg)

@ask.intent('SomewhereOverTheRainBow')
def SomewhereOverTheRainBow():
    msg = render_template('SomeWhereOverTheRainBow')
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True,port=5000)