# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:19:34 2018

@author: 09719446
"""
from random import randint,shuffle
num_player=6
day=0

def assign_roles(player):
    role_dict={}
    roles=["farmer","farmer","prohet","werewolf","werewolf","witch"]
    shuffle(roles)
    for index in range(0,len(roles)):
        role_dict[index+1]=[roles[index],"alive"]
    print role_dict
    return role_dict

roles=assign_roles(num_player)
    
msg_lib={"night":"It's night time close your eyes","day":"it's day time open your eyes",\
        "eye_open":"Open your eyes","eye_close":"Close your eyes",\
        "forcast_question":"Choose a person to forcast","forcast_good":"The person is a good guy","forest_bad":"The person is a bad guy",\
        "antitode":"You have a bottle of antitode if you want to use","toxicant":"You have a bottle of toxicant if you want to use",\
        "wolf_kill":"Werewolfs choose a person to kill"}       

def get_response(msg,choices):
    try:
        response=raw_input(msg)
        if response in choices:
           return response 
        else:
           response=raw_input("Invalid message,last chance!"+msg) 
    except:
        response=raw_input("Invalid message,last chance!"+msg)
    if response in choices:
        return response
    else:
        print "Invalid input. Chance missed"
        return
    
def send_msg(msg,target):
    print target+":"+msg 
    
def get_mode(List):
    most=List.count(max(List,key=List.count))
    mode=list(set(filter(lambda x: List.count(x)==most,List)))
    if len(mode)==1:
        return mode
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
    result=get_mode(response)
    if not result ==-1 :
        roles[result][1]="dying"
    return 

def prohet_turn():
    target="prohet"
    send_msg(msg_lib["eye_open"],target)
    get_response(msg_lib["forcast_question"],roles.keys)
    
        