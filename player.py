from world import World

class Player:

    def __init__(self, socket) -> None:

        self.client_socket = socket
        self.state = 0
        self.world = World()
        self.username = None
        self.password = None
        self.json = self.world.get()


    def send_response(self, message):

        self.client_socket.send(message.encode())


    def interact(self, message) -> None:

        self.route(message)


    def route(self, message):

        if self.state in range(0,10):
            self.login(message)

        elif self.state in range(10,20):
            self.play(message)


    def login(self, message):

        if self.state == 0:
            response = "Enter 'new' to create a new character, or your username.\n\r"
            self.send_response(response)
            self.state = 1

        elif self.state == 1:
            if message == "new":
                pass
                #Create a new character
            else:
                found = False
                for users in self.json['entities']:
                    if users['username'] == message:
                        found = True
                        self.username = message
                        self.send_response("Enter your password\n\r")
                        self.state = 9

                if not found:
                    response = f"""User {message} not found.\n\r
                                Enter your username or 'new' to create a new character.\n\r"""
                    self.send_response(response)
                    self.state = 1

        elif self.state == 9:
            found = False
            for users in self.json['entities']:
                if users['password'] == message:
                    found = True
                    self.password = message
                    self.send_response("You are now logged in.\n\r")
                    self.state = 10
                    self.play("")

            if not found:
                response = f"""Password failed.\n\r
                            Enter your username or 'new' to create a new character.\n\r"""
                self.send_response(response)
                self.state = 1


    def play(self, message):

        self.send_response("Reached play\n")




