import discord
from cooking_templates import base
import recipes

class Party(base.Party):

    def __init__(self) -> None:

        super().__init__()

        # constants
        self.STARTER = "Starter"
        self.SPICE_SPROUTS = "Spice Sprouts"
        self.WHEAT = "Wheat"
        self.BLUEBERRY = "Blueberry"
        self.LEAFER = "Sweet Leaf"
        self.BAKER = "Baker"

        self.recipe = recipes.CELEBRATION_CAKE

        # roles to be fulfilled
        self.roles={
            self.STARTER : [self.OPEN],
            self.SPICE_SPROUTS: [self.OPEN],
            self.WHEAT: [self.OPEN], 
            self.BLUEBERRY: [self.OPEN],
            self.LEAFER: [self.OPEN],
            self.BAKER: [self.OPEN]
        }
        # options to display in dropdown menu
        self.options=[
                discord.SelectOption(label = self.STARTER, description="Butter: Oven"),
                discord.SelectOption(label = self.SPICE_SPROUTS, description="Prep Station"),
                discord.SelectOption(label = self.WHEAT, description="Prep Station"),
                discord.SelectOption(label = self.BLUEBERRY, description="Mixing Station"),
                discord.SelectOption(label = self.LEAFER, description="Sweet Leaf: Mixing Station"),
                discord.SelectOption(label = self.BAKER, description="Oven"),
            ]
        
        self.update_post()

    def update_post(self) -> None:
        self.post_template = f"""# [Blueberry Pie](https://palia.wiki.gg/wiki/Blueberry_Pie) x50
(250 Focus Base) 1m 40s (90 Gold Base)
------------------------------
6 People Possible Cooking
-----------------------------
2 Prep Station
2 Mixing Station
1 Oven Station
-----------------------------
**Starter** (Oven)
butter (80g each)
{self.roles[self.STARTER][0]}

**Spice Sprouts** (Prep)
(30g each/Forage)
{self.roles[self.SPICE_SPROUTS][0]}

**Wheat** (Prep)
(130g each/Farm)
{self.roles[self.WHEAT][0]}

**Blueberry** (Mix)
(Farm only)
{self.roles[self.BLUEBERRY][0]}

**Sweetleaf** (Mix)
(Forage only)
{self.roles[self.LEAFER][0]}

**Baker** (Oven)
{self.roles[self.BAKER][0]}
-----------------------------"""