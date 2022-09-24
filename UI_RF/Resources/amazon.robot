*** Settings ***
Library  SeleniumLibrary
Variables   ../ObjectRepository/repository.py     amazon_home


*** Keywords ***
enter_item_to_search
    [Documentation]  It will enter the item.
    [Arguments]  ${p_item}="Mobiles"
    wait until element is visible   ${web_search_items}     10s     Search field not displayed.
    input text  ${web_search_items}       ${p_item}
    click element   ${web_button_items}
    scroll element into view  ${web_searched_item}
    wait until element is visible   ${web_searched_item}     10s     Searched Item not displayed.
    click element  ${web_searched_item}



