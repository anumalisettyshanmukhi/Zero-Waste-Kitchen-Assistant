from project.main_agent import run_agent

def app_interface(user_input: str):
    return run_agent(user_input)

if __name__ == "__main__":
    print(app_interface("Use tomatoes, garlic. Vegan."))
