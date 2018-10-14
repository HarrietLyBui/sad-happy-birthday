import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

from random import randint

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def singduet():
    r = randint(0, 2)
    if ( r == 0):
        welcome_msg = render_template('Singduetready')
    elif ( r == 1):
        welcome_msg = render_template('Singduetready1')
    elif ( r == 2):
        welcome_msg = render_template('Singduetready2')
    return question(welcome_msg)

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

@ask.intent('YesterdayFirst')
def YesterdayFirst():
    msg = render_template('Yesterday21')
    return question(msg)

@ask.intent('YesterdaySecond')
def YesterdaySecond():
    msg = render_template('Yesterday22')
    return question(msg)


@ask.intent('SomewhereOverTheRainBowND')
def SomewhereOverTheRainBowND():
    msg = render_template('SomeWhereOverTheRainBow21')
    return question(msg)

@ask.intent('SomewhereOverTheRainBowRD')
def SomewhereOverTheRainBow22():
    msg = render_template('SomeWhereOverTheRainBow22')
    return statement(msg)

@ask.intent("AMAZON.FallbackIntent")
def fallback():
    fallback_msg = render_template('fallback')
    return question(fallback_msg)

if __name__ == '__main__':
    app.run(debug=True,port=5050)