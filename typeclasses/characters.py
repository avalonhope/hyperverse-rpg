"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
import deal

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
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
        "This is called when object is first created, only."
        self.db.race = None
        self.db.faction = None
        self.db.subrace = None
        self.db.plural = False
        self.db.strength = 1
        self.db.agility = 1
        self.db.speed = 1
        self.db.health = 1
        
   # the result is always non-negative
    @deal.post(lambda result: result >= 1.0)
    # the function has no side-effects
    @deal.pure
    def proficiency (experience):
        """
        Calculate a charcater's skill proficency based on experience points.
        
        The result is 1 plus one tenth of the cube root of the experience points.
        
        For example: 1000 experience points gives a proficency of 2.0.
        """
        return 1.0 + (round((experience ** (1.0/3.0)), 2) / 10.0)
        
