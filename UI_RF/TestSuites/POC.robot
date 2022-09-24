*** Settings ***
Documentation    Suite is for POC
Library  SeleniumLibrary
Variables



*** Test Cases ***
open_amazon
    [Tags]    amazon1
    open browser    https://www.amazon.in/      chrome
    maximize browser window
    set selenium implicit wait
    select radio button









    



*** Keywords ***
Happy to see you
