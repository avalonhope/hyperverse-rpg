# type: ignore
from behave import given, when, then
from world.logic.characters import LeadCharacter
from world.logic.quests import Quest


@given("a character exists")
def create_character(context):
    """Create a test character."""
    context.character = LeadCharacter()


@given("a quest exists")
def create_quest(context):
    """Create a quest."""
    context.quest = Quest()


@when("the quests command is used")
def quests_command(context):
    """Run the command."""
    context.list_of_quests = context.character.command("quests")


@when("the joinquest command is used")
def joinquest_command(context):
    """Run the command."""
    context.list_of_quests = context.character.command("joinquest", context.quest)


@then("a list of available quests is shown")
def check_list_of_quests(context):
    """Check that a list of quests is shown."""
    if context.list_of_quests is None:
        raise AssertionError


@given("the quest has an existing partipant")
def quest_already_has_participants(context):
    """Ensure that the quest has at least one pariticipant."""
    context.quest.add_participant(LeadCharacter())


@then("the character is added to the list of quest participants")
def check_character_added_to_quest(context):
    """Check that the character is registered as a participant."""
    if context.character not in context.quest.list_participants():
        raise AssertionError
