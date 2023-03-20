from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, os


class SelTranslator:
    def __init__(self, driverPath=None, binaryLocation=None, sourceL="en", targetL="tr", waitTime=15, savePath=""):
        self.driverPath = driverPath
        self.binaryLocation = binaryLocation
        self.sourceL = sourceL
        self.targetL = targetL
        self.waitTime = waitTime
        self.savePath = savePath
        self.opt = Options()
        if driverPath is None:
            print("Driver path is not exists.")
            exit()
        if binaryLocation is not None:
            self.opt.binary_location(self.binaryLocation)
        if not os.path.exists(savePath):
            os.mkdir(savePath)
        prefs = {
            "translate_whitelists": {self.sourceL: self.targetL},
            "translate": {"enabled": "true"}
        }
        self.opt.add_experimental_option("prefs", prefs)
        self.count = 1
        self.browser = webdriver.Chrome(options=self.opt, executable_path=self.driverPath)
        self.browser.maximize_window()
        time.sleep(self.waitTime)

    def getHtml(self, html):
        self.weburl = html
        self.browser.get(self.weburl)
        time.sleep(2)
        height = self.browser.execute_script("return document.body.scrollHeight")
        for i in range(height):
            self.browser.execute_script('window.scrollBy(0,20)')
            height = self.browser.execute_script("return document.body.scrollHeight")
        time.sleep(2)

    def saveHtmlBulk(self, htmls):
        for i in htmls:
            i = i.replace("\\", "/")
            self.getHtml(i)
            self.savePage()
            self.count += 1

    def savePage(self):
        with open(f"{self.savePath}/{self.weburl.split('/')[-1]}-{self.count}-translated.html", "w",
                  encoding="utf-8") as p:
            p.write(self.browser.page_source)
