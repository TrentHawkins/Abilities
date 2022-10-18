# Abilities

Display possible score palettes for a particular RPG game/setup.

The library [`simple-term-menu`](https://pypi.org/project/simple-term-menu/) is used.

## Usage

Check viable scores for a character creation based on character hyperparameters.
* Select game from menu.

### Dungeons and Dragons

Before checking viable ability score palettes some hyperparameters need fixing:
* Select scoring tier. Beyond the standard, there are natural extensions/shrinkages of the standard. The `human-only` tier uses the range `0` to `19` so it is basically only usable with `standard human` which shifts all ability points `+1`, therefore the range becomeing `1` to `20`, which is the full range of the game.
* Select race and optionally subrace, to determine any bonuses that apply to your ability score palettes. You should be warned that some of the maximal sum abilitiy score palettes assume that you apply race bonuses to "expensive" score increments.
* Select extra ability points to accound for if loading a character of higher than 1 level. It measures in extra ability points instead of level, to account for custom character levelling-up, like getting a custom feature with only +1 or +0 ability points instead of the standard +2 ability points.

### Cyberpunk 2077

In this game 1 ability point is awarded per level:
* Select character level(s) to get viable ability score palettes and plan ahead your character development.
