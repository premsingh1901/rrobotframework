*** Settings ***
Documentation    Suite is for POC
Library  SeleniumLibrary
Variables    ../Config/config.yml
Variables    ../TestData/test_data.yml
Resource    ../Resources/amazon.robot

Test Teardown   close browser

*** Test Cases ***
open_amazon
    [Tags]    amazon1

    open browser    ${env.URL}      ${env.BROWSER}
    Maximize Browser Window
    set selenium implicit wait      10s
    amazon.enter_item_to_search     ${poc_amazon.mobile_search}
















    



*** Keywords ***
Happy to see you
