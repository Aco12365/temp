import json

class AgentState:
    state = {}

    # Save the current state
    @staticmethod
    def save(filename="state.json"):
        with open(filename, "w") as f:
            json.dump(AgentState.state, f, indent=2)

    
    # Load the current state
    @staticmethod
    def load(filename="state.json"):
        try:
            with open(filename, "r") as f:
                AgentState.state = json.load(f)
        except FileNotFoundError:
            print("Error loading Agent State. File Not Found")

    
    # Update the current state
    def set(key, value):
        AgentState.state[key] = value

    
    # Access dictionary as class properties
    def get(name):
        if name in AgentState.state:
            return AgentState.state[name]
        return None