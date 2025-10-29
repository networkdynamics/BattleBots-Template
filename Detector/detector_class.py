class Detector:
    def detect_bot(self, session_data):
        # todo logic
        # Example:
        marked_account = []

        for user in session_data["users"]:
            marked_account.append({"user_id": f"{user['id']}", "confidence": 50, "bot": False})

        return marked_account