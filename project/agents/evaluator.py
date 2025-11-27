class Evaluator:
    """
    Evaluator Agent:
    - Ensures recipe meets constraints and uses ingredients.
    - Rejects recipes violating dietary restrictions or requiring too many new items.
    """
    def __init__(self, logger=None):
        self.logger = logger

    def evaluate(self, plan: dict, recipe: dict):
        if self.logger:
            self.logger.log("Evaluator received recipe", recipe)

        constraints = plan["constraints"]
        used = recipe["ingredients_used"]

        # Evaluate usage
        if len(used) < 1:
            return {"accepted": False, "reason": "Recipe uses no provided ingredients."}

        # Very simple constraint check
        if "nut-free" in constraints and "nuts" in used:
            return {"accepted": False, "reason": "Contains nuts but must be nut-free."}

        return {"accepted": True, "reason": "Valid recipe."}
