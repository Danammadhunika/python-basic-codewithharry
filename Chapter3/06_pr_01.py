letter ='''Dear <|Name|>,
Greetings for ABC coding house. I am happy to tell you about your sec
You are selected!
Have a great day ahead!
Thanks regards
Date: <|Date|>'''
name = input("Enter name\n")
date = input("Enter date\n")
letter =letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)