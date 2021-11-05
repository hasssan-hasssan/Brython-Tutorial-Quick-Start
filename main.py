from browser import document, alert, console


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
