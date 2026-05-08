from agent import agent

print("Welcome")


def loop():
    history = []
    while True:
        message = input("You: ")
        response = agent(message)
        history.append({"role": "user", "parts": message})
        history.append({"role":  "model", "parts": response})

        print(response)


loop()
