import webbrowser, requests
from selenium import webdriver


def downloadAndWriteToFile(url):
    res = requests.get(url)
    res.raise_for_status()  # checks if there was an API call error
    content = open('download.txt', 'wb')
    try:
        for chunk in res.iter_content():
            content.write(chunk)
    except:
        print('Error in writing to the file')
    finally:
        content.close()

def defaultBrowserHandling(url):
    webbrowser.open(url)

def seleniumBrowser(url):
    browser = webdriver.Firefox()
    browser.get(url)


downloadAndWriteToFile('https://automatetheboringstuff.com/files/rj.txt')
defaultBrowserHandling('https://www.google.com')
seleniumBrowser('https://www.google.com')


