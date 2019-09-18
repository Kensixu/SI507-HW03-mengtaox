def my_function():
    question = input("What is your question?")
<<<<<<< HEAD
    return question


while True:
    ques = my_function()
    if ques[-1] == "?":
        print("Yes, it's a question.")
        break
    elif ques == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions.")
=======
    print(question)
my_function()

magic_answer = ["It is certain.", "It is decidedly so.", "Without a doubt", "Yes - definitely.", "You may rely on it.", 
"As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", 
"Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", 
"Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
answer_pick = magic_answer[random.randint(0, len(magic_answer)-1)]
>>>>>>> caccef8565e31b05524fe6427bd011e2870685c3
