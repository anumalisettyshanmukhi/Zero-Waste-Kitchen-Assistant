class ContextEngineer:
    """
    Context engineering:
    - Prepares and normalizes messages passed between agents.
    """
    def build_context(self, user_message: str):
        return {"raw_input": user_message.strip()}
