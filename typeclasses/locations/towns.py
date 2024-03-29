"""Towns"""
import icontract

from evennia import DefaultExit
from typeclasses.locations.locations import Location  # type: ignore
from world.logic.location_types import LocationType  # type: ignore


@icontract.invariant(lambda self: self.locationType == LocationType.TOWN)
class Town(Location):
    """Towns."""

    def at_object_creation(self):
        """Initial properties of a town."""
        self.db.locationType = LocationType.TOWN


class Road(DefaultExit):
    """Roads are the connectors for travel between Towns."""
