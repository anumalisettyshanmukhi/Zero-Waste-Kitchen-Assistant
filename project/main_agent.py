from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.memory.session_memory import SessionMemory
from project.core.context_engineering import ContextEngineer
from project.core.observability import Logger
from project.core.a2a_protocol import A2AProtocol

class MainAgent:
    def __init__(self):
        self.memory = SessionMemory()
        self.context_engineer = ContextEngineer()
        self.logger = Logger()
        self.protocol = A2AProtocol()

        self.planner = Planner(memory=self.memory, logger=self.logger)
        self.worker = Worker(logger=self.logger)
        self.evaluator = Evaluator(logger=self.logger)

    def handle_message(self, user_input: str):
        ctx = self.context_engineer.build_context(user_input)

        plan = self.protocol.pass_plan(self.planner.plan(ctx["raw_input"]))
        recipe = self.protocol.pass_recipe(self.worker.work(plan))
        evaluation = self.protocol.pass_evaluation(self.evaluator.evaluate(plan, recipe))

        if evaluation["accepted"]:
            response = f"Here is your recipe:\n{recipe}"
        else:
            response = f"Recipe rejected: {evaluation['reason']}"

        return {"response": response}

def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]
