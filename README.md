# Who's wolfery game
num_player   #first input to decide number of identities verion 1.0 set as 6 people
day number   #turns of the game
status of player: alive dying died    #dying means player was killed on the night

6 people game : identities are 2 farmers 1 prohet 1 witch 2 werewolf
Logic rundown
inital
assign indentities to 6 people as random
display indenties to them on mobile #posible adding comment on distribution of indentities
Yell night is coming !

Werewolf part
Call werewolf to open eyes! #possible time out peroid 120s?
Check alive and send mess to alive
Call werewolf to select a kill,or input on phone with agreement, whenever larger number of votes will be the killing target
set voted player status to dying
if equal vote, none will be killed.
Call werewolf to close eyes.

Prohet part
check status not died
Call prohet to open eye.
Call prohet to select a target to forcast with input on phone #possible time out 2min
Return feedback on wehther the target is good or bad depending on the true indenty display it on phone
Call prohet to close eye.

Witch part
check status not died
Call witch to open eye
Yell you got an antidote if you want to use  # timeout peorid ?
if antidote avaliable, send msg who's dead and request action taken yes or no
   if yes change staus of player to alive   if not pass
if antidote not ava: possible sleep(10s) and then pass
if toxicant avaliable, send msg want to kill or not ? request answer yes or no
   if yes request input of player number and change player to status of dying 
   if no pass
if toxicant not avaliable: sleep(10s) and then pass

End of the night , day+1
all status of dying change to died
check alive and died status, if werewolf =0 endgame if farmer=0 endgame if prohet=dead and witch =dead endgame otherwise continue
futher caculation may be required here: if bad >=good endgame

option method: display mess to player who's died or yell things out

if day one . set starter of speaker to died person
fianlly died person set speaker set left ot right (number -1 or +1)
if no died random start
Yell it's day time open your eyes!
speaker start get meg and response when finsihed 
next speaker get meg if not died ...
all speaker ends request everyone to vote
when everyone entered display results to everyone 
if equal votes 
Yell equal votes ,random request highest votes to start speak then pass to next
request vote again on those two numbers
display results if equal then pass else set target died
if not equal vote, set higest votes died
start conv for voted died player, rquest end conv when end the continue
game status check again #possible a function for this 

night again until end 

