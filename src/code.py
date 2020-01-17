import random

#This is for the indefinite loop of 'keep walking'. After 8-10 or so, they should be able to figure it out. If not... natural selection. 
walk_messages = [
    'That rock looks familiar...', 
    "It feels like it's been hours... but the sun hasn't moved...",
    'Your legs begin to hurt',
    'Whose tracks are those?',
    "What are those noises? They've been getting closer.",
    "Lap ????? of ?????",
    "They say the definition of insanity is doing the same thing over and over expecting a different result.",
    "You ever think about how, in the grand scheme of things, everything we do is so insignificant?"
    "I like long walks, but not like this.",
    "Maybe I can find Bigfoot and live with him.",
    "If I can figure out where north is, maybe I can find Santa",
    "If I ever get back. I'm moving to the tropics."
]

#This just means when they respond yes or no, which they do quite a few times, I don't have to recreate it each time
affirm_resp = ['yes']
neg_resp = ['no']

""""
I used this to copy and paste after the first 5 or so functions. They all have the same format basically.
def 
    response = input(" \n").lower()
    while response not in _____ and response not in ______:
        response = input("\n").lower()
    if response in :
        return True
    else:
        return False
"""

def leave_plane():
    response = input('As your sight begins to clear, you see a black column rising from the plane. You smell something acrid, do you leave the plane? Yes or no.\n').lower()
    while response not in affirm_resp and response not in neg_resp:
        response = input("This is important. It's a time sensitive crucical decision. Do you walk away from the plane, yes or no?\n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

#I make these each time the answer isn't yes or no. I try to add quite a few options they may respond with but still have it reask with a bit of a clarification in case it doesn't understand their response.  
up_wind = ['upwind', 'up']
down_wind = ['downwind', 'down']
def up_down_wind():
    response = input("As you walk away, you hear a defeaning explosion. It was a good thing you left or you'd be a goner. Good choice. The plane exploded. Now as you leave, do you want to go up or downwind? \n").lower()
    while response not in up_wind and response not in down_wind:
        response = input('Up or downwind? \n').lower()
    if response in up_wind:
        return True
    else:
        return False

def follow_river():
    response = input("Good. That was toxic smoke from the plane. You see a river. You always heard how rivers lead to civilization. Or was it to avoid them because the terrain could get dangerous? You can't quite remember but you need to decide. Do you follow the river, yes or no? \n").lower()
    while response not in affirm_resp and response not in neg_resp:
        response = input("You can't not decide. \n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

def catch_fish():
    response = input("What you didn't know is that the river ends up being a gorge and you would have most likely been trapped and died. Wait... you're getting hungry. You remember seeing fish in the river. Do you want to go back to try and catch one? Yes or no. \n").lower()
    while response not in affirm_resp and response not in neg_resp:
        response = input("Do you want to try to catch a fish? \n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

#same as up or downwind but with more options, i add as many as i can reasonably think of because i don't want it to break the immersion, however limited. 
hands = ['hands', 'barehands', 'use my hands', 'use your hands', 'use hands', 'try to use my hands']
spear = ['spear', 'make spear', 'make a spear', 'try to make a spear', 'try spear', 'a spear']
def hands_spear():
    response = input("You return to the neareast section of river. You see a lot of fish. Do you try to use your hands or make a spear? \n").lower()
    while response not in hands and response not in spear:
        response = input("You get a little confused. Maybe you're still a little confused. This time you try to decide in simpler terms. Maybe one word, hands or a spear?\n").lower()
    if response in hands:
        return True
    else:
        return True

#my mixtape = fire
#fire = needed for cooking
#therefore, by the transitive property
raw = ['raw', 'salmonella baybey', 'salmonella', 'sam on ella', "don't cook it", "dont cook it", 'eat it raw']
cook = ['cook', 'cook it', 'try cooking it', 'i cook it', 'fire', 'my mixtape']
def raw_cook():
    response = input("Wow, it worked! You feel like Tarzan. You have a slippery fish in your hands. You almost drop it, but don't. Now, do you just eat it raw or try to cook it?\n").lower()
    while response not in raw and response not in cook:
        response = input("You focused so much on catching the fish. You're so excited, all you think about is eat it raw or cook it?\n").lower()
    if response in raw:
        return True
    else:
        return False

clothes = ['clothes', 'my clothes', 'the clothes', 'try to use my clothes']
wood = ['wood', 'wood nearby', 'nearby wood', 'try to find food nearby']
def fire():
    response = input("You may be in the wilderness, but even these waters have been polluted by humans. Good choice. Now you just need some kindling to start the fire. You have your clothes or you can try to find wood nearby. Which do you choose? Wood or clothes? \n").lower()
    while response not in clothes and response not in wood:
        response = input("You got a little dizzy catching the fish. Try to stick to just clothes or wood. \n").lower()
    if response in clothes:
        return True
    else:
        return False

def berries():
    response = input("Now, do you try to find berries and eat them? You think you remember your scout training on how to tell if a berry is poisonous.\n").lower()
    while response not in affirm_resp and response not in neg_resp:
        response = input("This is a simple decision and needs a simple answer. Do you try to scavenge berries?\n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

walk = ['walk', 'keep walking', 'keep going', 'walking', 'continue' "don't stop", 'dont stop', 'stopnt', 'sleepnt', "sleepn't", "stopn't"]
sleep = ['sleep', 'go to sleep', 'walknt', 'pause', 'sleep for the night', 'go to sleep for the night', 'stop walking', 'dont walk']
def walk_sleep():
    response = input("You find yourself *yawn* getting *yawn* tired. You know you can't push yourself too much. Do you want to keep walking or sleep for the night?\n").lower()
    while response not in walk and response not in sleep:
        response = input("While it's good to take a pause, you can't stay here forever. Keep walking or go to sleep? \n").lower()
    if response in walk:
        return True
    else:
        return False

igloo = ['an igloo', 'structure', 'lean to', 'leanto', 'build a structure', 'igloo', 'build a igloo', 'build an igloo']
the_open = ['sleep in the open', 'buildnt', 'sleep out in the open', 'open', 'the open']
def igloo_open():
    response = input("Good. Keep up your strength for tomorrow to try to find help. Do you try to make some sort of structure, like an igloo, or do you sleep out in the open?\n").lower()
    while response not in igloo and response not in the_open:
        response = input("Where do you want to sleep? An igloo or the open? \n").lower()
    if response in igloo:
        return True
    else:
        return False

def eat_snow():
    response = input("You collapsed from exhaustion in the middle of the night. Somehow you make it through the night okay. You might have some frostbite in your left hand, but you don't have time to think about that right now. Your mouth feels like sandpaper and you can tell you're dehydrated. You were already a little thirsty when you took off. Do you try to eat snow? \n").lower()
    while response not in affirm_resp and response not in neg_resp:
        response = input("Do you eat snow to quench your thirst?\n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

def walk_three():
    response = input("Do you keep walking? Yes or yes. \n").lower()
    while response not in affirm_resp:
        response = input("Do you keep walking? Yes or yes. \n").lower()
    if response in affirm_resp:
        return True

def last_walk():
    response = input("You regain freewill. Do you keep walking? Yes or no. \n").lower()
    while response not in affirm_resp and response not in neg_resp:
        response = input("You can choose this time. Truly. Yes or no. \n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

def road():
    response = input("You come around a small hill and see a break in the trees. As you approach, you think it may be a clearing. It's too long for that. You see something up ahead... it's a moose crossing sign. You- You did it! This will lead to someone. Something. Anything that can help you. But doubt starts to creep in. Do you follow the road, which may be your best chance of survival? \n").lower()
    while response not in affirm_resp and response not in neg_resp:
        response = input("You are overjoyed, it may not be much but it's something. Do you follow the road? \n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

#this just keeps walking and looping. if they type break, i want the entire code to end just like if they died. it'll be a little easter egg. I just need to make sure that the one 'break' is sufficient and test whether i need it where it'll actually loop.
#so the break in the else didn't work so i need to say if false then break in the bottom
secret_option = ['break']
def walk_indef():
    print(random.choice(walk_messages))
    response = input("Keep walking? Yes or yes? \n").lower()
    while response not in affirm_resp and response not in secret_option:
        response = input("You really don't have any other choice now. \n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

#don't accept food from strangers. maybe theyre living in the middle of alaska for a reason. 
def warm_meal():
    print("What's that? \nSmoke rising in the distance?\nEven if it's just a campfire... it could be your saving grace.\nYou run to it, stumbling through the thick snow\nYou can't believe your eyes...\nIt's a house.\n You stumble up to the door and pound on it.\nAn old lady opens the door. For a second you think it might be your oma, but she died when you were 12.\nShe ushers you in her cottage. Her husband wraps a blanket around you while she adds wood to the fire.\nWhat happened, they ask. Are you okay?\nYou can barely respond. It's just now you realize how much everything hurts.\n'I was in a plane crash', you explain. 'No one- no one else made it out'.\n 'Oh sweetie', she croons. She puts a mug of hot tea next to you. You don't know if you can pick it up without dropping it. Your fingers are still so numb.\n")
    print("You begin to warm up after what feels like hours sitting in front of the fire. The husband tends to the fire and tells you stories as the woman makes soup. As she brings the hot bowl over... something seems odd.")
    response = input("Do you accept the soup?\n").lower()
    while response not in affirm_resp and response not in neg_resp:
        response = input("The woman waits for your answer.\n").lower()
    if response in affirm_resp:
        return True
    else:
        return False

"""
while true 
    print walk message
    if 'secret word' then break
"""
#game

#leave plane is true and survival
#int
plane_ch = leave_plane()
if plane_ch:
    #upwind is true and survive
    #downwind is false and death
    wind_ch = up_down_wind()
    if wind_ch:
    #follow river is true and death
    #leave river is false and survive
    #need to leave river w false to survive
        river_ch = follow_river()
        if river_ch:
            print("While rivers may go to civilization, this river turned into a gorge and you realized too late. You were trapped and died.")
        else:
            fish_ch = catch_fish()
            if fish_ch:
                #hands and spear are both true, it doesn't matter. they both succeed
                hand_spear_ch = hands_spear()
                #raw is true
                #cooked is false and goes to fire
                raw_cook_ch = raw_cook()
                if raw_cook_ch:
                    #getting berries is true and death
                    berries_ch = berries() 
                    if berries_ch:
                        print("You didn't remember your training well enough. They were poisonous. You die.")
                    else:
                        #walk is true and continues
                        #sleep goes to snow igloo
                        sleep_ch = walk_sleep()
                        if sleep_ch:
                            #eat snow is true and death
                            #not eating snow is false and living
                            snow_ch = eat_snow()
                            if snow_ch:
                                print("u die")
                            else:
                                print("Good choice. If you had a way to melt it, it would be fine. Eating frozen snow is worse than nothing because it is too cold.")
                                for n in range(2):
                                    #yes is true and walking. do it three tiems
                                    walk_ch = walk_three()
                                #yes is walking and cont
                                #no is stop and die
                                fin_walk_ch = last_walk()
                                if fin_walk_ch:
                                    #follow road is true and cont to house
                                    #not following road is false and you go into the eternal loop of walking. 
                                    road_ch = road() 
                                    if road_ch:
                                        #accepting soup is true and death
                                        #rejecting soup is false and also death
                                        meal_ch = warm_meal()  
                                        if meal_ch: 
                                            print("don't accept food from strangers")
                                        else:
                                            print("that's rude ur axed to death in ur sleep")
                                    else:
                                        print("You start to doubt yourself as you walk away from the road. You shake it off. There's no room to doubt yourself out here. You need to survive. You keep walking.")
                                        #yes is walk and loops back
                                        #'break' breaks and should completely end code. 
                                        while True:
                                            walk_indef_ch = walk_indef()
                                else:
                                    print("You succumb to the darkness. They find your body in the spring when the snow melts.")     
                        else:
                            #igloo is true and death
                            #open is false and death
                            igloo_ch = igloo_open()
                            if igloo_ch:
                                print("Better to sleep under shelter than to sleep out in the open. Unfortunately, you're bad at making igloos. It collapses on you and kills you in your sleep.")
                            else:
                                print("Sleep out in the open? It's freezing. You fool. You rightfully die of exposure and hyporthermia.")                                   
                else:
                    #clothes is true and death
                    #wood is false and also death
                    fire_ch = fire()
                    if fire_ch:
                        print("You burned your clothes? Fool. You die of hypothermia that night.")
                    else: 
                        print("Better choice than burning your clothes. Unfortunately, the wood was wet and you die of hypothermia trying to get it to light.")
            else:
                #getting berries is true and death
                berries_ch = berries() 
                if berries_ch:
                    print("You didn't remember your training well enough. They were poisonous. You die.")
                else:
                    #walk is true and continues
                    #sleep goes to snow igloo
                    sleep_ch = walk_sleep()
                    if sleep_ch:
                        #eat snow is true and death
                        #not eating snow is false and living
                        snow_ch = eat_snow()
                        if snow_ch:
                            print("u die")
                        else:
                            print("Good choice. If you had a way to melt it, it would be fine. Eating frozen snow is worse than nothing because it is too cold.")
                            for n in range(2):
                                #yes is true and walking. do it three tiems
                                walk_ch = walk_three()
                            #yes is walking and cont
                            #no is stop and die
                            fin_walk_ch = last_walk()
                            if fin_walk_ch:
                                #follow road is true and cont to house
                                #not following road is false and you go into the eternal loop of walking. 
                                road_ch = road() 
                                if road_ch:
                                    #accepting soup is true and death
                                    #rejecting soup is false and also death
                                    meal_ch = warm_meal()  
                                    if meal_ch: 
                                        print("don't accept food from strangers")
                                    else:
                                        print("that's rude ur axed to death in ur sleep")
                                else:
                                    print("You start to doubt yourself as you walk away from the road. You shake it off. There's no room to doubt yourself out here. You need to survive. You keep walking.")
                                    #yes is walk and loops back
                                    #'break' breaks and should completely end code. 
                                    while True:
                                        walk_indef_ch = walk_indef()
                            else:
                                print("You succumb to the darkness. They find your body in the spring when the snow melts.")     
                    else:
                        #igloo is true and death
                        #open is false and death
                        igloo_ch = igloo_open()
                        if igloo_ch:
                            print("Better to sleep under shelter than to sleep out in the open. Unfortunately, you're bad at making igloos. It collapses on you and kills you in your sleep.")
                        else:
                            print("Sleep out in the open? It's freezing. You fool. You rightfully die of exposure and hyporthermia.")                                    
    else:
        print("Should've gone upwind. Remember that black smoke? It was toxic and killed you.")
else:
    print("You should have walked away. The plane exploded.")