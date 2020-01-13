import sys
from pymongo import MongoClient
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

client = MongoClient('mongodb://localhost:27017')
##############################################################################################
########################### Scraped Items ####################################################
##############################################################################################

# UNIVERSAL AUDIO APOLLO TWIN X DUO THUNDERBOLT 3 INTERFACE
url = 'https://www.musiciansfriend.com/pro-audio/universal-audio-apollo-twin-x-duo-thunderbolt-3-audio-interface/l69012000000000?rNtt=apollo&index=1'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
title = page_soup.find('title')
containers = page_soup.find('span', 'price-wrap')
clean = containers.text.strip()
cleanTitle = title.text.strip()
displayRes = 'The ' + cleanTitle + ' is going to cost ' + str(clean)
print(cleanTitle)
print('The ' + cleanTitle + ' is going to cost ' + str(clean))


# MARSHALL JVM SERIES JVM410H 100W TUBE GUITAR AMPLIFIER
urlAmp = 'https://www.musiciansfriend.com/amplifiers-effects/marshall-jvm-series-jvm410h-100w-tube-guitar-amp-head'
reqAmp = Request(urlAmp, headers={'User-Agent': 'Mozilla/5.0'})
webpageAmp = urlopen(reqAmp).read()
page_soup_Amp = soup(webpageAmp, "html.parser")
titleAmp = page_soup_Amp.find('title')
containersAmp = page_soup_Amp.find('span', 'price-wrap')
cleanAmp = containersAmp.text.strip()
cleanTitleAmp = titleAmp.text.strip()
displayResAmp = 'The ' + cleanTitleAmp + ' is going to cost ' + str(cleanAmp)
print(cleanTitleAmp)
print('The ' + cleanTitleAmp + ' will cost ' + cleanAmp)


# Apple Watch
urlWatch = 'https://www.amazon.com/Apple-Watch-GPS-40mm-Aluminum/dp/B07XR5TRSZ/ref=sr_1_2_sspa?keywords=apple+watch&qid=1578007379&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQ0FGVjRKQzY1TDBTJmVuY3J5cHRlZElkPUEwOTU0ODg4M0lBT1ZFVkZMSlQ1MyZlbmNyeXB0ZWRBZElkPUEwMDg1NjAwMU5aSVFQNEtORTc0MSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
reqWatch = Request(urlWatch, headers={'User-Agent': 'Mozilla/5.0'})
webpageWatch = urlopen(reqWatch).read()
page_soup_Watch = soup(webpageWatch, "html.parser")
titleWatch = page_soup_Watch.find('title')
containersWatch = page_soup_Watch.find('span', 'priceBlockBuyingPriceString')
cleanWatch = containersWatch.text.strip()
cleanTitleWatch = titleWatch.text.strip()
displayResWatch = 'The ' + cleanTitleWatch + \
    ' is going to cost ' + str(cleanWatch)
print(cleanTitleWatch)
print('The ' + cleanTitleWatch + ' in question will cost ' + cleanWatch)

##############################################################################################
########################### Interface ########################################################
##############################################################################################


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text=displayRes))
        self.webscra1 = TextInput(multiline=False)
        self.inside.add_widget(self.webscra1)

        self.inside.add_widget(Label(text=displayResAmp))
        self.webscra2 = TextInput(multiline=False)
        self.inside.add_widget(self.webscra2)

        self.inside.add_widget(Label(text=displayResWatch))
        self.webscra3 = TextInput(multiline=False)
        self.inside.add_widget(self.webscra3)

        self.add_widget(self.inside)

self.submit = Button(text="Submit", font_size=40)
self.submit.bind(on_press=self.pressed)
self.add_widget(self.submit)

def pressed(self, instance):
    item_one = self.webscra1.text
    item_two = self.webscra2.text
    item_three = self.webscra3.text

    print(item_one, item_two, item_three)
    self.webscra1.text = ""
    self.webscra2.text = ""
    self.webscra3.text = ""


class ScraperApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    ScraperApp().run()
##############################################################################
########################## Database ##########################################
##############################################################################
