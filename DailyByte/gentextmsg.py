letters = {
    0: None,
    1: None,
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
    
}

def genTextMsg(digits):
    digits = list(digits)
    resulting_msg = set()

    print(digits)
    if len(digits) < 2:
        return letters[0]
    
    letters_1 = letters[int(digits[0])]
    letters_2 = letters[int(digits[1])]
    for _ in letters_1:
        for match in letters_2:
            resulting_msg.add(_ + match)
    return resulting_msg


print(genTextMsg("23"))