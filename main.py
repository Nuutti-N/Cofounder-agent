from agent import agent

print("Welcome")


def loop():
    history = []
    while True:
        message = input("You: ")
        response = agent(message, history)
        history.append({"role": "user", "parts": [{"text": message}]})
        history.append({"role":  "model", "parts": [{"text": response}]})
        print(response)


loop()
