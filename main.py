from browser import document, alert, console, ajax, window, html
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


# load file
def on_load(reader):
    document['file-text'].value = reader.target.result


def file_reader(e):
    file = document['file-upload'].files[0]
    reader = window.FileReader.new()
    reader.readAsText(file)
    reader.bind('load', on_load)


document['file-upload'].bind('input', file_reader)


# Animation
box = document['rotate-box']
angle = 10


def change(e):
    global angle
    box.style.transform = f"rotate({angle}deg)"
    angle += 10


document['rotate-btn'].bind('click', change)


# Local storage
storage = window.localStorage

if storage.getItem('item'):
    document['show-saved'].textContent = storage.getItem('item')


def add_item(e):
    get_item = document['get-item'].value
    storage.setItem('item', get_item)
    document['show-saved'].textContent = get_item
    alert('You added an object in local storage')


def remove_item(e):
    storage.removeItem('item')
    document['show-saved'].textContent = ""
    alert('You removed an object from local storage')


document['add-btn'].bind('click', add_item)
document['remove-btn'].bind('click', remove_item)


# draw with js and brython
def draw_br(e):
    height = document['height'].value
    width = document['width'].value
    color = document['color'].value
    window.draw_js(height, width, color)


document['draw-btn'].bind('click', draw_br)


# draw with js and brython

def draw_br_2(height, width, color):
    shap = document['shap2']
    shap.attrs['style'] = f"background-color: {color}"
    shap.width = width
    shap.height = height


window.draw_br_2 = draw_br_2
