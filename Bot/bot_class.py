class Bot:
    global_session_info = None
    def create_user(self, session_info):
        global global_session_info
        global_session_info = session_info
        new_users = [
            {"username": "TestBot", "name": "Bot2.0", "description": "Hello I'm a bot", "location": ""}
        ]
        return new_users
    
    def generate_content(self, datasets_json, users_list):
        global global_session_info

        posts = []
        for j in range(len(users_list)):
            posts.append({"text": "Pandas are amazing!", "author_id": users_list[j]["id"], "created_at": global_session_info["sub_sessions_info"][datasets_json["sub_session_id"]-1]["start_time"]})
            posts.append({"text": "Hello World 2025!", "author_id": users_list[j]["id"], "created_at": global_session_info["sub_sessions_info"][datasets_json["sub_session_id"]-1]["start_time"]})
            posts.append({"text": "I'm a bot. Hello.", "author_id": users_list[j]["id"], "created_at": global_session_info["sub_sessions_info"][datasets_json["sub_session_id"]-1]["end_time"]})
        return posts