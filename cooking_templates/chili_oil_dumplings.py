import discord
from cooking_templates import base
import recipes

class Party(base.Party):

    def __init__(self) -> None:

        super().__init__()

        # constants
        self.STARTER = "Starter"
        self.SERNUK = "Sernuk Meat"
        self.POTATO = "Potato"
        self.WHEAT = "Wheat"
        self.SPICY_PEPPER = "Spicy Pepper"
        self.RICE = "Rice"
        self.OIL = "Cooking Oil"
        self.MIXER = "Mixer"

        self.recipe = recipes.CELEBRATION_CAKE

        # roles to be fulfilled
        self.roles={
            self.STARTER : [self.OPEN],
            self.SERNUK: [self.OPEN],
            self.POTATO: [self.OPEN],
            self.WHEAT: [self.OPEN], 
            self.SPICY_PEPPER: [self.OPEN],
            self.RICE: [self.OPEN],
            self.OIL: [self.OPEN],
            self.MIXER: [self.OPEN, self.OPEN]
        }
        # options to display in dropdown menu
        self.options=[
                discord.SelectOption(label = self.STARTER, description="Spice Sprouts: Stove"),
                discord.SelectOption(label = self.SERNUK, description="Prep Station"),
                discord.SelectOption(label = self.POTATO, description="Prep Station"),
                discord.SelectOption(label = self.WHEAT, description="Prep Station"),
                discord.SelectOption(label = self.SPICY_PEPPER, description="Prep Station"),
                discord.SelectOption(label = self.RICE, description="Stove"),
                discord.SelectOption(label = self.OIL, description="Mixing Station"),
                discord.SelectOption(label = self.MIXER, description="Mixing Station"),
            ]
        
        self.update_post()

    def update_post(self) -> None:
        self.post_template = f"""# [Chili Oil Dumplings](https://palia.wiki.gg/wiki/Chili_Oil_Dumplings)

(350Focus Base) 3m (76 Gold Base)
-----------------------------------------------
9 People Possible Cooking
-----------------------------------------------
4 Prep Station
2 Stove Station
1 Mix Station 
2 Mixers
-------------------------------------------------
**Starter: (STOVE)**
Spice Sprouts (30ea) - {self.roles[self.STARTER][0]}

-----------------------------------------------
**PREP STATION X4**
STAY OUT OF STATION'S LET (POTATO) GO FIRST

(Sernuk Meat @26ea) - {self.roles[self.SERNUK][0]}

START AND FINISH ONLY 
(Potato @180ea)- {self.roles[self.POTATO][0]}

(Wheat @130ea) - {self.roles[self.WHEAT][0]}

(Spicy Pepper @farming) - {self.roles[self.SPICY_PEPPER][0]}
-----------------------------------------------
**STOVE**

(Rice @105ea)- {self.roles[self.RICE][0]}
-----------------------------------------------
**MIX STATION**

(Cooking oil @20ea)- {self.roles[self.OIL][0]}
-----------------------------------------------
**MIXERS X2**
(Mixer)- {self.roles[self.MIXER][0]}

(Mixer)- {self.roles[self.MIXER][1]}
------------------------------------------------"""