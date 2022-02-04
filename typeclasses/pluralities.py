"""
Pluralities
Pluralities are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Plurality class in this module
is setup to be the "default" character type created by the default
creation commands.
"""
from evennia import DefaultCharacter


class Plurality(DefaultCharacter):
    """
    The Plurality defaults to reimplementing some of base Object's hook methods with the
    following functionality:
    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.
    """
    
    def at_object_creation(self):
        """
        Called only at initial creation.
        
        There should be at least two personsa and at least one inner world in a plural system.
        
        """
        #set persistent attributes
        self.db.personas = []
        self.db.worlds = []

    def get_personas(self):
        """
        List of top-level personas within the plural system
        """
        return self.db.personas

    pass