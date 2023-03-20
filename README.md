# sel_translator
Translate website and local html files with sel_translator

# Installation
```
python setup.py
```

# Usage
```
from sel_translator import SelTranslator
import glob
maindir = glob.glob("*.html")
web = SelTranslator(driverPath="C:\\chromedriver.exe", sourceL="en", targetL="tr", waitTime=15, savePath="translated")
web.saveHtmlBulk(maindir)
```
Or single website
```
from sel_translator import SelTranslator
web = SelTranslator(driverPath="C:\\chromedriver.exe", sourceL="en", targetL="tr", waitTime=15, savePath="translated")
web.getHtml("index.htm-1-translated.html")
web.savePage()
```
# MIT
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
