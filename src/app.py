#!/usr/bin/env python3
import sys
from src.flag_behaviours import ascii_flag_fn, default_behaviour, help_flag_fn, color_flag_fn
from src.flag_descriptions import help_description, ascii_description, color_description
from src.pos_args_maps import arg_to_color_map
from src.flag import Flag

help_flag: Flag = Flag(help_flag_fn,help_description,takes_arguments=False)
ascii_flag: Flag = Flag(ascii_flag_fn,ascii_description,takes_arguments=True)
color_flag: Flag = Flag(color_flag_fn,color_description,takes_arguments=True)
color_flag.pos_arg_map = arg_to_color_map
flag_objects: list[Flag] = [help_flag,ascii_flag,color_flag]
flag_map = {
    "-h" : help_flag,
    "--help": help_flag,
    "-a": ascii_flag,
    "--ascii": ascii_flag,
    "-c":color_flag,
    "--color":color_flag
}
class PositionalArgs():
    greetings: list[str]
    color_flag: list[str]

class ExtractedArgs():
    positional_args: PositionalArgs
    flags: list[str]

def extract_args(sys_args: list[str]= []) -> tuple[list[str], list[str], list[str]]: # -> ExtractedArgs
    greetings:list[str] = []
    flags:list[str] = []
    positional_args = []
    for arg in sys_args:
        if arg.startswith("-"):
            flags.append(arg)
        else:
            positional_args.append(arg)
    greetings = positional_args     
    for flag in flag_objects:
        for pos_arg in list(flag.pos_arg_map.keys()):
            if pos_arg in positional_args and pos_arg not in flag.positional_args:
                flag.positional_args.append(pos_arg)
    return (greetings,flags)

def parse_args(greetings:list[str], flags: list[str]): #hello -c red red fails. greetings = [red, red] instead of greetings = [red]
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

        if flag_map[flag].takes_arguments:      
            greetings_temp = greetings
            for pos_arg_flag in flag_map[flag].positional_args:
                if pos_arg_flag in greetings_temp:
                    greetings_temp.remove(pos_arg_flag)
            if len(flag_map[flag].positional_args) != 0 and len(greetings_temp) < 2:
                print(flag_map[flag].description)
                sys.exit()    
    
        if not flag_map[flag].takes_arguments:
            flag_map[flag].fn()
            sys.exit()


    for flag in flags:
        if flag_map[flag].is_used:
            continue
        for greeting in greetings[1:]:
            greeting = flag_map[flag].fn(greeting)
            print(greeting)
        flag_map[flag].is_used= True
    """for greeting in greetings[1:]:
        for flag in flags:
            if len(flag.positional_args) != 0:
                for pos_arg in flag.positional_ar gs:
                        greeting = flag_map[flag].fn(greeting,pos_arg)
                flag_map[flag].is_used=True
            else: 
                greeting=flag_map[flag].fn(greeting)
        print(greeting)
        flag_map[flag].is_used=True"""   
    sys.exit()  
  
          
def main_thread():
    greetings,flags = extract_args(sys.argv)
    print(f"GREETINGS; {greetings}")
    print(f"COLOR_FLAG POS ARGS: {color_flag.positional_args}")
    parse_args(greetings,flags)

    
