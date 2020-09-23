people = 0 #hvor mange mennesker der aktuelt er i rummet
maxpeople = 50 #max antallet af mennesker der må være i rummet
entering = False #bool der er sand hvis der er en på vej ind af døren
exiting = False #bool der er sand hvis der er en der er på vej ud af døren
redlight = False #bool der er sand hvis lyset skal lyse rødt

def idle(): #definitionen
    if entering == True: #hvis der er en der går ind
        people += 1 #gør variablen en større
        if people = maxpeople or people > maxpeople: #hvis der er så mange inde som der må være eller flere
            redlight = True #lys rød
        else:#ellers
            redlight = False#lys grøn
        entering = False #gør entering false
    if exiting == True: # hvis der er en der er på vej ud
        if people > 0: # hvis der er mennesker inde i butikken
            people -= 1 # gør antallet en mindre
        exiting = False # gør exiting false

#eventuelt kan man lave en ny funktion der resetter antallet af mennesker ved midnat
# eller ved et tryk på en knap
