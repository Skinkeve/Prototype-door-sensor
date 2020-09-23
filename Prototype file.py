people = 0
maxpeople = 50
entering = False
exiting = False
redlight = False

def idle():
    if entering == True:
        people += 1
        if people = maxpeople or people > maxpeople:
            redlight = True
        else:
            redlight = False
        entering = False
    if exiting == True:
        if people > 0:
            people -= 1
        exiting = False
