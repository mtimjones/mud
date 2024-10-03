from world import World
from threading import Thread, Lock

class Player:

    def __init__(self, socket) -> None:

        self.client_socket = socket
        self.state = 0
        self.world = World()
        self.username = None
        self.password = None
        self.json = self.world.get()
        self.send_mutex = Lock()


    def send_response(self, message):

        with self.send_mutex:
            self.client_socket.send(message.encode())


    def interact(self, message) -> None:

        self.route(message)


    def route(self, message):

        if self.state in range(0,10):
            self.login(message)

        elif self.state in range(10, 20):
            self.newchar(message)

        elif self.state in range(20,30):
            self.play(message)


    def login(self, message):

        if self.state == 0:
            self.send_response("Enter 'new' to create a new character, or your username.\n\r")
            self.state = 1

        elif self.state == 1:
            if message == "new":
                #Create a new character
                self.send_response("Enter your character's name: \n\r")
                self.state = 10
            else:
                found = False
                for users in self.json['entities']:
                    if users['username'] == message:
                        found = True
                        self.username = message
                        self.send_response("Enter your password\n\r")
                        self.state = 9

                if not found:
                    response = f"User {message} not found.\n\r Enter your username or 'new' to create a new character.\n\r"
                    self.send_response(response)
                    self.state = 0

        elif self.state == 9:
            found = False
            for users in self.json['entities']:
                if users['password'] == message:
                    found = True
                    self.password = message
                    self.send_response("You are now logged in.\n\r")
                    self.state = 20
                    self.play("")

            if not found:
                response = f"Password failed.\n\rEnter your username or 'new' to create a new character.\n\r"
                self.send_response(response)
                self.state = 0


    def newchar(self, message):

        self.send_response("We're here for new char.\n\r")

        # Make sure that the player doens't exist.

        # If so, request the password.

        # Otherwise, return to self.state = 0

        pass


    def play(self, message):

        self.send_response("Reached play\n\r")


