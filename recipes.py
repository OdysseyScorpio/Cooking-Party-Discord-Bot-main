import discord
from cooking_templates import *

CELEBRATION_CAKE = "Celebration Cake"
CHILI_OIL_DUMPLINGS = "Chili Oil Dumplings"
SASHIMI = "Sashimi"
BLUEBERRY_PIE = "Blueberry Pie"
VEGGIE_FRIED_RICE = "Veggie Fried Rice"
TROUT_DINNER = "Trout Dinner"
STEAK_DINNER = "Steak Dinner"
SUSHI = "Sushi"
SERNUK_NOODLE_STEW = "Sernuk Noodle Stew"
RAMEN = "Ramen"
PALIAN_ONION_SOUP = "Palian Onion Soup"
MEATY_STIR_FRY = "Meaty Stir Fry"
MACARON = "Macaron"
LOADED_POTATO_SOUP = "Loaded Potato Soup"
HEARTY_VEGETABLE_SOUP = "Hearty Vegetable Soup"
FRIED_CATFISH_DINNER = "Fried Catfish Dinner"
FISH_STEW = "Fish Stew"
CREAMY_CARROT_SOUP = "Creamy Carrot Soup"
CREAM_OF_TOMATO_SOUP = "Cream of Tomato Soup"
CREAM_OF_MUSHROOM_SOUP = "Cream of Mushroom Soup"
CHAPPA_MASALA = "Chappa Masala"
BOUILLABAISSE = "Bouillabaisse"
APPLE_PIE = "Apple Pie"
BACON_STUFFED_MUSHROOMS = "Bacon-Stuffed Mushrooms"
AKWINDU_CHAPPA = "Akwindu Chappa"

options = [discord.SelectOption(label = CELEBRATION_CAKE),
                  discord.SelectOption(label = CHILI_OIL_DUMPLINGS),
                  discord.SelectOption(label = SASHIMI),
                  discord.SelectOption(label = BLUEBERRY_PIE),
                  discord.SelectOption(label = VEGGIE_FRIED_RICE),
                  discord.SelectOption(label = TROUT_DINNER),
                  discord.SelectOption(label = STEAK_DINNER),
                  discord.SelectOption(label = SUSHI),
                  discord.SelectOption(label = SERNUK_NOODLE_STEW),
                  discord.SelectOption(label = RAMEN),
                  discord.SelectOption(label = PALIAN_ONION_SOUP),
                  discord.SelectOption(label = MEATY_STIR_FRY),
                  discord.SelectOption(label = MACARON),
                  discord.SelectOption(label = LOADED_POTATO_SOUP),
                  discord.SelectOption(label = HEARTY_VEGETABLE_SOUP),
                  discord.SelectOption(label = FRIED_CATFISH_DINNER),
                  discord.SelectOption(label = FISH_STEW),
                  discord.SelectOption(label = CREAMY_CARROT_SOUP),
                  discord.SelectOption(label = CREAM_OF_TOMATO_SOUP),
                  discord.SelectOption(label = CREAM_OF_MUSHROOM_SOUP),
                  discord.SelectOption(label = CHAPPA_MASALA),
                  discord.SelectOption(label = BOUILLABAISSE),
                  discord.SelectOption(label = APPLE_PIE),
                  discord.SelectOption(label = BACON_STUFFED_MUSHROOMS),
                  discord.SelectOption(label = AKWINDU_CHAPPA),
]

# Returns correct party object based on recipe
# Returns False if recipe not supported
def get_party(recipe) -> base.Party:
    if recipe == CELEBRATION_CAKE: return celebration_cake.Party()
    if recipe == CHILI_OIL_DUMPLINGS: return chili_oil_dumplings.Party()
    if recipe == SASHIMI: return sashimi.Party()
    if recipe == BLUEBERRY_PIE: return blueberry_pie.Party()
    return False
        
        