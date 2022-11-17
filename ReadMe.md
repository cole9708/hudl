This project is to write a basic Selenium Test Framework using Python for Hudl Login Page

To install all requirements please  use the following:
pip install -r /path/to/requirements.txt

The Chrome Browser exe under the HudlAutomation folder needs to be in the system environment path on Windows. On Mac their path should be added to /etc/paths file

Test uses Chrome driver. Please install chromebrowser(works with version 107.0.5304.107)for the tests to run

please install python 3.10(pytest should be included within this )
pytest will also need to be installed (pip install pytest)
selenium will need to be installed (pip install selenium)

to run the tests navigate to the test folder and type command py.test

use "pytest -k" to run tests with a particular keyword expression

To generate a HTML report for a Selenium test, we have to install a plugin with the command: pip install pytest-html
to run tests and generate report (pytest --html=report.html)

usernames and passwords are kept in utilities/properties.ini and conftest function fixture -- as this is going to a public domain i have renamed it password which is incorrect

for API test please import requests (these will run as part of pytest also)
