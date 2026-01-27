#!/usr/bin/env python3
import sys
from src.flag_behaviours import ascii_flag_fn, default_behaviour, help_flag_fn, color_flag_fn
from src.flag_descriptions import help_description, ascii_description, color_description
from src.color_maps import arg_to_color_map
from src.flag import Flag

help_flag: Flag = Flag(help_flag_fn,help_description,takes_argument=False)
ascii_flag: Flag = Flag(ascii_flag_fn,ascii_description,takes_argument=True)
color_flag: Flag = Flag(color_flag_fn,color_description,takes_argument=True)


flag_map = {
    "-h" : help_flag,
    "--help": help_flag,
    "-a": ascii_flag,
    "--ascii": ascii_flag,
    "-c":color_flag,
    "--color":color_flag
}

def extract_args(sys_args: list[str]= []) -> tuple[list[str], list[str], list[str]]:
    greetings:list[str] = []
    flags:list[str] = []
    color_arguments = []
    for arg in sys_args:
        if arg.startswith("-"):
            flags.append(arg)
        else:
            greetings.append(arg)
    return (greetings,flags,color_arguments)
#split into positional arguments and flags. 
#sort the positional arguments into their categories => color_pos_args, hello_pos_args,...
#

def parse_args(greetings:list[str], flags: list[str], color_arguments: list[str] = []): 
    no_greetings = len(greetings) < 2
    
    if len(flags) == 0 and no_greetings:
        help_flag.fn()
        sys.exit()
        
    if len(flags) == 0:
        for greeting in greetings[1:]: # sys.argv will always be populated with path of program.
            default_behaviour(greeting)
        sys.exit()
    
    for flag in flags: #error checking loop
        if flag not in flag_map:
            print(f"{flag} unknown. Use -h(--help) to see supported flags")
            sys.exit()
            
        if no_greetings:
            print(flag_map[flag].description)
            sys.exit()
                
        if not flag_map[flag].takes_argument:
            flag_map[flag].fn()
            sys.exit()

    for flag in flags:
        if flag_map[flag].is_used:
            continue
        for greeting in greetings[1:]: 
            greeting = flag_map[flag].fn(greeting,color_arguments)
            print(greeting)
        flag_map[flag].is_used= True
    sys.exit()  
            
def main_thread():
    greeting,flags,color_arguments = extract_args(sys.argv)
    print(f"COLOR_ARGUMENTS: {color_arguments}")
    print(f"GREETINGS: {greeting[1:]}")
    parse_args(greeting,flags,color_arguments)

    
