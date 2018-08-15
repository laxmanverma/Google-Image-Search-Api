import CarWallpapers.src.Helper.htmlContent as htmlContent
import CarWallpapers.src.ResponsePreparator.GoogleSearchResponsePreparator as googleSearchResponsePreparator
import CarWallpapers.src.Constants.Constants as constants

def getUrl(SEARCH_NAME):
     SEARCH_NAME +=" wallpaper 1080x1920"
     SEARCH_NAME = SEARCH_NAME.replace(' ','+')
     SEARCH_URL = constants.Constants.GOOGLE_SEARCH_API_URL.format(SEARCH_NAME)
     print(SEARCH_URL)
     return SEARCH_URL

def getWallpapers(KEY_WORD):
     url = getUrl(KEY_WORD)
     content = htmlContent.getSoupContent(url)
     return googleSearchResponsePreparator.getFormattedContent(content, KEY_WORD)
