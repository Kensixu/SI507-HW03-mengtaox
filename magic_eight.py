def my_function():
    question = input("What is your question?")
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
