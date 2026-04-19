from .pos_args_maps import arg_to_color_map

help_flag_description = """\
Usage:
  greeting [OPTIONS] [ARG...]

Print a greeting.

With one or more ARG values, prints "hello" followed by each ARG.
With no ARG, prints this help and exits.

Options:
  -h, --help                Show this help message and exit.
  -a, --ascii TEXT          Render the greeting as ASCII art using TEXT.
  -c, --color COLOR [TEXT]  Colorize TEXT using COLOR. If TEXT is omitted, show
                            information about COLOR usage and exit.

Examples:
  hello world
  hello world world2
  hello -a world
  hello -c red world
  hello -c red world -a
"""
ascii_flag_description = """\
-a, --ascii TEXT
    Render TEXT as ASCII art.

Usage:
    hello -a(--ascii) TEXT

Examples:
    hello -a world
"""

available_colors = "\n".join(f"  {c}" for c in arg_to_color_map.keys())
color_flag_description = f"""\
-c, --color COLOR [TEXT]
    Colorize TEXT using COLOR. If TEXT is omitted, show this help and exit.

Usage:
    hello -c(--color) COLOR [TEXT]

Examples:
    hello -c red world
    hello --color blue

Available colors:
{available_colors}
"""
