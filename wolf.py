# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:19:34 2018

@author: 09719446
"""
from random import randint,shuffle,choice
import time
num_player=6
day=1
game_status=True
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

def get_response(msg,player,choices=[],time_out_sec=10):
    start_time=time.clock()
    response=raw_input(msg)
    if choices :
        while True:
            if time.clock()>start_time+time_out_sec :
               print "Timeout chance missed"
               return False
            else:
               if response.isdigit():
                  response=int(response)
                  if response in choices:
                      return response
                  else:
                      response=raw_input("Invalid input. "+ msg)
               else:
                  response=response.lower()
                  if response in choices:
                      return response
                  else:
                      response=raw_input("Invalid input. "+ msg)
    else: return 

        
    
def send_msg(msg,target):
    print target,
    print ": "+msg
    
def get_mode(List,single_output=True):
    most=List.count(max(List,key=List.count))
    mode=list(set(filter(lambda x: List.count(x)==most,List)))
    if single_output:
        if len(mode)==1 and not(List[0]==False and List[1]==False):
            return mode[0]
        elif False in mode and not(List[0]==False and List[1]==False):
            mode.remove(False)
            return mode[0]      
        else: 
            return False   #an indication of duplicated votes
    else:
        return mode
    
def player_next(player,order):
    if order=="l":
       increment=-1
    else:  
       increment=1
    if min(roles.keys())<=player+increment<=max(roles.keys()):
            next_player=roles.keys()[roles.keys().index(player)+increment]
    elif player+increment<min(roles.keys()):
            next_player=max(roles.keys())
    elif player+increment>max(roles.keys()):
            next_player=min(roles.keys())
    return next_player,increment    

def wolf_turn():
    response=[]
    target="werewolf"
    timeout=60
    send_msg(msg_lib["eye_open"],target)
    send_msg("Werewolf prepare to kill...",target)
    #time.sleep(10)
    for role in roles:
        if roles[role][0] ==target and roles[role][1] =="alive":
           response.append(get_response(msg_lib["wolf_kill"],role,roles.keys(),timeout))
    print response
    kill_num=get_mode(response)
    if kill_num !=False :
        roles[kill_num][1]="dying"
    send_msg(msg_lib["eye_close"],"werewolf")
    return kill_num

def prohet_turn():
    target=prohet
    timeout=30
    send_msg(msg_lib["eye_open"],target)
    response=get_response(msg_lib["forcast_question"],target,roles.keys(),timeout)
    if prohet in roles:
      if response in roles.keys() :
         if roles[response][0]=="werewolf":
            send_msg(msg_lib["forcast_bad"],"prohet")
         else: send_msg(msg_lib["forcast_good"],"prohet")
      else:
          send_msg("No Choice was made,your turn end.",target)
    else: time.sleep(randint(5,10))
    send_msg(msg_lib["eye_close"],"prohet")
    return    

def witch_turn(kill_num):
    target=witch
    timeout=30
    send_msg(msg_lib["eye_open"],target)
    if kill_num!=-1 and witch in roles and "antidote" in roles[witch]:
       send_msg("Last night number %d player was killed"%kill_num,target)
       response=get_response(msg_lib["antidote"],target,["y","n"],timeout)
       if response =="y" :
           roles[kill_num][1]="alive"
           roles[witch][2]="antidote_used"
    else: time.sleep(randint(5,10))  
    if witch in roles and "toxicant" in roles[witch]:
        response = get_response(msg_lib["toxicant"],target,["y","n"],timeout)
        if response  == "y":
            response = get_response("Select a player number to kill:",target,roles.keys(),timeout)
            if response !=False:
                roles[response][1]="dying"
                roles[witch][3]="toxicant_used"
                return response
            else: send_msg("No target was selected",target)
    else: time.sleep(randint(5,10))
    return 

def night_end():
    died=[]
    for key in roles:
           if roles[key][1]=="dying":
              roles[key]="died"
              died.append(key)
    send_msg("Day time open your eyes","All")
    if died and False not in died:
        send_msg("Player died are %s"%died,"All")
    else:
        died=[]
        send_msg("Peaceful night","ALL")
    return died


def pre_day_time(died_people):
    if day==1:
       for died in range(0,len(died_people)):
           get_response("Start your death sentence,number %s player: "%died_people[died],died_people[died]) 
    if len(died_people)==1:
       order=get_response("Choose left or right to start speak, type l or r: ",died_people[0],["l","r"])
       [start_speaker,order]=player_next(died_people[0],order)
    else:
       start_speaker=choice(roles.keys())
       order=choice([-1,1]) #-1 anticlockwise 1 clockwise
    for people in died_people:
        del roles[people]
    return start_speaker, order

def get_vote(voter,vote_target=roles.keys()):
    vote={}
    vote_list=[]
    for player in voter:
        vote[player]=(get_response("Start your vote player %d: "%player,player,vote_target))
        vote_list.append(vote[player])
    vote_dict={}
    for player in voter:
        vote_dict[player]=vote_list.count(player)    
    print vote
    print vote_dict
    vote_result=get_mode(vote_list,False)
    return vote_result

def check_game_status():
    player_list=[]
    for key in roles:
        player_list.append(roles[key][0])
    if "werewolf" not in player_list:
        send_msg("Good guy win!!","ALL")
        return False
    elif ("prohet" not in player_list and "witch" not in player_list ) or "farmer" not in player_list:
        send_msg("Bad guy win!!","All")
        return False
    elif player_list.count("werewolf")>=0.5*len(player_list):
        send_msg("Bad guy win!!","All")
        return False
    else: return True
    
def day_time(start_speaker,order):
    speak_order=roles.keys()
    if order==-1:
        speak_order.reverse()
    pop=speak_order[:speak_order.index(start_speaker)]
    speak_order[:speak_order.index(start_speaker)]=[]
    speak_order+=pop
    for player in  speak_order:       
        get_response("Start your speech player %d: "%player,player)
    vote_result=get_vote(speak_order)
    if len(vote_result)==1:
       del roles[vote_result[0]]
       send_msg("player %d has been voted out"%vote_result[0],"ALL")
       get_response("Start your death sentence, %s player: "%vote_result[0],vote_result[0])
    elif len(vote_result)>1:
        send_msg("Equal votes %s"%vote_result,"ALL")
        for player in vote_result:
            get_response("Start your speech player %d for not dying: "%player,player)
            speak_order.remove(player)
        vote_result=get_vote(speak_order,vote_result) 
        if len(vote_result)==1:
           del roles[vote_result[0]]
           send_msg("player %d has been voted out"%vote_result[0],"ALL")
           get_response("Start your death sentence, %s player: "%vote_result[0],vote_result[0])
    
while game_status:
    send_msg("Night has Fall Close all your eyes","ALL")
    killed=wolf_turn()
    prohet_turn()
    witch_turn(killed)
    died=night_end()
    [start_speaker,order]=pre_day_time(died)
    day_time(start_speaker,order)
    game_status=check_game_status()
    day+=1
    print "%d Day"%day
    