"""Ability score generator for know games.

This is the main navigation menu.
-	First you select a game,
-	Then you select defining details about the character you want to build.
-	When all the possibilities for your set-up character are shown, you may filter choices down and even mark your favorite ones.
"""


from re import sub
from shutil import get_terminal_size

from simple_term_menu import TerminalMenu

from src.games.cyberpunk_2077 import Cyberpunk2077
from src.games.disco_elysium import DiscoElysium
from src.games.dungeons_and_dragons import DungeonsDragons


def _add_missing_control_characters_for_keys(cls, keys) -> None:
	pass


TerminalMenu._add_missing_control_characters_for_keys = _add_missing_control_characters_for_keys  # type: ignore
TerminalMenu._codename_to_capname.update(
	{
		"left": "kcub1",
		"right": "kcuf1",
	}
)
TerminalMenu._codenames = tuple(TerminalMenu._codename_to_capname.keys())


menu_width = get_terminal_size().columns
menu_style = {
	"accept_keys": (
		"enter",
		"right",
	),
	"clear_menu_on_exit": True,
	"clear_screen": True,
#   "cursor_index": None,  # set locally
	"cycle_cursor": True,
	"exit_on_shortcut": False,
	"menu_cursor": None,
	"menu_cursor_style": None,
	"menu_highlight_style": (
		"standout",
	),
	"preselected_entries": None,
#   "preview_border": DEFAULT_PREVIEW_BORDER,
#   "preview_command": None,
#   "preview_size": DEFAULT_PREVIEW_SIZE,
#   "preview_title": DEFAULT_PREVIEW_TITLE,
	"quit_keys": (
		"escape",
		"left",
	),
	"raise_error_on_interrupt": True,
	"search_case_sensitive": True,
	"search_highlight_style": (
		"bold",
	),
	"search_key": None,
#   "shortcut_brackets_highlight_style": DEFAULT_SHORTCUT_BRACKETS_HIGHLIGHT_STYLE,
#   "shortcut_key_highlight_style": DEFAULT_SHORTCUT_KEY_HIGHLIGHT_STYLE,
#   "show_search_hint": DEFAULT_SHOW_SEARCH_HINT,
#   "show_search_hint_text": None,
#   "show_shortcut_hints": DEFAULT_SHOW_SHORTCUT_HINTS,
#   "show_shortcut_hints_in_status_bar": DEFAULT_SHOW_SHORTCUT_HINTS_IN_STATUS_BAR,
	"skip_empty_entries": False,
	"status_bar": None,
#   "status_bar_below_preview": DEFAULT_STATUS_BAR_BELOW_PREVIEW,
#   "status_bar_style": DEFAULT_STATUS_BAR_STYLE,
#   "title": None  # set locally
}
multi = {
	"multi_select": True,
	"multi_select_cursor": "+",
	"multi_select_cursor_brackets_style": None,
	"multi_select_cursor_style": None,
	"multi_select_empty_ok": True,
	"multi_select_keys": (
		"space",
		"right",
	),
	"multi_select_select_on_accept": False,
#   "show_multi_select_hint": DEFAULT_SHOW_MULTI_SELECT_HINT,
#   "show_multi_select_hint_text": None,
}  # unused

game_dict = {
	"DungeonsDragons": "Dungeons and Dragons",
	"Cyberpunk2077": "Cyberpunk 2077",
	"DiscoElysium": "Disco Elysium",
}

