# computerDatabaseApplication

This is example of an automation testing framework for **Computer Database Application** which is using
**Selenium WebDriver, Python, PyTest and Allure**. 
This framework is built using **POM** pattern. Currently only **Chrome** browser is supported.

**webdriver-manager** package is used to automatically download **chromedriver** 
for your corresponding Chrome browser installed and corresponding OS.

This project also contains **requirements.txt** with the list of 
all dependencies which will be picked up by PyCharm automatically.

**runConfigurations** for Smoke Tests, Regression Tests, All Tests and Allure Reports added to the project as files.

<hr>

**Requirements for Windows users:**
1. **Chrome** browser installed. https://www.google.com/chrome/
2. **Python** installed. https://www.python.org/downloads/
3. **PyCharm** Community Edition installed. https://www.jetbrains.com/pycharm/download/#section=windows
4. **Git** installed (optional). https://git-scm.com/downloads
5. **Allure** cli installed in order to run reports. (Requires **Java** to be installed)

**Allure installation** (required for reports):
1. Install **scoop** https://scoop.sh/
2. Execute **scoop install allure** in the powershell 
3. Download and install JDK 

*(Optional)* How to check if **Python** is installed:
1. Open cmd or powershell 
2. Execute the following command: **python --version**
3. You should see output similar to this [![image.png](https://i.postimg.cc/NF071Q3G/image.png)](https://postimg.cc/sQthzCfb)

<hr>



