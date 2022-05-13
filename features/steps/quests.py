from behave import *
from typeclasses import accounts


@given("a new character has been created")
def step_impl(context):
    """Create a test character."""
    test_account = accounts.create("username", "password")
    test_account.create_character()


@when("the quest command is used")
def step_impl(context):
    """Run the quest command."""


@then("a list of quests is shown")
def setp_impl(context):
    """Check that a list of quests is shown."""