import behave

password = 'Qwerty123'


@behave.given('user is on Poczta Onet website')
def step_start_page(context):
    context.browser.get('https://www.onet.pl/')
    context.browser.implicitly_wait(10)
    context.browser.find_element_by_link_text('Przejdź do serwisu').click()
    context.browser.find_element_by_css_selector('headerNavItem mail').click()


@behave.when("user fills in the Sign In form and submits it")
def step_set_login_in(context):
    context.browser.find_element_by_id('f_login').send_keys('adrian.kupiec@op.pl')
    context.browser.find_element_by_id('f_password').send_keys(password)
    context.browser.find_element_by_css_selector('input.loginButton').click()


@behave.then("User can see email list")
def step_valid_login(context):
    context.browser.save_screenshot("screenshot-login.png")
    assert context.browser.find_element_by_css_selector('list-wrapper')
