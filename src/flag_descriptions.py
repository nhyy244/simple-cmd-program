from src.color_maps import arg_to_color_map
help_description="""Usage: greeting [OPTION]... [ARG]

Print a greeting.

If ARG is provided, prints "greeting ARG".
If no ARG is given, desiplay --help text

Options:
  -h, --help              display this help and exit
  -a, --ascii string      displays the greeting in a cool way
"""
ascii_description=""" 
-a(--ascii) string 
Takes a string and transforms it into ascii art
    """

available_colors="  \n".join([color for color in arg_to_color_map.keys()])
color_description=f""" 
-c(--color) [color] string
Takes a string and colors it. If no colors are specified, a random one will be chosen. 
Example usage: hello -c red greeting

Colors available:
{available_colors}
""" #TODO enforce that only one color can be chosen. if multiple colors are specified, only the first one is chosen
