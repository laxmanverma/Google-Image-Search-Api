import collections
import json

def getFormattedContent(content, KEY_WORD):
    data = []

    for i in range(int(99)):

        for child in content.find("div", {"data-ri": "{}".format(str(i))}).find("div", {"class": "rg_meta"}).children:
            data_content = json.loads(child)
            LINK = collections.OrderedDict()
            LINK['img_url'] = data_content["ou"]
            LINK['label'] = KEY_WORD
            LINK['source'] = "Goole Image Search"
            LINK['author'] = "Google"
            data.append(LINK)
            # print(LINK)
            # print(i)

    return data