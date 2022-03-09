from collections import OrderedDict
from random import random
import requests

from bs4 import BeautifulSoup, FeatureNotFound
from requests import get


# this is for poshmark

otherKeywords = ['VINTAGE', 'VTG', 'PLAYER', 'TRAINING', 'FUTBOL', 'LA LIGA', 'PREMIER LEAGUE', 'STADIUM', 'LIGUE 1', '90S']
brandKeywords = ['FC', 'T90', 'total 90', 'opel', 'FLY EMIRATES', 'unicef', 'QATAR',  'dri-fit', 'climalite' 'AIG',   'ETIHAD', 'BWIN', 'RAKUTEN', 'PIRELLI', 'MACRON', 'KAPPA', 'AON']
clubKeywords = ['FCB', 'BARCELONA', 'BAYERN' 'ACM', 'MILAN' 'TORINO', 'RM', 'REAL MADRID', 'MANCHESTER', 'ARSENAL', 'DORTMUND', 'INTER', 'LAZIO', 'MUNCHEN', 'CITY', 'UTD', 'JUVENTUS', 'JUVE', 'PSG', 'PARIS', 'GERMAIN', 'ATM', 'MADRID', 'ATLETICO']
countryKeywords = ['NATIONAL', 'FIFA', 'WC', 'WORLD CUP', 'USA', 'ARGENTINA', 'DFB', 'GERMANY', 'SPAIN', 'ESPANA', 'ITALY', 'ITALIA', 'BELGIUM', 'PORTUGAL', 'BRAZIL', 'FRANCE', 'NETHERLANDS']
playerKeywords = ['MESSI', 'RONALDO', 'ROBBEN', 'PERSIE', 'SUAREZ', 'DEPAY', 'AGUERO', 'LUKAKU', 'FABREGAS', 'BECKHAM', 'VILLA', 'PULISIC', 'TOTTI', 'NEYMAR', 'BATISTUTA', 'GRIEZMANN', 'SAUL', 'SILVA']
shoeModels = {'MERCURIAL', 'NEMEZIZ', ''}

adidasJerseys = OrderedDict({
        'brand': 'adidas',
})
nikeJerseys = OrderedDict({
        'brand': 'nike',
})
pumaJerseys = OrderedDict({
        'brand': 'puma',
})

standardJerseys = OrderedDict({    
        'department': 'Mens',
        'category': 'Shirts',
        'subcategory': 'Jerseys',
        'sort': 'price_asc',
        'size': 'XL',
        'type': 'closet',
        'price': '15-35'
})

def SearchPoshmarkProducts(webpage, searchQuery, brand):    
    searchURL = webpage + "search?"
    searchURL += "query=" + searchQuery
    searchURL += "&department=" + standardJerseys['department']
    searchURL += "&size[]=" + standardJerseys['size']
    searchURL += "&price[]=" + standardJerseys['price']
    searchURL += "&brand[]=" + brand
    # searchURL += "&sub_category=" + standard_jerseys['subcategory']
    searchURL += "&sort_by=price_asc"
    # print(searchURL)
    # searchURL.append("&category=" + category)
    # searchURL.append("&type=listings&src=dir")
    page = requests.get(searchURL)
    # print(page)
    # print(page.content)
    return page
    # soup = BeautifulSoup(page.content, 'html.parser')
    
def SortedHTMLPage(page):
        # class: tile col-x12 col-l6 col-s8 p--2
        soup = BeautifulSoup(page.content, 'html.parser')
        tiles = soup.select('div.tile.col-x12.col-l6.col-s8.p--2')
        images = []

        # print("Number of tiles: " + str(len(tiles)))
        for tile in tiles:
            try:
                images += tile.select('img.ovf--h')[0].attrs['src']
            except:
                images += tile.select('img.ovf--h')[0].attrs['data-src']



webpage = "https://poshmark.com/"
query = "soccer jersey"
department = "men"

htmlPage = SearchPoshmarkProducts(webpage, query, 'adidas')
# displayPage = SortedHTMLPage(htmlPage)
SortedHTMLPage(htmlPage)

# page2 = requests.get(webpage)
# soup = BeautifulSoup(page2.content, 'html.parser')
# news_items = []
    



    
# strictness_pass = self._check_strictness(tile, arguments)
# if strict and strictness_pass:
#  There needs to be a better way to do this.
# p = Product(
# url=f"https://poshmark.com{tile.find('a').get('href')}")
# p._build_product_from_tile(tile, self.session)
# self.results.append(p)
# continue
# elif strict and not strictness_pass:
# continue
# elif not strict:
# p = Product(
# url=f"https://poshmark.com{tile.find('a').get('href')}")
# p._build_product_from_tile(tile, self.session)
# self.results.append(p)
# continue