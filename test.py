class Users:
    def __init__(self):
        self.users = []

    def setUser(self, sender_id, status):
        self.users.append(dict({"sender_id": sender_id, "status": status}))

    def getUser(self, sender_id):
        return [user for user in self.users if user['sender_id'] == sender_id]

    def removeUser(self, sender_id):
        self.users = [user for user in self.users if user['sender_id'] != sender_id]

    def updateStatus(self, sender_id, status):
        for user in self.users:
            if user.get('sender_id') == sender_id:
                user.update(dict({'sender_id': sender_id, 'status': status}))


if __name__ == "__main__":
    users = Users()
    users.setUser("123", 0)
    users.setUser("124", 0)
    users.updateStatus("123", 1)
    # users.removeUser("124")
    try:
        users.getUser("123")[0].get('sender_id')
    except IndexError:
        users.setUser("123", 0)
    print(users.getUser("123"))