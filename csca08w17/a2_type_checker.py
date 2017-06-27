import builtins

# Check for use of functions print and input.

# IMPORTANT!
# If you are getting this error message here: 
# line 11, in <module>
#     our_print = print
# invalid syntax: <string>, line 11, pos 21
# Then you are using the wrong version of Python! Make sure you have Python 3!
our_print = print
our_input = input

def disable_print(*args):
    raise Exception("You must not call print anywhere in your code!")

def disable_input(*args):
    raise Exception("You must not call input anywhere in your code!")

builtins.print = disable_print
builtins.input = disable_input

import Calendar

# Type check Calendar.command_help
result = Calendar.command_help()
assert isinstance(result, str), \
       '''Calendar.command_help should return a str, but returned {0}
       '''.format(type(result))


# Type check Calendar.command_add
result = Calendar.command_add("2017-02-28", "Python class", {})
assert isinstance(result, str), \
       '''Calendar.command_add should return a str, but returned {0}
       '''.format(type(result))


# Type check Calendar.command_show
result = Calendar.command_show({})
assert isinstance(result, str), \
       '''Calendar.command_show should return a str, but returned {0}
       '''.format(type(result))


# Type check Calendar.command_delete
result = Calendar.command_delete("2017-02-28", 0, {})
assert isinstance(result, str), \
       '''Calendar.command_delete should return a str, but returned {0}
       '''.format(type(result))


# Type check Calendar.save_calendar
result = Calendar.save_calendar({})
assert isinstance(result, bool), \
       '''Calendar.save_calendar should return a bool, but returned {0}
       '''.format(type(result))

# Type check Calendar.load_calendar
result = Calendar.load_calendar()
assert isinstance(result, dict), \
       '''Calendar.load_calendar should return a dict, but returned {0}
       '''.format(type(result))

# Type check Calendar.is_command
result = Calendar.is_command("add")
assert isinstance(result, bool), \
       '''Calendar.is_command should return a bool, but returned {0}
       '''.format(type(result))


# Type check Calendar.is_calendar_date
result = Calendar.is_calendar_date("2015-10-15")
assert isinstance(result, bool), \
       '''Calendar.is_calendar_date should return a bool, but returned {0}
       '''.format(type(result))


# Type check Calendar.is_natural_number
result = Calendar.is_natural_number("2015")
assert isinstance(result, bool), \
       '''Calendar.is_natural_number should return a bool, but returned {0}
       '''.format(type(result))

# Type check Calendar.parse_command
result = Calendar.parse_command("add 2015-10-22")
assert isinstance(result, list), \
       '''Calendar.parse_command should return a list, but returned {0}
       '''.format(type(result))


our_print("""
Hooray! The type checker passed!
This does NOT necessarily mean that your functions are correct!

It does mean that the functions in Calendar.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

Please note user_interface() has not been typechecked.

Be sure to thoroughly test your functions yourself before submitting.""")

builtins.print = our_print
builtins.input = our_input