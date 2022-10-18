"""Disco Elysium ability scoring.

base palette:  1  1  1  1
initial points: 8
level range: 1-6
"""

from ..abilities import Abilities, Schema


class DiscoElysium(Abilities):
    """Specialized Abilities class for Disco Elysium.

    Disco Elysium uses a custom cut-off which is lower than the default half cost volume.
    """

    _definition = [1, 6]
    _extent = 4
    _cutoff = 2 * _extent

    def __init__(self):
        """Generate a new Disco Elysium attribute score system."""
        super().__init__(Schema(definition=DiscoElysium._definition), DiscoElysium._extent, cutoff=DiscoElysium._cutoff)

    def __repr__(self) -> str:
        """Wrap Abilities print with mod 2."""
        return super().__repr__(spectrum=set(range(1, 7)), mod=2)
