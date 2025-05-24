import atexit
from Models.AgentState import AgentState
import signal
import sys

# Handle initial startup logic
def startup():
    AgentState.load()
    name = AgentState.get("name")

    if not AgentState or not name:
        print("Welcome to Scheduler! What can I call you? :)")
        name = str(input())
        AgentState.set("name", name)
        AgentState.save()
        print(f"Hi {name}! What can I help you with?")
    else:
        print(f"Welcome back {name}! How can I help?")


# Main event loop for agent command processing
def main():
    is_running = True

    while is_running:
        user_input = str(input())

        if user_input == "quit":
            is_running = False
            print(f"That's it for now, goodbye {AgentState.get('name')}!")


# Register both exit strategies
atexit.register(lambda: AgentState.save())
signal.signal(signal.SIGINT, lambda s, f: (AgentState.save(), sys.exit(0)))
signal.signal(signal.SIGTERM, lambda s, f: (AgentState.save(), sys.exit(0)))


if __name__ == "__main__":
    startup()
    main()