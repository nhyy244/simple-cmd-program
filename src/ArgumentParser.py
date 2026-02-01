from typing import Callable
from src.flag_descriptions import help_flag_description
from src.flag_behaviours import default_behaviour
import sys
class Flag: 
    def __init__(self, name:list[str], fn: Callable[..., str | None], description:str, arguments:list[str] = []): 
        self.name = name
        self.fn = fn
        self.description = description
        self.arguments = arguments #all possible arguments for the flag
        self.active_argument = "" #flag argument passed in by the user. Only one active argument allowed

class ArgumentValidator:
    def __init__(self, flags: list[Flag], arguments: list[str]):
        self.flags = flags
        self.arguments = arguments
        self.is_both_flags_and_args_not_present = not self.flags and not self.arguments
        self.is_flag_present_with_no_argument = self.flags and not self.arguments
        self.is_argument_present_with_no_flags = self.arguments and not self.flags 
        self.is_both_argument_and_flag_present = self.arguments and self.flags
    
    def rearrange_color_flag(self) -> list[Flag]:
        self.flags.sort(
            key=lambda f: ("-c" in f.name or "--color" in f.name) # False < True 
        )
        return self.flags
class ArgumentParser:
    def __init__(self):
        self.flags:list[Flag] = []
        self.arguments: list[str] = []
        self.help_description = help_flag_description
        
    def add_flag(self, name : list[str], fn: Callable[..., str | None], description : str, arguments : list[str] = []):
        self.flags.append(Flag(name=name,
                                fn=fn,
                                description=description,
                                arguments=arguments))
        
    def get_flag(self, name:str) -> Flag | None:
        for flag in self.flags:
            if name in flag.name:
                return flag
        return None
    
    def parse_args(self,command_line_arguments: list[str]):
        flags,arguments = self._extract_flags_and_arguments(command_line_arguments)
        # print(f"user arguments: {arguments}")
        # print(f"flags: {flags}")
        # for flag in flags: 
        #     print(f"Active arguments for flag {flag.name}: {flag.active_argument}")

        argument_validator = ArgumentValidator(flags,arguments)
        if argument_validator.is_both_flags_and_args_not_present:
            print(self.help_description)
            sys.exit()
        if argument_validator.is_flag_present_with_no_argument: #not handling the FLAG_NAME --help case. 
            if self.get_flag("-h") in flags:
                print(self.help_description)
                sys.exit()
            print(flags[0].description)
            sys.exit()
        if argument_validator.is_argument_present_with_no_flags:
            for arg in arguments:
                default_behaviour(arg)
            sys.exit()   
        if argument_validator.is_both_argument_and_flag_present:
            flags = argument_validator.rearrange_color_flag()
            for flag in flags:
                print(flag.name)
            for argument in arguments:
                for flag in flags:
                    if flag.arguments and flag.active_argument:
                        argument = flag.fn(argument, flag.active_argument)
                    else:
                        if flag.arguments: #if a flag that takes arguments is invoked without arguments but with a greeting
                            print(flag.description)
                            sys.exit()
                        argument = flag.fn(argument)
                print(argument)
        return

    def _extract_flags_and_arguments(self, command_line_arguments: list[str]):
        flags: list[Flag] = []
        arguments: list[str] = []
        seen: set[int] = set()

        for item in command_line_arguments[1:]:
            if item.startswith("-"):
                flag = self.get_flag(item)
                if flag is None:
                    print(f"No flag with name {item} found. Use '-h(--help)' for more information")
                    sys.exit()

                if id(flag) not in seen:
                    flags.append(flag)
                    seen.add(id(flag))
            else:
                arguments.append(item)

        arguments = self._map_arguments_to_flag_arguments(flags, arguments)
        return flags, arguments
    
    def _map_arguments_to_flag_arguments(self, flags:list[Flag], arguments:list[str]) -> list[str]:
        for flag in flags:
            for arg in arguments:
                if arg in flag.arguments:
                    flag.active_argument = arg
                    arguments.remove(arg)
                    break
        return arguments
    

                
                    
        
                
            
                
                
