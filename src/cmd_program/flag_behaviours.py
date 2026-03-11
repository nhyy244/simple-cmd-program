import art
from cmd_program.flag_descriptions import help_flag_description
from cmd_program.pos_args_maps import arg_to_color_map


def default_behaviour(message: str):
    print(f"hello {message}")


def help_flag_fn() -> None:
    print(help_flag_description)


def ascii_flag_fn(argument: str, flag_argument: str = "") -> str:
    result = art.text2art(f"hello {argument}", font="random")
    if isinstance(result, tuple):
        return result[0]
    return result


def color_flag_fn(argument: str, flag_argument: str = ""):
    return f"{arg_to_color_map[flag_argument]}{argument}{arg_to_color_map['default']}"
