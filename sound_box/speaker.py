from flask import Flask, request, render_template
from pynput.mouse import Button, Controller  
from selenium import webdriver
import time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        search = request.form.get('textview')
        url = get_url(search)
        iframe = url.replace('watch?v=', 'embed/')

        return render_template('index.html', iframe=iframe)


def get_url(text_search):
    driver = webdriver.Chrome()
    driver.get('https://youtube.com')

    searchbox = driver.find_element_by_xpath('//*[@id="search"]')
    searchbox.send_keys(text_search)

    search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
    search_button.click()

    time.sleep(3)
    mouse = Controller()
    mouse.position = (234.50390625, 358.1171875)
    time.sleep(2)
    mouse.click(Button.left, 1)

    url = driver.current_url
    driver.close()

    return url


if __name__ == '__main__':
    app.run(debug=True)


