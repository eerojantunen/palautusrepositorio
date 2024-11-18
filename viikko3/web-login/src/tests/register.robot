*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  nalle
    Set Password  nalle123
    Set Password confirmation  nalle123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  na
    Set Password  nalle123
    Set Password confirmation  nalle123
    Submit Credentials
    Registration Should Fail

Register With Valid Username And Too Short Password
    Set Username  nalle
    Set Password  na
    Set Password confirmation  na
    Submit Credentials
    Registration Should Fail

Register With Valid Username And Invalid Password
    Set Username  nalle
    Set Password  nallepalle
    Set Password confirmation  nallepalle
    Submit Credentials
    Registration Should Fail
Register With Nonmatching Password And Password Confirmation
    Set Username  na
    Set Password  nalle123
    Set Password confirmation  nalle1234
    Submit Credentials
    Registration Should Fail

Register With Username That Is Already In Use
    Set Username  nalle
    Set Password  nalle123
    Set Password confirmation  nalle123
    Submit Credentials
    Go To Register Page
    Set Username    nalle
    Set Password    vaikeasalasana23
    Set Password Confirmation    vaikeasalasana23
    Submit Credentials
    Registration Should Fail


*** Keywords ***
#...
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Registration Should Fail
    Register Page Should Be Open