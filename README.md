# KoichiBot (workingProject).
## 1. ποΈ Project Structure

---

### π§’ baseline documents/folders

> - π bot.py: Change this ***file*** and add here the code for your bot.
> - π resources: Add into this ***folder*** files to be used with your bot such as images, spreadsheets and etc. 
> - π VERSION: Change the content of this ***file*** when updating the version of your bot. It is recommended to use versions in the format X.Y. E.g. 1.0, 1.1, 2.5, 3.10.

### baseline naming scheme
> ## π³ ROOT FOLDER οΈ
> - πβββ MANIFEST.in       <- This ***file*** defines the content of the package such as images.
> - πβββ README.md         <- Simple README ***file*** for your bot project. 
> - πβββ VERSION           <- This ***file*** defines the Bot package version.
> - ποΈβββ botPython         <- Main ***module*** for your Bot package.
> > ## ποΈbotPython 
> > - πβββ __init__.py 
> > - πβββ __main__.py   <- Entrypoint for the ***module***. You don't need to bother with this file. 
> > - πβββ bot.py        <- ***Module*** for your bot code. Here is where you will develop your bot. 
> >-   πβββ resources     <- ***Folder*** containing resources useful for the Bot. 
> - πβββ build.bat         <- Batch script to generate the package 
> - πβββ build.sh          <- Shell script to generate the package 
> - πβββ requirements.txt  <- File describing the python dependencies for your Bot. 
> - πβββ setup.py          <- Setup file for the package.
> 

### :memo: [source + credit](https://botcity-dev.github.io/bot-python-template/project/)

---

## 2. π¨Design Patterns

---

> ### security + encryption
> - :ποΈ: [Base Pattern](https://refactoring.guru/design-patterns/proxy) to add a layer of security
> - :π§Ώ: [Base Implementation](https://rednafi.github.io/digressions/python/2020/06/16/python-proxy-pattern.html) implementation used as guide

