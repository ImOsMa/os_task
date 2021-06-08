*** Settings ***
Library    Conf.py
Library    SeleniumLibrary
Library    ${CURDIR}${/}\\apps\\pages\\login_page_actions.py
Variables    ${CURDIR}${/}..\\variables\\credential_variables.py
*** Variables ***


*** Keywords ***

Open Main Page
    [Documentation]    Keyword open login page of the site
    Log To Console    The process of opening the site
    Setup Action

Close Browser And Main Page
    [Documentation]    Keyword close browser
    Log To Console    The process of closing browser
    Teardown Action



