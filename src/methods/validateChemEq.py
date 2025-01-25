"""
Scripts to validate chemical equation strings.

Functions:
    validateChemicalEquation(raw_input) -> boolean
    validateSide(raw_input) -> boolean
    validateTerm(raw_input) -> boolean
"""

def validateChemicalEquation(raw_input):
    """
    Check that the input string satisfies specific criteria.
    
    Criteria:
        - The input only contains " ", "+", ":", "(", ")", and letters and numbers
        - There is exactly one ":" separating the reactant and product sides of the equation
        - If there is whitespace between two letters, there is also a "+"
        - Terms begin with uppercase letters
        - Parentheses are balanced
        - Substrings from lowercase to earliest uppercase (right->left) contain only alphabetical characters
        (For a lowercase character, there is an unbroken string of letters to the left that contains an uppercase letter)
    Higher-level conditions, such solvability or valid chemical expressions, 
    require processing so they will be caught later in the program.
    Arguments:
        raw_input: [str]
    Returns: 
        True [boolean]: if raw_input meets conditions
        False [boolean]: if raw_input doesn't meet conditions
    """
    # Checks for illegal characters
    legal_characters = ([32, 40, 41, 43, 58] + [i for i in range(97, 122)] + 
                        [i for i in range(65, 91)] + [i for i in range(48, 58)])
    for idx in range(len(raw_input)):
        char = raw_input[idx]
        if not ord(char) in legal_characters:
            print(f"Invalid String: Contains illegal character '{char}' at index {idx}")
            return False
    # Checks there are two sides of an equation separated by ":"
    sides = raw_input.split(":")
    if len(sides) != 2:
        print(f"Invalid String: There are not two sides of an equation separated by ':'")
        return False
    sides = [i.strip() for i in sides]
    # Side-level validation
    for side_idx in range(2):
        if not validateSide(sides[side_idx]):
            return False
    return True

def validateSide(raw_input):
    """
    Check that input satisfies specific criteria.
    
    Returns True/False if the input string satisfies the following criteria:
        - If there is whitespace between two letters, there is also a "+"
        - Terms begin with uppercase letters
        - Parentheses are balanced
        - Substrings from lowercase to earliest uppercase (right->left) contain only alphabetical characters
        (For a lowercase character, there is an unbroken string of letters to the left that contains an uppercase letter)
    Arguments:
        raw_input: side of equation [str]
    Returns: 
        True [boolean]: if raw_input meets conditions
        False [boolean]: if raw_input doesn't meet conditions
    """
    # Checks if "+" between all terms on side
    term = raw_input.split("+")
    term = [i.strip() for i in raw_input.split("+") if i] # ignore possibly empty
    for term_idx in range(len(term)):
        tmp = term[term_idx]   
        # Checks if a term contains a space
        if " " in tmp:
            print(f"Invalid String: Terms '{tmp}' are not properly joined")
            return False
        #Term-level validation
        if not validateTerm(tmp):
            return False
    return True
        
def validateTerm(raw_string_term):
    term = raw_string_term
    """
    Check that input satisfies specific criteria.
    
    Returns True/False if the input string satisfies the all following criteria:
        - Terms begin with uppercase letter or opening parenthesis
        - Parentheses are balanced
        - Substrings from lowercase to earliest uppercase (right->left) contain only alphabetical characters
        (For a lowercase character, there is an unbroken string of letters to the left that contains an uppercase letter)
    Arguments:
        raw_input: term in equation [str]
    Returns: 
        True [boolean]: if raw_input meets conditions
        False [boolean]: if raw_input doesn't meet conditions
    """
    term.strip()
    # Check that term begins with uppercase-letter or opening parenthesis
    if not (term[0].isupper() or term[0]=="("):
        print(f"Invalid String: Term '{term}'does not begin with an uppercase letter")
        return False
    # Checks that term contains balanced parentheses
    if term.count('(') != term.count(')'):
        print(f"Invalid String: Term '{term}' has unbalanced parentheses")
        return False
    # Check that substrings from lowercase to nearest uppercase  (right->left) contain only alphabetic characters
    upper_idxs = [idx for idx, chr in enumerate(term) if chr.isupper()]
    char_idx = len(term)-1
    while char_idx >= 0:
        if term[char_idx].islower():
            try:
                nearest_idx = list(filter(lambda a : a < char_idx, upper_idxs))[-1]
            except IndexError:
                nearest_idx = 0
            sub = term[nearest_idx:char_idx+1]
            if not sub.isalpha():
                print(f"Invalid String: Term '{term}' has invalid element in '{sub}'")
                return False
            char_idx = nearest_idx
        char_idx -= 1
    return True