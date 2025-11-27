from project.tools.tools import search_web, calculate_portions

class Worker:
    """
    Worker Agent:
    - Executes the planner's plan.
    - Performs searches, generates draft recipes.
    """
    def __init__(self, logger=None):
        self.logger = logger

    def work(self, plan: dict):
        if self.logger:
            self.logger.log("Worker received plan", plan)

        # Perform search
        query = plan["search_queries"][0]
        search_results = search_web(query)

        # Dummy recipe generation
        recipe = {
            "title": "Zero-Waste Inspired Dish",
            "ingredients_used": plan["ingredients"],
            "instructions": [
                "Mix all leftover ingredients.",
                "Season with pantry staples.",
                "Cook until delicious."
            ],
            "portion_adjusted": calculate_portions(2, 1)
        }

        if self.logger:
            self.logger.log("Worker generated recipe", recipe)

        return recipe
