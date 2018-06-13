# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:19:34 2018

@author: 09719446
"""
from random import randint,shuffle
from time import sleep
num_player=6
day=1
def assign_roles(player):
    role_dict={}
    roles=["farmer","farmer","prohet","werewolf","werewolf","witch"]
    shuffle(roles)
    global prohet
    prohet=roles.index("prohet")+1
    global witch
    witch=roles.index("witch")+1
    for index in range(0,len(roles)):
        if roles[index]=="witch":
           role_dict[index+1]=[roles[index],"alive","antidote","toxicant"]
        else: role_dict[index+1]=[roles[index],"alive"]
    print role_dict
    return role_dict

roles=assign_roles(num_player)
    
msg_lib={"night":"It's night time close your eyes","day":"it's day time open your eyes",\
        "eye_open":"Open your eyes","eye_close":"Close your eyes",\
        "forcast_question":"Choose a person to forcast: ","forcast_good":"The person is a good guy","forcast_bad":"The person is a bad guy",\
        "antidote":"You have a bottle of antitode if you want to use,response y/n: ","toxicant":"You have a bottle of toxicant if you want to use,response y/n: ",\
        "wolf_kill":"Werewolfs choose a person to kill: "}       

def get_response(msg,choices):
    response=raw_input(msg)
    turn=0
    while True:
        if turn<=1:
          if response.isdigit():
             if int(response) in choices:
                 return int(response)
               
             else:
               response=raw_input("Invalid input Last Chance,"+msg)
          else:
             if response in choices:
                 return response
               
             else:
               response=raw_input("Invalid input Last Chance,"+msg)
        else:
           print "Invalid input. Chance missed"
           return False
        turn+=1
    
def send_msg(msg,target):
    print target+":"+msg 
    
def get_mode(List):
    most=List.count(max(List,key=List.count))
    mode=list(set(filter(lambda x: List.count(x)==most,List)))
    if len(mode)==1 and not(List[0]==False and List[1]==False):
        return mode[0]
    elif False in mode and not(List[0]==False and List[1]==False):
         mode.remove(False)
         return mode[0]      
    else: 
        return -1   #an indication of duplicated votes
    
def wolf_turn():
    response=[]
    target="werewolf"
    send_msg(msg_lib["eye_open"],target)
    send_msg(msg_lib["wolf_kill"],target)
    for role in roles:
        if roles[role][0] ==target and roles[role][1] =="alive":
           response.append(get_response(msg_lib["wolf_kill"],roles.keys()))
    print response
    kill_num=get_mode(response)
    if not kill_num ==-1 :
        roles[kill_num][1]="dying"
    send_msg(msg_lib["eye_close"],"werewolf")
    return kill_num

def prohet_turn():
    target="prohet"
    send_msg(msg_lib["eye_open"],target)
    response=get_response(msg_lib["forcast_question"],roles.keys())
    if prohet in roles:
      if response in roles.keys() :
         if roles[response][0]=="werewolf":
            send_msg(msg_lib["forcast_bad"],"prohet")
         else: send_msg(msg_lib["forcast_good"],"prohet")
      else:
          send_msg("No Choice was made,your turn end.",target)
    else: sleep(randint(1,5))
    send_msg(msg_lib["eye_close"],"prohet")
    return    

def witch_turn(kill_num):
    target="witch"
    send_msg(msg_lib["eye_open"],target)
    if kill_num!=-1 and witch in roles and "antidote" in roles[witch]:
       send_msg("Last night number %d player was killed"%kill_num,target)
       response=get_response(msg_lib["antidote"],["y","n"])
       if response =="y" :
           roles[kill_num][1]="alive"
           roles[witch][2]="antidote_used"
    else: sleep(randint(1,5))  
    if witch in roles and "toxicant" in roles[witch]:
        response = get_response(msg_lib["toxicant"],["y","n"])
        if response  == "y":
            response = get_response("Select a player number to kill:",roles.keys())
            if response !=False:
                roles[response][1]="dying"
                roles[witch][3]="toxicant_used"
                return response
            else: send_msg("No target was put",target)
        else: sleep(randint(1,5))   
    else: sleep(randint(1,5))
    return 

#def night_end()