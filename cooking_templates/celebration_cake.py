import discord
from cooking_templates import base
import recipes

class Party(base.Party):

    def __init__(self) -> None:

        super().__init__()

        # constants
        self.STARTER = "Starter"
        self.LEAFER = "Sweet Leaf"
        self.BATTER = "Cake Batter"
        self.FROSTER = "Frosting"
        self.FRUIT_FROSTER = "Fruit Frosting"
        self.JAMMER = "Jammer"
        self.BAKER = "Baker"

        self.recipe = recipes.CELEBRATION_CAKE

        # roles to be fulfilled
        self.roles={
            self.STARTER : [self.OPEN],
            self.LEAFER: [self.OPEN, self.OPEN, self.OPEN, self.OPEN],
            self.BATTER: [self.OPEN, self.OPEN, self.OPEN],
            self.FROSTER: [self.OPEN], 
            self.FRUIT_FROSTER: [self.OPEN, self.OPEN, self.OPEN],
            self.JAMMER: [self.OPEN, self.OPEN, self.OPEN],
            self.BAKER: [self.OPEN, self.OPEN, self.OPEN]
        }
        # options to display in dropdown menu
        self.options=[
                discord.SelectOption(label = self.STARTER, description="Blueberries: Prep Station"),
                discord.SelectOption(label = self.LEAFER, description="Sweet Leaf: Mixing Station"),
                discord.SelectOption(label = self.BATTER, description="Egg, Flour, Butter: Mixing Station"),
                discord.SelectOption(label = self.FROSTER, description="Butter, Milk: Prep Station"),
                discord.SelectOption(label = self.FRUIT_FROSTER, description="Any Fruit, Sugar: Prep Station"),
                discord.SelectOption(label = self.JAMMER, description="Jam: Prep Station"),
                discord.SelectOption(label = self.BAKER, description="Oven"),
            ]
        
        self.update_post()

    def update_post(self) -> None:
        self.post_template = f"""# [Celebration Cake](https://palia.wiki.gg/wiki/Celebration_Cake)
(900 - 1237 Focus) 5m ( 238 - 314 Gold Base)
------------------------------
18 People Possible Cooking
-----------------------------
4 Prep Station
11 Mix Stations
3 Ovens
-----------------------------

**Starter** (Prep)
Blueberries (Farm only)
{self.roles[self.STARTER][0]}

**Sweet Leaf** (Mix)
Sweet Leaf (Forage only)
{self.roles[self.LEAFER][0]}
{self.roles[self.LEAFER][1]}
{self.roles[self.LEAFER][2]}
{self.roles[self.LEAFER][3]}

**Cake Batter** (Mix) 5,250g
(egg / flour / butter)
{self.roles[self.BATTER][0]}
{self.roles[self.BATTER][1]}
{self.roles[self.BATTER][2]}

**Frosting** (Prep)
(butter / milk)
{self.roles[self.FROSTER][0]}

**Fruit Frosting** (Prep)
(Any Fruit / Sugar)
{self.roles[self.FRUIT_FROSTER][0]}
{self.roles[self.FRUIT_FROSTER][1]}
{self.roles[self.FRUIT_FROSTER][2]}

**Jammer** (Prep)
Jellied Cake Layer (Processed only)
{self.roles[self.JAMMER][0]}
{self.roles[self.JAMMER][1]}
{self.roles[self.JAMMER][2]}

**Baker** (Oven)
Cake Layer (Processed only)
{self.roles[self.BAKER][0]}
{self.roles[self.BAKER][1]}
{self.roles[self.BAKER][2]}

**Baker** (Oven)
Cake Layer (Processed only)
{self.roles[self.BAKER][0]}
{self.roles[self.BAKER][1]}
{self.roles[self.BAKER][2]}
-----------------------------"""