if __name__ == "__main__":
	preferred_scores = set()

	game_index = 0

	try:
		while game_index is not None:
			game_index = TerminalMenu(
				(f"  {value:{menu_width-2}}" for value in game_dict.values()),
				title=f"Choose game:\n",
				cursor_index=game_index,  # type: ignore  # The initially selected item index.
			**menu_style).show()

			if game_index is None:
				break

			game = list(game_dict.values())[game_index]

			if game == game_dict["DungeonsDragons"]:
				tier = 2

				while tier is not None:
					tier = TerminalMenu(
						(f"  {value:{menu_width-2}}" for value in DungeonsDragons._names.values()),
						title=f"{game}: tier\n",
						cursor_index=tier,  # type: ignore  # The initially selected item index.
					**menu_style).show()

					if tier is None:
						break

					race_index = 3

					while race_index is not None:
						if tier == 6:
							race_index = TerminalMenu(
								(f"  {'Human':{menu_width-2}}",),
								title=f"{game}: {DungeonsDragons._names[tier]} race\n",  # type: ignore
								cursor_index=race_index,  # type: ignore  # The initially selected item index.
							**menu_style).show()

							if race_index is not None:
								race_index = 3

						else:
							race_index = TerminalMenu(
								(f"  {key:{menu_width-2}}" for key in DungeonsDragons._races),
								title=f"{game}: {DungeonsDragons._names[tier]} race\n",
								cursor_index=race_index,  # type: ignore  # The initially selected item index.
							**menu_style).show()

						if race_index is None:
							break

						race = list(DungeonsDragons._races)[race_index]  # type: ignore

						subrace_index = 0

						if type(DungeonsDragons._races[race]) is dict:
							subrace_index = TerminalMenu(
								(f"  {key:{menu_width-2}}" for key in DungeonsDragons._races[race]),
								title=f"{game}: {DungeonsDragons._names[tier]} subrace {race}\n",
								cursor_index=subrace_index,  # The initially selected item index.
							**menu_style).show()

							if subrace_index is None:
								continue

							subrace = list(DungeonsDragons._races[race])[subrace_index]  # type: ignore

						else:
							subrace = ""

						extra = 0

						while extra is not None:
							extra = TerminalMenu(
								(f"  +{key:<{menu_width-3}}" for key in range(DungeonsDragons._max_extra + 1)),
								title=f"{game}: {DungeonsDragons._names[tier]} {subrace} {race} extra\n",
								cursor_index=extra,  # type: ignore  # The initially selected item index.
							**menu_style).show()

							if extra is None:
								break

							scores_list = [
								f" {key:<{menu_width-1}}" for key in repr(DungeonsDragons(tier, race, subrace, extra)).split("\n")
							]
							scores_index = 0

							while scores_index is not None:
								scores_index = TerminalMenu(
									scores_list,
									title=f"{game}: {DungeonsDragons._names[tier]} {subrace} {race} +{extra} {len(scores_list)}\n",
									cursor_index=scores_index,  # type: ignore  # The initially selected item index.
								**menu_style).show()

								if scores_index is None:
									break

								scores_list[scores_index] = sub("^ ", "+", scores_list[scores_index])  # type: ignore
								preferred_scores.add(scores_list[scores_index])  # type: ignore

			if game == game_dict["Cyberpunk2077"]:
				level = 0

				while level is not None:
					level = TerminalMenu(
						(f"  {f'{key+1:>2}':<{menu_width-2}}" for key in range(Cyberpunk2077._max_level)),
						title=f"{game}: level\n",
						cursor_index=level,  # type: ignore  # The initially selected item index.
					**menu_style).show()

					if level is None:
						break

					scores_list = [
						f" {key:<{menu_width-1}}" for key in str(Cyberpunk2077(level + 1)).split("\n")  # type: ignore
					]
					scores_index = 0

					while scores_index is not None:
						scores_index = TerminalMenu(
							scores_list,
							title=f"{game}: Level {level+1} ({len(scores_list)})\n",
							cursor_index=scores_index,  # type: ignore  # The initially selected item index.
						**menu_style).show()

						if scores_index is None:
							break

						scores_list[scores_index] = sub("^ ", "+", scores_list[scores_index])  # type: ignore
						preferred_scores.add(scores_list[scores_index])  # type: ignore

			if game == game_dict["DiscoElysium"]:
				scores_list = [
					f" {key:<{menu_width-1}}" for key in str(DiscoElysium()).split("\n")
				]
				scores_index = 0

				while scores_index is not None:
					scores_index = TerminalMenu(
						scores_list,
						title=f"{game}: ({len(scores_list)})\n",
						cursor_index=scores_index,  # type: ignore  # The initially selected item index.
					**menu_style).show()

					if scores_index is None:
						break

					scores_list[scores_index] = sub("^ ", "+", scores_list[scores_index])  # type: ignore
					preferred_scores.add(scores_list[scores_index])  # type: ignore

		for scores in sorted(preferred_scores):
			print(scores)

	except KeyboardInterrupt:
		exit()
