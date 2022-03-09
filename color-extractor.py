import requests
import pysnooper
from  icecream import ic

url = "https://color-extractor-for-apparel-2.p.rapidapi.com/colors"

querystring = {"image_url":"https://brand.assets.adidas.com/image/upload/f_auto,q_auto,fl_lossy/if_w_gt_1920,w_1920/enUS/Images/running-ss22-ultraboost-educate-catlp-masthead-large-d_tcm221-857738.jpg"}

headers = {
    'x-rapidapi-host': "color-extractor-for-apparel-2.p.rapidapi.com",
    'x-rapidapi-key': "6102ff5749mshaf469034e00fac1p11a5f8jsn77106cc2b77e"
    }

with pysnooper.snoop():
    response = requests.request("GET", url, headers=headers, params=querystring)

ic(response.text)