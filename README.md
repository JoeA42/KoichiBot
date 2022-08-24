# KoichiBot (workingProject).
## 1. Project Structure

---

### baseline documents/folders

> - bot.py: Change this ***file*** and add here the code for your bot.
> - resources: Add into this ***folder*** files to be used with your bot such as images, spreadsheets and etc. 
> - VERSION: Change the content of this ***file*** when updating the version of your bot. It is recommended to use versions in the format X.Y. E.g. 1.0, 1.1, 2.5, 3.10.

### baseline naming scheme
> ## ROOT FOLDER
> - ├── MANIFEST.in       <- This ***file*** defines the content of the package such as images.
> - ├── README.md         <- Simple README ***file*** for your bot project. 
> - ├── VERSION           <- This ***file*** defines the Bot package version.
> - ├── botPython         <- Main ***module*** for your Bot package.
> > ### botPython 
> > - ├── __init__.py 
> > - ├── __main__.py   <- Entrypoint for the ***module***. You don't need to bother with this file. 
> > - ├── bot.py        <- ***Module*** for your bot code. Here is where you will develop your bot. 
> >-   └── resources     <- ***Folder*** containing resources useful for the Bot. 
> - ├── build.bat         <- Batch script to generate the package 
> - ├── build.sh          <- Shell script to generate the package 
> - ├── requirements.txt  <- File describing the python dependencies for your Bot. 
> - └── setup.py          <- Setup file for the package.
> 

### :memo: [source + credit](https://botcity-dev.github.io/bot-python-template/project/)

---

