import CarWallpapers.src.Helper.htmlContent as htmlContent
import CarWallpapers.src.ResponsePreparator.GoogleSearchResponsePreparator as googleSearchResponsePreparator

def getUrl(SEARCH_NAME):
     SEARCH_NAME +=" wallpaper 1080x1920"
     SEARCH_NAME = SEARCH_NAME.replace(' ','+')
     SEARCH_URL = "https://www.google.co.in/search?q={}&newwindow=1&sa=X&tbm=isch&tbo=u&source=univ&ved=0ahUKEwjImLTS_7bbAhWMr48KHSsoCDkQsAQIJw&biw=1301&bih=653".format(SEARCH_NAME)
     print(SEARCH_URL)
     return SEARCH_URL

def getWallpapers(KEY_WORD):
     url = getUrl(KEY_WORD)
     content = htmlContent.getSoupContent(url)
     return googleSearchResponsePreparator.getFormattedContent(content, KEY_WORD)
