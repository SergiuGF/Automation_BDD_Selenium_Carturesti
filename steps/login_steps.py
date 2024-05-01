from behave import *

@given("the user is on the home page and is logged out")
def step_impl(context):
    context.login_page.navigate_to_home_page_log_out()

"""@Login1"""
@when('the user clicks on the login button')
def step_impl(context):
    context.login_page.open_login_box()

@when('the user clicks on the existing user button')
def step_impl(context):
    context.login_page.click_existing_user()

@when('the user enters a valid email "{email}"')
def step_impl(context, email):
    context.login_page.set_login_email(email)

@when('the user enters a correct password "{pwd}"')
def step_impl(context, pwd):
    context.login_page.set_login_password(pwd)

@when('the user clicks the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('the login box is closed')
def step_impl(context):
    context.login_page.login_box_not_displayed()


"""@Login2"""
@when('the user enters email address "{email}"')
def step_impl(context, email):
    context.login_page.set_login_email(email)

@when('the user enters password "{pwd}"')
def step_impl(context, pwd):
    context.login_page.set_login_password(pwd)

@Then('the login error message is displayed')
def step_impl(context):
    context.login_page.log_error_message_is_displayed()

@Then('the login error message contains "{error_msg_text}" text')
def step_impl(context, error_msg_text):
    context.login_page.log_error_message_is_correct(error_msg_text)


"""@Login3"""
@Then('the second login error message is displayed')
def step_impl(context):
    context.login_page.second_log_error_message_is_displayed()

@Then('the second login error message contains "{error_msg_text}" text')
def step_impl(context, error_msg_text):
    context.login_page.second_log_error_message_is_correct(error_msg_text)
