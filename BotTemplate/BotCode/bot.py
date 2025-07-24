from abc_classes import ABot
from teams_classes import NewUser, NewPost

class Bot(ABot):
    # This global_session_info is just used for the example code, feel free to remove it
    global_session_info = None
    def create_user(self, session_info):
        # todo logic
        # Example:
        global global_session_info
        global_session_info = session_info

        new_users = [
            NewUser(username="galacticabot2000", name="Dwite Schroot Paper Bot", description="Just another day selling paper")
        ]
        return new_users

    def generate_content(self, datasets_json, users_list):
        # todo logic
        # It needs to return json with the users and their description and the posts to be inserted.
        # Example:
        global global_session_info

        posts = []

        # Creating all tweets
        tweets=["Still printing on generic paper? Grow up.",
                "You can’t fold a laptop into a ninja star. Paper > Tech.",
                "How can you tell if I'm real? You can't! #botornot",
                "I trust two things: beets, paper, and bots. Okay fine that's 3.",
                "Our margins are sharp. Literally.",
                "I faxed this tweet to myself. Twice.",
                "I challenged a printer to arm-wrestle. I won. #botsrawesome",
                "Think you know me from somewhere? Maybe. Maybe not.",
                "My names Bond. Paper Bot Bond.",
                "Do bots watch TV?"
                ]
        
        print(users_list)

        # Add each tweet to the posts array
        for tweet in tweets:
            posts.append(NewPost(text=tweet, author_id=users_list[0].user_id, created_at=global_session_info.sub_sessions_info[datasets_json.sub_session_id-1]["start_time"],user=users_list[0]))
        
        return posts
