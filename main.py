from tkinter import *
import requests
from bs4 import BeautifulSoup


def get_html_data(url):
    html_data = requests.get(url)
    return html_data


def covid_data():
    # main url
    url = "https://www.worldometers.info/coronavirus/"

    # fetching html content using request.get method
    html = get_html_data(url)

    # parsing the html content using beautiful soup
    beautyHtml = BeautifulSoup(html.text, 'html.parser')

    # collecting all the div which has class name content-inner
    info_div = beautyHtml.find('div', attrs={'class': 'content-inner'})

    # creating a empty string to store the acctual data
    covidData = ""

    # gettting each data from info_div and storing into empty string
    for info in info_div.find_all('div', attrs={'id': 'maincounter-wrap'}):
        try:
            h1 = info.h1.get_text()
            number = info.span.get_text()
            covidData += h1 + " " + number + '\n'
        except AttributeError:
            pass

    return covidData


def get_country():
    name = country_name.get()
    # main url
    url = f"https://www.worldometers.info/coronavirus/country/{name}/"

    # fetching html content using request.get method
    html = requests.get(url)

    # parsing the html content using beautiful soup
    beautyHtml = BeautifulSoup(html.text, 'html.parser')

    # collecting all the div which has class name content-inner
    info_div = beautyHtml.find('div', attrs={'class': 'content-inner'})

    # creating a empty string to store the acctual data
    covidData = ""

    # gettting each data from info_div and storing into empty string
    for info in info_div.find_all('div', attrs={'id': 'maincounter-wrap'}):
        try:
            h1 = info.h1.get_text()
            number = info.span.get_text()
            covidData += h1 + " " + number + '\n'
        except AttributeError:
            pass

    heading['text'] = f"Coronavirus Cases In {name}"
    data['text'] = covidData


def reload():
    new_data = covid_data()
    heading['text'] = "World Wide Coronavirus Cases"
    country_name.set("")
    data['text'] = new_data


if __name__ == '__main__':
    root = Tk()
    root.title("Covid19 Cases (Live)")
    root.geometry("500x300")

    # country name title
    title = Label(root, text="Enter Your Country Name")
    title.grid(row=0, column=0, pady=5, padx=5)

    # country input section
    country_name = StringVar()
    country_entry = Entry(root, textvariable=country_name, font=24)
    country_entry.grid(row=2, column=0, pady=5, padx=5)

    # search btn
    search = Button(root, text="Search", font=5, background="red", fg="white", command=get_country)
    search.grid(row=2, column=1, pady=5)

    # main covid19 heading wordwide
    heading = Label(root, text="World Wide Coronavirus Cases", font=25, fg="red")
    heading.grid(row=3, column=0)

    # covid data

    data = Label(root, text=covid_data(), font=2)
    data.grid(row=4, column=0, pady=5, padx=20)

    # reload button
    reloadBtn = Button(root, text="Reload", font=5, background="skyblue", fg="white", command=reload)
    reloadBtn.grid(row=5, column=0)

    root.mainloop()