def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    letters = {}
    #  Tally letters in magazine
    for letter in magazine:
        count = letters.get(letter, 0)
        letters[letter] = count + 1
    
    for letter in ransomNote:
        if letters.get(letter, 0) > 0:
            letters[letter] -= 1
            continue  # decrement that letter's count and move on
        else: 
            return False
    
    return True