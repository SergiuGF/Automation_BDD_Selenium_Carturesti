from behave import *

@given("the user is on the Home Page")
def step_impl(context):
    context.home_page.navigate_to_home_page()


"""@Search"""
@when('the user clicks on the search bar')
def step_impl(context):
    context.home_page.click_search_bar()

@when('the user search for an existing product "{product}"')
def step_impl(context, product):
    context.home_page.search_for_products(product)

@then('at least three products are displayed')
def step_impl(context):
    context.home_page.check_product_quantity()


"""@Filter1"""
@when('the user clicks on the dropdown menu')
def step_impl(context):
    context.home_page.click_meniu()

@when('the user clicks on the books tab')
def step_impl(context):
    context.home_page.click_books_tab()

@when('the user applies the in stock filter')
def step_impl(context,):
    context.home_page.apply_in_stock_filter()

@then('the -in stock- detail is displayed')
def step_impl(context):
    context.home_page.in_stock_msg_is_displayed()

@then('the product contains text "{text}"')
def step_impl(context, text):
    context.home_page.in_stock_msg_is_correct(text)


"""@Filter2"""
#first two steps are the same

@when('the user applies the 100-200 price filter')
def step_impl(context,):
    context.home_page.apply_price_filter()

@then('all the prices of the products are between "{min_price}" and "{max_price}" ron')
def step_impl(context, min_price, max_price):
    context.home_page.check_products_prices(min_price, max_price)


"""@Test_URL"""
@when('the user clicks on a hyperlink "{button}"')
def step_impl(context,button):
    context.home_page.click_hyperlink_button(button)

@then('the user is redirected to a new "{URL}"')
def step_impl(context, URL):
    context.home_page.check_url(URL)


"""Language"""
@when('the page is set to Romanian language')
def step_impl(context):
    context.home_page.set_to_romanian()

@when('the user sets the page to English language')
def step_impl(context):
    context.home_page.set_to_english()

@then('the page is set to "{ENGLISH}"')
def step_impl(context, ENGLISH):
    context.home_page.check_language(ENGLISH)


"""@Assistant"""
@when('the user clicks on the assistant button')
def step_impl(context):
    context.home_page.open_assistant()

@then('the assistant tab is open')
def step_impl(context):
    context.home_page.check_assistant_tab_displayed()

@when('the user clicks on the close assistant button')
def step_impl(context):
    context.home_page.close_assistant()

@then('the assistant tab is closed')
def step_impl(context):
    context.home_page.check_assistant_tab_not_displayed()
