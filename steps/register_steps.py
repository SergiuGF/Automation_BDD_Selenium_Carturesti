from behave import *

@given("the user is on the home page and is not logged in")
def step_impl(context):
    context.register_page.navigate_to_home_page_log_out()


"""@Register1"""
@when('the user clicks on the register button')
def step_impl(context):
    context.register_page.open_reg_box()

@when('the user clicks on the new user button')
def step_impl(context):
    context.register_page.new_user()

@when('the user enters a random valid email')
def step_impl(context):
    context.register_page.set_random_email()

@when('the user enters a valid password "{pwd}"')
def step_impl(context, pwd):
    context.register_page.set_password(pwd)

@when('the user clicks the signup button')
def step_impl(context):
    context.register_page.click_singup_button()

@then('the email and password error message is not displayed')
def step_impl(context):
    context.register_page.check_email_pwd_error_not_displayed()


"""@Register2"""
@when('the user enters an invalid email "{invalid_email}"')
def step_impl(context, invalid_email):
    context.register_page.invalid_email(invalid_email)

@then('the email error message is displayed')
def step_impl(context):
    context.register_page.reg_email_error_message_is_displayed()

@then('the email error message contains "{error_msg_text}" text')
def step_impl(context, error_msg_text):
    context.register_page.reg_email_error_message_is_correct(error_msg_text)


"""@Register3"""
@when('the user enters an invalid password "{pwd}"')
def step_impl(context, pwd):
    context.register_page.invalid_password(pwd)

@then('the password error message is displayed')
def step_impl(context):
    context.register_page.reg_pwd_error_message_is_displayed()

@then('the password error message contains "{error_msg_text}" text')
def step_impl(context, error_msg_text):
    context.register_page.reg_pwd_error_message_is_correct(error_msg_text)


"""@Register4"""
@then('the captcha error message is displayed')
def step_impl(context):
    context.register_page.reg_cpt_error_message_is_displayed()

@then('the captcha error message contains "{error_msg_text}" text')
def step_impl(context, error_msg_text):
    context.register_page.reg_cpt_error_message_is_correct(error_msg_text)