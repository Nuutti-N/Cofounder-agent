from agent import agent

print("Welcome")


def loop():
    while True:
        message = input("You: ")
        response = agent(message)
        print(response)


loop()
