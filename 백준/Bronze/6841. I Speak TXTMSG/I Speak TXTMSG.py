def translate_text():
    translation_table = {
        "CU": "see you",
        ":-)": "I’m happy",
        ":-(": "I’m unhappy",
        ";-)": "wink",
        ":-P": "stick out my tongue",
        "(~.~)": "sleepy",
        "TA": "totally awesome",
        "CCC": "Canadian Computing Competition",
        "CUZ": "because",
        "TY": "thank-you",
        "YW": "you’re welcome",
        "TTYL": "talk to you later"
    }
    
    while True:
        user_input = input()
        if user_input in translation_table:
            print(translation_table[user_input])
        else:
            print(user_input)
        
        if user_input == "TTYL":
            break

translate_text()
