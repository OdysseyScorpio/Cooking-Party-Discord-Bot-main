class Party:
    def __init__(self) -> None:
        # recipe
        self.recipe = ""

        # signup sheet to update with selected roles
        self.post_template = ""

        # message id of the signup sheet
        self.message_id = 0

        # the thread this party is in
        self.thread = None

        # constants
        self.OPEN = "open"

        # roles to be fulfilled
        self.roles={}

        # options to display in dropdown menu
        self.options=[]
    
    # adds cook to specific role if there is still room
    def add_cook(self, role, name) -> bool:
        for cook in self.roles[role]:
            if cook == self.OPEN:
                self.roles[role][self.roles[role].index(cook)] = name
                return True
        return False

    # removes cook from all roles
    def remove_cook(self, name) -> None:
        for role in self.roles:
            for cook in self.roles[role]:
                if cook == name:
                    self.roles[role][self.roles[role].index(cook)] = self.OPEN

    def remove_role(self, role) -> None:
        #TODO: remove role when it is full
        pass
    
    def add_role(self, role) -> None:
        #TODO: add role when it becomes available again
        pass