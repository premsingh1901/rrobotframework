amazon_home= {
    "web_search_items": "css:input#twotabsearchtextbox",
    "web_button_items": "css:input#nav-search-submit-button",
    "web_searched_item": "xpath://span[contains(text(),'OnePlus Nord CE 2 5G (Gray Mirror, 8GB RAM, 128GB Storage)')]",
}




def get_variables(arg):
    if arg == 'amazon_home':
        return amazon_home
    else:
        return -1