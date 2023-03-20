from sel_translator import SelTranslator
import glob

maindir = glob.glob("*.html")
web = SelTranslator(driverPath="C:\\chromedriver.exe", sourceL="en", targetL="hi", waitTime=15, savePath="translated")
web.saveHtmlBulk(maindir)