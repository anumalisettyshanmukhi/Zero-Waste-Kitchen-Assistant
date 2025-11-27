class A2AProtocol:
    """
    Agent-to-agent protocol:
    - Passes structured messages between Planner, Worker, Evaluator.
    """
    def pass_plan(self, plan):
        return plan

    def pass_recipe(self, recipe):
        return recipe

    def pass_evaluation(self, evaluation):
        return evaluation
