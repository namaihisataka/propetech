from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import json

def generatePropListJson(keyward):

    keyward = parse.quote(keyward)
    resource = request.urlopen('https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=030&bs=011&fw=' + keyward +"&pc=100")
    html = resource.read().decode()

    dottables= sp.select('.dottable--cassette .dottable-line dl')
    # print(dottables)
    locations = []
    prices = []
    names = []
    for n, item in enumerate(dottables):
        if item.dt.string == "所在地":
            locations.append(item.dd.string)
        if item.dt.string == "販売価格":
            prices.append(item.dd.span.string)
        if item.dt.string == "物件名":
            names.append(item.dd.string)
    prop_dict = {}
    print(len(prices), len(names), len(locations))
    for name, location, price in zip(names, locations, prices):
        prop_dict[name] = [location, price]
    print(prop_dict)
    return json.dumps(prop_dict)
import sys
if __name__ == "__main__ ":
    args = sys.argv
    generatePropListJson(args[1])
