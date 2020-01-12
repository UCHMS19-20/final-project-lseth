import random

walk_messages = [
    'That rock looks familiar...', 
    "It feels like it's been hours... but the sun hasn't moved...",
    'Your legs begin to hurt',
    'Whose tracks are those?',
    "What are those noises? They've been getting closer. "
]

affirm_resp = ['yes']
neg_resp = ['no']

def 
    response = input(" \n").lower()
    while response not in :
        response = input("\n").lower()
    if response in :
        return True
    else:
        return False

def leave_plane
    response = input('As your sight begins to clear, you see a black column raising from the plane. You smell something acrid, do you leave the plane? Yes or no. \n').lower()
    while response not in affirm_resp or neg_resp:
        response = input("This is important. It's a time sensitive crucical decision. Do you walk away from the plane, yes or no?\n").lower()
    if response in affirm_resp:
        return True
    else:
        return False
    
up_wind = ['upwind', 'up']
down_wind = ['downwind', 'down']

def up_down_wind
    response = input("As you walk away, you hear a defeaning explosion. It was a good thing you left or you'd be a goner. Good choice. The plane exploded. Now as you leave, do you want to go up or downwind? \n").lower()
    while response not in up_wind or down_wind:
        response = input('Up or downwind? \n').lower()
    if response in up_wind:
        return True
    else:
        return False

def follow_river
    response = input("Good. That was toxic smoke from the plane. You see a river. You always heard how rivers lead to civilization. Or was it to avoid them because the terrain could get dangerous? You can't quite remember but you need to decide. Do you follow the river, yes or no? \n").lower()
    while response not in affirm_resp or neg_resp:
        response = input("You can't not decide. \n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

def catch_fish
    response = input("What you didn't know is that the river ends up being a gorge and you would have most likely been trapped and died. Wait... you're getting hungry. You remember seeing fish in the river. Do you want to go back to try and catch one? Yes or no. \n").lower()
    while response not in affirm_resp or neg_resp:
        response = input("Do you want to try to catch a fish? \n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

hands = ['hands', 'barehands', 'use my hands', 'use your hands', 'use hands', 'try to use my hands']
spear = ['spear', 'make spear', 'make a spear', 'try to make a spear', 'try spear', 'a spear']
def hands_spear
    response = input("You return to the neareast section of river. You see a lot of fish. Do you try to use your hands or make a spear? \n").lower()
    while response not in hands or spear:
        response = input("You get a little confused. Maybe you're still a little confused. This time you try to decide in simpler terms. Maybe one word, hands or a spear?\n").lower()
    if response in hands:
        return True
    else:
        return True

raw = ['raw', 'salmonell baybey', 'salmonella', 'sam on ella', "don't cook it", "dont cook it", 'eat it raw']
cook = ['cook', 'cook it', 'try cooking it', 'i cook it', 'fire', 'my mixtape']
def raw_cook
    response = input("Wow, it worked! You feel like Tarzan. You have a slippery fish in your hands. You almost drop it, but don't. Now, do you just eat it raw or try to cook it?\n").lower()
    while response not in :
        response = input("You focused so much on catching the fish. You're so excited, all you think about is eat it raw or cook it?\n").lower()
    if response in raw:
        return True
    else:
        return False

clothes = ['clothes', 'my clothes', 'the clothes', 'try to use my clothes']
wood = ['wood', 'wood nearby', 'nearby wood', 'try to find food nearby']
def fire
    response = input("You may be in the wilderness, but even these waters have been polluted by humans. Good choice. Now you just need some kindling to start the fire. You have your clothes or you can try to find wood nearby. Which do you choose? Wood or clothes? \n").lower()
    while response not in clothes or wood :
        response = input("You got a little dizzy catching the fish. Try to stick to just clothes or wood. \n").lower()
    if response in clothes:
        return True
    else:
        return False

def berries
    response = input("Now, do you try to find berries? You think you remember your scout training on how to tell if a berry is poisonous\n").lower()
    while response not in affirm_resp or neg_resp:
        response = input("This is a simple decision and needs a simple answer. Do you try to scavenge berries?\n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

while true 
    print walk message
    if 'secret word' then break

#game

#leave plane is true and survival
plane_ch = leave_plane
#upwind is true and survive
#downwind is false and death
wind_ch = up_down_wind
#follow river is true and death
#leave river is false and survive
#need to leave river w false to survive
river_ch = follow_river
fish_ch = catch_fish
#hands and spear are both true, it doesn't matter. they both succeed
hand_spear_ch = hands_spear
#raw is true
#cooked is false and goes to fire
raw_cook_ch = raw_cook
#clothes is true and death
#wood is false and also death
fire_ch = fire
#getting berries is true and death
berries_ch = berries