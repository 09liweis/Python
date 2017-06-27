"""
# Copyright Nick Cheng, Brian Harrington, Danny Heap, Xueli Tan
# 2013, 2014, 2015, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2016
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from regextree import RegexTree, StarTree, DotTree, BarTree, Leaf

# Do not change anything above this comment except for the copyright
# statement

# Student code below this comment.

# this is the regex sumbols and operators
# number symbols
num_symbols = ['0', '1', '2', 'e']
# repeation symbol
repeat_sym = ['*']
# binary operation symbols
binary_sym = ['|', '.']


def is_regex(s):
    '''(str) -> Bool
    Determine whether a string is a valid regular expression. Return True if it
    is. Return False, vice versa
    '''
    # if it is a single character
    if len(s) <= 1:
        return (s in num_symbols)
    # if string ends with *
    elif s[-1] == '*':
        return is_regex(s[:-1])
    # if string with bracket in beginning and ending
    elif s[-1] == ')' and s[0] == '(':
        # testing to see whether the format error exist
        try:
            (left_side, right_side, operator) = str_deconstruct(s)
        except ValueError:
            return False
        # 
        return (operator in binary_sym
                and is_regex(left_side) and is_regex(right_side))
    # any ohter situation
    else:
        return False


def str_deconstruct(string):
    '''(string) -> set of string
    This function is a helper function for is_regex, which analyzes the given
    regexstr with '(' and ')' 
    and return a tuple of the left, right, and operator of 
    the regex expresstion
    REQ: min length of the str is 5
    REQ: str must start with '(' and ends with ')' 
    >>> str_deconstruct('(0.1)')
    ('0', '1', '.')
    >>> str_deconstruct('(0|1)')
    ('0', '1', '|')
    >>> str_deconstruct('((0.1')
    raise ValueError
    >>> str_deconstruct('((0.1)|(1.0*))')
    ('(0.1)', '(1.0*)', '|')
    '''
    # if the length of the string is too short
    if len(string) < 5:
        raise ValueError('it did not meet the minimum length')
    # if the string is not string with '(' and end with ')'
    elif string[0] != '(' and string[-1] != ')':
        raise ValueError('it not a regular expression')

    try:
        # remove the bracket of the string
        string = string[1:-1]
        # call helper func(find_operator()) to get the index of the operator
        index_of_operator = find_operator(string)
        # get the left and right side
        left = string[:index_of_operator]
        right = string[index_of_operator + 1:]
        operator = string[index_of_operator]
    
    except IndexError:
        # operator not found
        raise ValueError('formatted incorrectly')
    return (left, right, operator)


def find_operator(string):
    '''(string) -> int
    This function return the location of the operator in a regex expression
    REQ: min length of the string is 3
    >>> find_operator('0.0')
    1
    >>> find_operator('(1.0)|1')
    5
    '''
    # empty string
    if len(string) == 0:
        return 0

    else:
        # loop throught the string in order to find the operator in the widest
        # regular expression. Meantime, it does not care abouth anything
        # inside teh smaller bracket
        index = 0
        found_operator = False
        while index < len(string) and not found_operator:
            letter = string[index]

            # found operator. exist loop
            # index is the wanted result
            if letter in binary_sym:
                found_operator = True

            # 
            # find its end and skip to that index
            elif(letter == '('):
                index = find_end(string, index)

            else:
                # move to the next letter
                index += 1

        return index


def find_end(string, start):
    """(str, int) -> int
    This function returns the index of the end of the smaller regular
    expression

    REQ: start must smaller than the length of the string
    REQ: s[start_index] must be '('

    >>> find_end('(1.0).(0|1)', 0)
    4
    >>> find_end('(1.(0|0)).1', 0)
    8
    """

    # initializing the current level of sub_regex
    sub_regex = 1
    # move the next letter after '('
    index = start + 1

    # loop through the string to find the end of the sub_regex
    # or reach the end of the string 
    while sub_regex > 0 and index < len(string):
        letter = string[index]
        # if char is '(', sub_regex level + 1
        if letter == '(':
            sub_regex += 1
        # letter is ')', sub_regex level - 1
        elif letter == ')':
            sub_regex -= 1
        # move to the next letter
        index += 1

    # now the index can be the end of the sub_regex or the end of the string
    return index


def all_regex_permutations(s):
    '''(str) -> set of str
    return a set of all the permutations of the valid regular expression based
    on the give characters

    >>> all_regex_permutations('')
    set()
    >>> all_regex_permutations('2*')
    {'2*'}
    >>> all_regex_permutations('0*2')
    set()
    >>> all_regex_permutations('(0|1)()()()()')
    set()
    >>> all_regex_permutations('21.)(')
    {'(2.1)', '(1.2)'}
    '''
    # first base case -> s is an empty string
    # return empty set
    if len(s) == 0:
        return set()

    # second base case -> the length of the string is one
    if len(s) == 1:
        # if s is the regex number symbol, return it in the set
        if s in num_symbols:
            return {s}
        # s is not a regex expression, return empty set
        else:
            return set()

    # third ase case -> there are unequal number of bracket in the string
    # not valid, return empty set
    if (('(' in s) or ')' in s) and (s.count('(') != s.count(')')):
        return set()

    # fourth ase case -> if number of binary operator and the bracket is
    # not same, return empty set

    # calculate the number of dot and bar
    bin_operator_number = s.count('.') + s.count('|')

    # is the number of the operator and the '(' same
    if s.count('(') != bin_operator_number:
        return set()

    # recursive steps
    else:
        # create an empty set to store the permutations
        result = set()

        # if '*' is in the string
        if '*' in s:
            # remove the repeat of '*' one time
            modified_string = remove_repeat(s, ['*'])

            # find all the permutations of the modified string
            modified_permutations = all_regex_permutations(modified_string)

            # store the star symbol in the end of permutations
            result.update({(string + '*') for string in modified_permutations})

        # if '.' and '|' are in the given string
        for operator in binary_sym:
            if operator in s:
                # modified the string with one time repeat of the operator and
                # '(' and ')'
                modified_string = remove_repeat(s, [operator, '(', ')'])

                # For each possible way to divide lesser_s into
                # two non-empty strings:
                for (left_side, right_side) in split_str(modified_string):
                    # Get all possible regex permutations of (left, right).
                    # Format it like this: "({l_perm}{op}{r_perm})"
                    # And add it to perms
                    for left_perm in all_regex_permutations(left_side):
                        for right_perm in all_regex_permutations(right_side):
                            result.add("({}{}{})".
                                       format(left_perm, operator, right_perm))
        return result


def remove_repeat(string, elements):
    '''(str, list of characters) -> str
    this function remove the first appearance of the string and 
    REQ: all characters in the elements must occur in string

    >>> remove_occurences('spam_ham_eggs', 'sam_')
    'pham_eggs'
    >>> remove_occurences('spam_ham_eggs', ('s', 'a', 'm', '_'))
    'pham_eggs'
    '''
    # transfer the string into a list
    list_form = []
    for letter in string:
        list_form.append(letter)
    # remove the first appearance of the symbol
    for letter in elements:
        list_form.remove(letter)
    # store the element of the list of modified string into a string
    result = ''
    for letter in list_form:
        result += letter
    return result


def split_str(string):
    '''(str) -> set of tuples of strs
    return the set of all the possible combination of give string

    >>> split_combinations('02*') 
    {('*', '20'), ('2', '0*'), ('0', '2*'),
    ('02', '*'), ('0*', '2'), ('2*', '0')}
    '''
    # creat an empty 
    result = set()
    # split the string into two
    # i is smaller than the two parts of the length of the string
    i = 0
    while i < ((len(string) // 2) + 1):
        # get the combinations of all the letters in the string
        combinations = get_combs(string, i)
        # for each element of the combinations, attain for a str with the chars
        # in string which is not in the set of combination
        # add tuple of (word, unused_letter) to set
        for word in combinations:
            unused_letter = remove_repeat(string, word)
            result.add((word, unused_letter))
            result.add((unused_letter, word))
        i += 1

    return result


def get_combs(string, str_length):
    '''(str, int) -> str of str
    find all the combinations of the the letters in string
    with the given str_length and return them in a set

    REQ: len(string) >= str_length >= 0 

    >>> get_combs('1234', 1)
    {'1', '2', '3', '4'}
    >>> get_combs('1234', 2)
    {'12', '13', '14', '23', '24', '34'}
    '''
    # firstly, base case -> if str_length is one, 
    # return the set of characters in s
    if str_length == 1:
        return set(string)

    # secondly, recursive step
    else:
        # create an empty set to return
        result = set()

        # loop through each character in string
        i = 0
        while i < len(string):
            letter = string[i]

            # find the combination of the rest of character of the string 
            # from the index of the next character
            smaller_set = get_combs(string[(i + 1):], (str_length - 1))

            # update the set with the connectiong of word in smaller_set
            # and the letter
            result.update({(letter + word) for word in smaller_set})
            i += 1

        return result


def regex_match(r, s):
    '''(RegexTree, str) -> bool
    Determine whether the string matches the regular expression of the regex
    tree. Return True iff they match, False, vice versa.

    >>> regex_match(build_regex_tree('((1.(0|1)*).2)'), '10110012')
    True
    >>> regex_match(build_regex_tree('((1.(0|1)*).2)'), '12')
    True
    >>> regex_match(build_regex_tree('((1.(0|1)*).2)'), '21')
    False
    >>> regex_match(build_regex_tree('((1.(0|1)*).2)'), '122')
    False
    '''
    # if the regex matches 
    (num_matched, match_success) = same_number(r, s)
    if(match_success and (num_chars_matched == len(s))):
        return True
    else:
        return False


def same_number(r, s):
    '''(RegexTree, str) -> (int, bool)
    Return the index of the first character in s that is not matched by the
    regular expression represented by the RegexTree r, as well as whether
    or not the this match attempt is considered to have succeeded.

    Format of return tuple: (num_chars_matched, match_success)

    >>> num_matched(build_regex_tree('(1.2)'), '12012')
    (2, True)
    >>> num_matched(build_regex_tree('(1.2)'), '21012')
    (0, False)
    >>> num_matched(build_regex_tree('(1.2)'), '1')
    (0, False)
    >>> num_matched(build_regex_tree('(1|2)'), '12121200012')
    (1, True)
    >>> num_matched(build_regex_tree('(1|2)'), '21121200012')
    (1, True)
    >>> num_matched(build_regex_tree('(1|2)'), '02121200012')
    (0, False)
    >>> num_matched(build_regex_tree('(1*|e)'), '111')
    (3, True)
    >>> num_matched(build_regex_tree('(1*|e)'), '222')
    (0, True)
    >>> num_matched(build_regex_tree('1****'), '111212100')
    (3, True)
    >>> num_matched(build_regex_tree('1****'), '111')
    (3, True)
    >>> num_matched(build_regex_tree('2****'), '111212100')
    (0, True)
    >>> num_matched(build_regex_tree('1****'), '')
    (0, True)
    >>> num_matched(build_regex_tree('e'), '')
    (0, True)
    '''
    # Base case: if r represents 'e'
    if(r.symbol == 'e'):
        # e dosen't match any characters, but it always succeeds
        return (0, True)

    # Base case: if r represents '0', '1', or '2'
    elif(r.symbol in {'0', '1', '2'}):
        # If the zeroth character of s matches the regex symbol,
        # one character is successfuly matched
        if(r.symbol == s[:1]):
            return (1, True)
        # Otherwise, the match fails
        else:
            return (0, False)

    # Recursive decomposition:

    # r represents '*' operator
    elif(r.symbol == '*'):
        # Try to match child with string
        (num_chars_matched, match_success) = num_matched(r.children[0], s)
        # Keep track of total number of characters already matched
        total_match = num_chars_matched
        # Keep trying to match if at least one character matched the last time
        while(num_chars_matched > 0):
            # Don't include the characters in s that are already matched
            (num_chars_matched, match_success) = \
                num_matched(r.children[0], s[total_match:])
            # Keep track of total
            total_match += num_chars_matched
        # Return the total number of characters matched
        # Always considered a success, even if no characters are matched
        return (total_match, True)

    # r represents '|' operator
    elif(r.symbol == '|'):
        # Match left and right child with string
        (l_num_matched, l_success) = num_matched(r.children[0], s)
        (r_num_matched, r_success) = num_matched(r.children[1], s)
        # if both children match, find out which one matched more characters
        # and return its num_matched
        if(l_success and r_success):
            return (max((l_num_matched, r_num_matched)), True)
        # if one of the children match, return its num_matched
        elif(l_success):
            return (l_num_matched, True)
        elif(r_success):
            return (r_num_matched, True)
        # Otherwise, the match failed
        else:
            return (0, False)

    # r represents '.' operator
    elif(r.symbol == '.'):
        # Match left child with string
        (l_num_matched, l_success) = num_matched(r.children[0], s)
        # if left child did not match, then there can't be a match for r
        if(not l_success):
            return (0, False)
        else:
            # Match right child with string, excluding the characters
            # already matched by left child
            (r_num_matched, r_success) = \
                num_matched(r.children[1], s[l_num_matched:])
            # if right child matched, return the total number of characters
            # matched by left and right child.
            # if not, the match failed
            if(r_success):
                return ((l_num_matched + r_num_matched), True)
            else:
                return (0, False)

    # Unsupported operator
    else:
        return (0, False)


def build_regex_tree(regex):
    '''(str) -> RegexTree
    Based on the given regular expression store it in a RegexTree
    Return the root

    REQ: regex must be a valid regular expression

    >>> build_regex_tree("(((0.1)|e)|(e.0*))") == 
    ... BarTree(BarTree(BarTree(DotTree(Leaf('0')), Leaf('1')), Leaf('e')), \
    ... DotTree(Leaf('e'), StarTree(Leaf('0'))))
    True
    '''
    # determine whether it is a valid regex expression
    if not is_regex(regex):
        raise ValueError('not valid regex expression')

    # first: base case -> only one symbol in the string
    if len(regex) == 1:
        # store the symbol in the Leaf and return it
        return Leaf(regex)

    # recursive step
    # expression ends with '*'
    elif regex[-1] == '*':
        # build the StarTree and store the data
        return StarTree(build_regex_tree(regex[:-1]))

    # regex starts and ends with '(' and ')'
    else:
        # break the regex 
        (left, right, operator) = str_deconstruct(regex)
        # find the right type of tree
        if operator == '.':
            tree_type = DotTree
        else:
            tree_type = BarTree
        # put the left part and the right part into the recursive call
        return tree_type(build_regex_tree(left),
                               build_regex_tree(right))
