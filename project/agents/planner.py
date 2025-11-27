
class Planner:
    """
    Planner Agent:
    - Interprets user input (ingredients + constraints).
    - Produces a structured plan: cuisine direction, required search queries,
      dietary rules to enforce, and optimization goal (zero-waste).
    """
    def __init__(self, memory=None, logger=None):
        self.memory = memory
        self.logger = logger

    def plan(self, user_message: str):
        if self.logger:
            self.logger.log("Planner received input", user_message)

        allergies = self.memory.get("allergies", [])
        staples = self.memory.get("staples", ["salt", "oil"])

        # ---- Improved ingredient extraction logic ----
        STOPWORDS = {
            "i","have","and","please","meal","recipe","recipes","make","cook",
            "for","a","the","with","using","use"
        }
        punctuation = ",.!?;:"

        # Step 1: normalize words + strip punctuation
        tokens = [
            w.strip(punctuation).lower()
            for w in user_message.split()
        ]

        # Step 2: detect constraints BEFORE filtering ingredients
        DIET_TAGS = {"vegan", "vegetarian", "nut-free", "gluten-free"}
        constraints = [t for t in tokens if t in DIET_TAGS]

        # Step 3: ingredient detection
        ingredients = [
            t for t in tokens
            if t not in STOPWORDS
            and t not in DIET_TAGS
            and t != ""
        ]

        # Build search query
        plan = {
            "ingredients": ingredients,
            "constraints": constraints,
            "allergies": allergies,
            "staples": staples,
            "search_queries": [
                f"recipes using {', '.join(ingredients)} "
                f"{', '.join(constraints)} zero waste"
            ],
        }

        if self.logger:
            self.logger.log("Planner generated plan", plan)

        return plan

