#!/usr/bin/env python3
import sys
from cmd_program.ArgumentParser import ArgumentParser
from cmd_program.flag_behaviours import ascii_flag_fn, help_flag_fn, color_flag_fn
from cmd_program.flag_descriptions import (
    help_flag_description,
    ascii_flag_description,
    color_flag_description,
)
from cmd_program.pos_args_maps import arg_to_color_map


def main_thread():
    arg_parser = ArgumentParser()

    color_flag_arguments = [key for key in arg_to_color_map.keys()]
    arg_parser.add_flag(
        name=["-c", "--color"],
        fn=color_flag_fn,
        description=color_flag_description,
        arguments=color_flag_arguments,
    )
    arg_parser.add_flag(
        name=["-a", "--ascii"],
        fn=ascii_flag_fn,
        description=ascii_flag_description,
        arguments=[],
    )
    arg_parser.add_flag(
        name=["-h", "--help"],
        fn=help_flag_fn,
        description=help_flag_description,
        arguments=[],
    )

    arg_parser.parse_args(sys.argv)
