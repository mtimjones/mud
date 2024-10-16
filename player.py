from world import World
from threading import Thread, Lock
from enum import IntEnum

class pstate(IntEnum):
    Init = 1
    Get_Character_Name = 2
    Get_Character_Password = 9
    xxLogin = 9

    New_Character_Creation = 10
    xxNew = 19

    Logged_In = 20
    xxPlay = 29


class Player:

    def __init__(self, socket) -> None:

        self.client_socket = socket
        self.state:pstate = pstate.Init
        self.username = None
        self.password = None
        self.world = World()
        self.json = self.world.get()
        self.send_mutex = Lock()


    def send_response(self, message):

        with self.send_mutex:
            self.client_socket.send(message.encode())


    def interact(self, message) -> None:

        self.route(message)


    def route(self, message):

        if self.state <= pstate.xxLogin:
            self.login(message)

        elif self.state <= pstate.xxNew:
            self.newchar(message)

        elif self.state <= pstate.xxPlay:
            self.play(message)


    def login(self, message):

        if self.state == pstate.Init:
            self.send_response("Enter 'new' to create a new character, or your username: ")
            self.state = pstate.Get_Character_Name

        elif self.state == pstate.Get_Character_Name:
            if message == "new":
                #Create a new character
                self.send_response("\n\rEnter your character's name: ")
                self.state = pstate.New_Character_Creation
            else:
                found = False
                for user in self.json['entities']:
                    if user['username'] == message:
                        found = True
                        self.username = message
                        self.send_response("\n\rEnter your password: ")
                        self.state = pstate.Get_Character_Password

                if not found:
                    response = f"\n\rUser {message} not found.\n\rEnter your username or 'new' to create a new character: "
                    self.send_response(response)
                    self.state = pstate.Init

        elif self.state == pstate.Get_Character_Password:
            found = False
            for user in self.json['entities']:
                if user['password'] == message:
                    found = True
                    self.entity = user
                    self.password = message
                    self.send_response("\n\rYou are now logged in.  Type 'help' for help.\n\r\n\r")
                    self.state = pstate.Logged_In
                    self.entity['loggedin'] = True
                    self.player_look()

            if not found:
                response = f"\n\rPassword failed.\n\rEnter your username or 'new' to create a new character:"
                self.send_response(response)
                self.state = pstate.Init


    def newchar(self, message):

        self.send_response("\n\rWe're here for new char.\n\r")

        # Make sure that the player doens't exist.

        # If so, request the password.

        # Otherwise, return to self.state = pstate.Init

        pass


    def play(self, message):

        if message == 'look':
            self.player_look()
        elif message == 'n' or message == 'north':
            self.player_move('north')
        elif message == 's' or message == 'south':
            self.player_move('south')
        elif message == 'w' or message == 'west':
            self.player_move('west')
        elif message == 'e' or message == 'east':
            self.player_move('east')
        elif message == 'i' or message == 'inventory':
            self.player_inventory()
        elif message == 'help':
            self.player_help()
        else:
            self.send_response(f"Command {message} not understood.")
            self.player_help()


    def player_look(self):

        for room in self.json['rooms']:
            if self.entity['location'] == room['name']:
                self.world.take()
                self.send_response(f"{room['description']}\n\r\n\r");

                self.send_response("   Exits are ")
                for key in room['exits']:
                    self.send_response(f"{key} ")
                self.send_response("\n\r")

                self.send_response("   Items here: ")
                for item in room['items']:
                    self.send_response(f"{item['name']}, ")
                self.send_response("\r\n")

                self.send_response("   Players here: ")
                for player in self.json['entities']:
                    if player["location"] == room['name']:
                        self.send_response(f"{player["username"]},")
                self.send_response("\r\n\n\r")
                self.world.give()


    def player_help(self):

        pass


    def player_move(self, direction):

        pass


    def player_inventory(self):

        self.send_response("   Items: ")
        for item in self.entity['items']:
            self.send_response(f"{item['name']}, ")
        self.send_response("\n\r\n\r")


    def player_take(self):
        pass


    def logout(self):
        self.entity['loggedin'] = False
