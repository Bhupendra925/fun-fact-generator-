import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact():
    clear()
    
    # Heading
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

    # Fetching fun fact from API
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        fact = data['text']
        put_text(fact).style("color:blue; font-size:18px")
    else:
        put_text("Couldn't fetch a fact!").style("color:red; font-size:18px")

    # Add refresh button
    put_buttons(
        ['Another Fun Fact!'],
        onclick=lambda _: get_fun_fact()
    )

def main():
    get_fun_fact()
    hold()

if __name__ == "__main__":
    from pywebio.platform.tornado_http import start_server
    start_server(main, port=8080, debug=True)
