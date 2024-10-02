from world import World

class Player:

    def __init__(self, socket) -> None:

        self.client_socket = socket
        self.state = 0
        self.world = World()
        self.username = None
        self.password = None

    def send_response(self, message):
        self.client_socket.send(message.encode())


    def interact(self, message) -> None:

        print(f"Got {message}")

        self.route(message)


    def route(self, message):

        if self.state in range(0,10):

            self.login(message)

        elif self.state in range(10,20):

            self.play(message)


    def login(self, message):

        if self.state == 0:
            response = "Enter 'new' to create a new character, or your username. "
            self.send_response(response)
            self.state = 1

        elif self.state == 1:
            if message == "new":
                pass
                #Create a new character
            else:
                self.username = message
                print(f"!!!!username {message}\n")
                # Search for the username
                self.send_response("Enter your password ")
                self.state = 9

        elif self.state == 9:
            self.password = message
            print(f"!!!!password {message}\n")
            # Check password
            self.send_response("You are now logged in\n")
            self.state = 10
            self.play("")
            
    def play(self, message):

        self.send_response("Reached play\n")


