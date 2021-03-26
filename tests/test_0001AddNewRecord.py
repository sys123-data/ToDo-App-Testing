import pytest, time
from tests.framework.fixture import toDoAppPage
from tests.framework.fixture import app

from pytest_bdd import (
    scenario,
    given,
    when,
    then
)


@scenario('features/0001AddNewRecord.feature','Add new record')
def test_add_new_record():
    """Add new record"""

@given('I access the website')
def i_access_the_website(toDoAppPage):
    assert toDoAppPage.go_to_web_site(), 'Web site not loaded'

@when('I insert <value>')
def i_insert_value(toDoAppPage,value):
    assert toDoAppPage.send_msj(value), 'Msj not sent'

@when('I click add')
def i_click_add(toDoAppPage):
    assert toDoAppPage.click_add_button(), 'Button not clicked'

@then('<value> should be available')
def look_for_added_item(toDoAppPage,value,app):
    assert toDoAppPage.look_for_added_item(value), 'Item not added'
    app.take_screenshot('0001')
    toDoAppPage.end_session()