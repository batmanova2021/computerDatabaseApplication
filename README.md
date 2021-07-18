# computerDatabaseApplication

This is example of an automation testing framework for **Computer Database Application** which is using
**Selenium WebDriver, Python, PyTest and Allure**. 
This framework is built using **POM** pattern. Currently only **Chrome** browser is supported.

**webdriver-manager** package is used to automatically download **chromedriver** 
for your corresponding Chrome browser installed and corresponding OS.

This project also contains **requirements.txt** with the list of 
all dependencies which will be picked up by PyCharm automatically.

**runConfigurations** for Smoke Tests, Regression Tests, All Tests and Allure Reports added to the project as files.
runConfigurations will be automatically picked up by PyCharm.
<hr>

**Requirements for Windows users:**
1. **Chrome** browser installed. https://www.google.com/chrome/
2. **Python** installed. https://www.python.org/downloads/
3. **PyCharm** Community Edition installed. https://www.jetbrains.com/pycharm/download/#section=windows
4. **Git** installed (optional). https://git-scm.com/downloads
5. **Allure** cli installed in order to run reports. (Requires **Java** to be installed)

**Allure installation** (required for reports):
1. Install **scoop** using instructions here https://scoop.sh/
2. Execute **scoop install allure** in the powershell. 
3. Download and extract JDK on your computer (JDK 11 was used for this project) https://www.oracle.com/java/technologies/javase-jdk11-downloads.html
4. Click on Windows icon and type env, click on "Edit the system environment variables".
5. Click on "Environment variables".
6. In System Variables click on "New" button.
7. Set Variable name: JAVA_HOME
8. Click on "Browse Directory" and locate your JDK folder (for example C:\annbat\Downloads\jdk-11.0.11)

*(Optional)* How to check if **Python** is installed:
1. Open cmd or powershell.
2. Execute the following command: **python --version**
3. You should see output similar to this [![image.png](https://i.postimg.cc/NF071Q3G/image.png)](https://postimg.cc/sQthzCfb)

<hr>

**Option 1** (if you are already using PyCharm):
1. Copy link to this repository.
2. Open PyCharm.
3. Click on "VCS" -> Enable VCS integration.
4. Make sure "Git" is selected as a VCS and press OK.
5. Click on "VCS" -> Git -> Clone.
6. Paste the link to the repository and click on "Clone" button.
7. Click on "Open in a new window" button.
8. Your computerDatabaseProject will open in a new window.
9. PyCharm will automatically detect requirements.txt and will ask you to import and install all dependencies, click on OK. Wait until all dependencies will be installed.
10. Click on run/debug Configurations and click on "Edit Configurations". Verify runConfigurations (Run Smoke Tests, Run Regression Tests etc are displayed).

**Option 2** (if you just installed PyCharm and running it for the first time):
1. Copy link to this repository.
2. Open PyCharm.
3. Click on New Project -> from VCS.
4. Paste the link and click on Create.
8. Your computerDatabaseProject will open in a new window.
9. PyCharm will automatically detect requirements.txt and will ask you to import and install all dependencies, click on OK. Wait until all dependencies will be installed.
10. Click on run/debug Configurations and click on "Edit Configurations". Verify runConfigurations (Run Smoke Tests, Run Regression Tests etc are displayed).

<hr>

**How to execute tests and run reports**

1. From "run/debug Configuration" dropdown select the job which you would like to run.
2. For example select **"Run Smoke Tests"** and press "Run" button or Shift + F10 [![image.png](https://i.postimg.cc/vTP63xJg/image.png)](https://postimg.cc/RJHF0hV4)
3. Google **Chrome** browser will open in a full screen and only Smoke Tests will be executed (tests with @pytest.mark.smoketest). [![image.png](https://i.postimg.cc/Kc9kXLW4/image.png)](https://postimg.cc/dDytr7wK)
4. You will see **Test Results** in PyCharm [![image.png](https://i.postimg.cc/nLkV4fbM/image.png)](https://postimg.cc/hJXqnwGq)
5. Select **"Run Allure Reports"** from "run/debug Configuration" dropdown. It is executing bat file with "allure serve reports" command. Optionally you can execute this command manually in terminal.[![image.png](https://i.postimg.cc/6QYw7Vnv/image.png)](https://postimg.cc/d7kgpyWs)
6. **Allure Reports** will open in a default browser [![image.png](https://i.postimg.cc/ht0hrdVS/image.png)](https://postimg.cc/FY79F1Pq)
7. You can check specific test and see the screenshot at the teardown [![image.png](https://i.postimg.cc/J7BnFgjY/image.png)](https://postimg.cc/dDwwk5HG) 

**(Optional):**
1. You can run "Generate HTML Report and Open" from "run/debug Configurations".
2. New folder "allure-reports" will be generated inside tests folder and allure will open report in a default browser.
3. index.html file will be generated which you can open in any browser. [![image.png](https://i.postimg.cc/Mp4PTvrY/image.png)](https://postimg.cc/G4FJghRB)




