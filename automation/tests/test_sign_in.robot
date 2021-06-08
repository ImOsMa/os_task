*** Settings ***
Resource    ${CURDIR}${/}..\\robottools\\keywords.robot
Library    ${CURDIR}${/}..frmk\\apps\\pages\\login_page_actions.py
Variables  ${CURDIR}${/}..frmk\\variables\\credential_variables.py
Suite Setup    Open Main Page
*** Test Cases ***

Log In With Correct Credentials
    [Documentation]    The test case checs log in with correct credentials
    Sign In    username=CORRECT_USERNAME   password=CORRECT_PASSWORD   desription=CORRECT_USERNAME_DESCRIPTION
    [Teardown]    Run Keyword    Close Browser And Main Page

Log In With Short Password
    [Documentation]    The test case checs log in with short password
    ${data_type}    'short_password'
    Sign In    username=CORRECT_USERNAME   password=SHORT_CRED   desription=CORRECT_USERNAME_DESCRIPTION    data_type=${data_type}
    [Teardown]    Run Keyword    Close Browser And Main Page

Log In With Short Username
    [Documentation]    The test case checs log in with short username
    ${data_type}    'short_username'
    Sign In    username=SHORT_CRED   password=CORRECT_PASSWORD   desription=CORRECT_USERNAME_DESCRIPTION    data_type=${data_type}
    [Teardown]    Run Keyword    Close Browser And Main Page

Log In With Empty Username
    [Documentation]    The test case checs log in with empty username
    ${data_type}    'empty_username'
    Sign In    username=' '   password=CORRECT_PASSWORD   desription=CORRECT_USERNAME_DESCRIPTION    data_type=${data_type}
    [Teardown]    Run Keyword    Close Browser And Main Page

Log In With Empty Password
    [Documentation]    The test case checs log in with empty password
    ${data_type}    'empty_password'
    Sign In    username=CORRECT_USERNAME   password=' '   desription=CORRECT_USERNAME_DESCRIPTION    data_type=${data_type}
    [Teardown]    Run Keyword    Close Browser And Main Page