from browser import document, alert, console, ajax
from browser.template import Template


# show_alert
def show_alert(e):
    alert("Hello !")
    document["output-hello"].textContent = "Hello World !"


document['btn'].bind('click', show_alert)


# I/O in the same time
def show_output(e):
    console.log(e.target.value)
    document['output'].textContent = e.target.value


document['text'].bind('input', show_output)


# Template Variable
Template(document['hi-to']).render(name="Mohammad")
Template(document['sum']).render(a=10, b=5)


# Ajax call
url = "https://api.chucknorris.io/jokes/random"


def on_complete(req):
    import json
    data = json.loads(req.responseText)
    joke = data['value']
    document['show-joke'].textContent = joke


def get_joke(e):
    req = ajax.ajax()
    req.open('GET', url, True)
    req.send()
    document['show-joke'].textContent = "LOADING....."
    req.bind('complete', on_complete)


document['joke-btn'].bind('click', get_joke)
