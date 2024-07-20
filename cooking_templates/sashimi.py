import discord
from cooking_templates import base
import recipes

class Party(base.Party):

    def __init__(self) -> None:

        super().__init__()

        # constants
        self.STARTER = "Starter"
        self.FISH = "Fish"
        self.RICE = "Rice"

        self.recipe = recipes.CELEBRATION_CAKE

        # roles to be fulfilled
        self.roles={
            self.STARTER : [self.OPEN],
            self.FISH : [self.OPEN],
            self.RICE : [self.OPEN],
        }
        # options to display in dropdown menu
        self.options=[
                discord.SelectOption(label = self.STARTER, description="Spice Sprouts: Prep Station"),
                discord.SelectOption(label = self.FISH, description="Any Fish: Prep Station"),
                discord.SelectOption(label = self.RICE, description="Stove"),
            ]
        
        self.update_post()

    def update_post(self) -> None:
        self.post_template = f"""# [Sashimi](https://palia.wiki.gg/wiki/Sashimi)
(100 Focus Base) 1m ( 92-677 Gold Base)
------------------------------
3 People Possible Cooking
-----------------------------
2 Prep Station
1 Stove Station
-----------------------------

**Starter** (Prep)
Spice Sprouts (30g each/Forage)
{self.roles[self.STARTER][0]}

**Any Fish** (Prep)
(Fishing Only)
{self.roles[self.FISH][0]}

**Rice** (Stove)
(105g each/Farm)
{self.roles[self.RICE][0]}
-----------------------------"""