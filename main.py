from browser import document, alert, console


# show_alert
def show_alert(e):
    alert("Hello !")
    document["output-hello"].textContent = "Hello World !"


document['btn'].bind('click', show_alert)
