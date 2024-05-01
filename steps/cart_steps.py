from behave import *

@given("the user is logged in and is on the home page")
def step_impl(context):
    context.cart_page.navigate_to_home_page_and_login()


"""@Cart"""
@when('the user searches for book "{product_name}"')
def step_impl(context, product_name):
    context.cart_page.search_product(product_name)

@when('the user clicks on the add to cart button')
def step_impl(context):
    context.cart_page.click_add_to_cart()

@when('the user clicks on the cart button')
def step_impl(context):
    context.cart_page.click_cart_btn()

@then('the product is displayed')
def step_impl(context):
    context.cart_page.cart_product_is_displayed()

@then('the product in the cart contains text "{product_name}"')
def step_impl(context, product_name):
    context.cart_page.cart_product_contains_text(product_name)


"""@Wishlist"""
@when('the user searches for wished book "{product_name}"')
def step_impl(context, product_name):
    context.cart_page.search_product(product_name)

@when('the user clicks on the add to wishlist button')
def step_impl(context):
    context.cart_page.click_add_to_wishlist()

@when('the user clicks on the wishlist button')
def step_impl(context):
    context.cart_page.click_wishlist_btn()

@then('the wished product is displayed')
def step_impl(context):
    context.cart_page.wish_product_is_displayed()

@then('the product in the wishlist contains text "{product_name}"')
def step_impl(context, product_name):
    context.cart_page.wish_product_contains_text(product_name)


"""@CartPrices"""
@when('the user adds products to the cart')
def step_impl(context):
    context.cart_page.search_and_add_to_cart()

@when('the user clicks on the cart button - CartPrices')
def step_impl(context):
    context.cart_page.click_cart_btn()

@then('the total price is equal to the sum of all prices')
def step_impl(context):
    context.cart_page.total_price_is_correct()
