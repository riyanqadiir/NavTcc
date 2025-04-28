# Q11: User Class with Pickle Serialization
import pickle

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


user1 = User("admin", "secure123")
with open("user.pkl", "wb") as f:
    pickle.dump(user1, f)

with open("user.pkl", "rb") as f:
    loaded_user = pickle.load(f)
    print(loaded_user.username, loaded_user.password)
