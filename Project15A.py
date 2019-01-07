
# coding: utf-8

# # This program that I have chosen for this assignment is "Mad-Libs"

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[6]:

#These do not change, and they only are here to allow the while loop and if statement to work correctly. 
choice = 0
x = True



#The function where all of the stories and variables which will be placed in the stories are stored.
def MadLibs(): 
    
    #A statement which shows the user that they are playing "Mad-Libs"
    print "Mad-Libs!"
    
    #The choice of which story the person will be filling out. Only three stories can currently be picked. 
    choice = int(input('Pick a number between 1 through 3 for a different story!'))
    
    #The reason why the function is mainly inside a while loop is so it can be chosen again if the person did not
    #choose a valid number. 
    while x == True:
        if choice == 1:
            
            #The inputs of all words in the story.
            adj1 = raw_input('Pick an adjective!')
            adj2 = raw_input('Pick another adjective!')
            animal1 = raw_input('Pick an animal!')
            room1 = raw_input('Pick a room in a house!')
            verbpst1 = raw_input('Pick a verb that is past tense!')
            verb1 = raw_input('Pick a verb!')
            name1 = raw_input("Pick a relative's name!")
            noun1 = raw_input('Pick a noun!')
            liquid1 = raw_input('Pick a liquid!')
            verbing1 = raw_input('Pick a verb ending in "-ing"!')
            body1 = raw_input('Pick a body part! (Plural)')
            nounplu1 = raw_input('Pick a plural noun!')
            verbing2 = raw_input('Pick another verb ending in "-ing"!')
            noun2 = raw_input('Pick another noun')
            
            #The story is then called after all words have been chosen. Then, the words would be worked into the story.
            print "It was a "+str(adj1)+", cold November day. I woke up to the "+str(adj2)+" smell of "+str(animal1)+" roasting in the "+str(room1)+" downstairs. I "+str(verbpst1)+" down the stairs to see if I could help "+str(verb1)+" for dinner. My mom said, "+'"See if '+ str(name1)+'needs a fresh '+str(noun1)+'."'+' So I carried a tray of glasses full of '+str(liquid1)+' into the '+str(verbing1)+" room. When I got there, I couldn't believe my "+str(body1)+"! There were "+str(nounplu1)+" "+str(verbing2)+ " on the "+str(noun2)
            #This stops the while loop since a valid number was given. 
            break;
        
        elif choice == 2:
            
            #The inputs of all words in the story.
            adj1 = raw_input('Pick an adjective!')
            place1 = raw_input('Pick a place!')
            adj2 = raw_input('Pick another adjective!')
            adj3 = raw_input('Pick another adjective!')
            nounplu1 = raw_input('Pick a plural noun!')
            nounplu2 = raw_input('Pick aother plural noun!')
            noun1 = raw_input('Pick a noun!')
            verb1 = raw_input('Pick a verb!')
            noun2 = raw_input('Pick another noun!')
            verb2 = raw_input('Pick another verb!')
            verbact1 = raw_input('Pick an action verb!')
            nounplu3 = raw_input('Pick another plural noun!')
            noun3 = raw_input('Pick another noun!')
            verbing1 = raw_input('Pick a verb ending in "-ing"!')
            noun4 = raw_input('Pick another noun!')
            time1 = raw_input('Pick a measurement of time!')
            adj4 = raw_input('Pick another adjective!')
            verbact2 = raw_input('Pick another action verb!')
            verb3 = raw_input('Pick another verb!')
            adj5 = raw_input('Pick another adjective!')
            nounposs1 = raw_input('Pick a possessive noun!')
            
            #The story is then called after all words have been chosen. Then, the words would be worked into the story.
            print "On the "+str(adj1)+" trip to "+str(place1)+", my "+str(adj2)+" friend and I decided to invent a game, Since this would be a rather "+str(adj3)+" trip, it would be need to be a game with "+str(nounplu1)+" and "+str(nounplu2)+". Using our "+str(noun1)+" to "+str(verb1)+", we tried to get the "+str(noun2)+" next to us to play too, but they just "+str(verb2)+"-ed at us and "+str(verbact1)+" away. After a few rounds, we thought the game could use some "+str(nounplu3)+" so we turned on the "+str(noun3)+" and started "+str(verbing1)+" to the "+str(noun4)+" before I got "+str(adj4)+" and decided to "+str(verbact2)+". I'll never "+str(verb3)+" that trip, it was the most "+str(adj5)+" road trip of my "+str(nounposs1)+"."
            #This stops the while loop since a valid number was given. 
            break;
            
        elif choice == 3:
            
            #The inputs of all words in the story.
            person1 = raw_input('Pick a name of a relative!')
            adj1 = raw_input('Pick an adjective!')
            adj2 = raw_input('Pick another adjective!')
            noun1 = raw_input('Pick a noun!')
            adj3 = raw_input('Pick another adjective!')
            noun2 = raw_input('Pick another noun!')
            adj4 = raw_input('Pick another adjective!')
            adj5 = raw_input('Pick another adjective!')
            verb1 = raw_input('Pick a verb!')
            verb2 = raw_input('Pick another verb!')
            person2 = raw_input('Pick another name of a relative!')
            verb3 = raw_input('Pick another verb!')
            adj6 = raw_input('Pick another adjective!')
            verb4 = raw_input('Pick another verb!')
            
            #The story is then called after all words have been chosen. Then, the words would be worked into the story.
            print "Yesterday, "+str(person1)+" and I went to the park. On our way to the "+str(adj1)+" park, we saw a "+str(adj2)+" "+str(noun1)+" on a bike. We also saw big "+str(adj3)+" balloons tied to a "+str(noun2)+". Once we got to the "+str(adj4)+" park, the sky turned "+str(adj5)+". It started to "+str(verb1)+" and "+str(verb2)+". "+str(person2)+" and I "+str(verb3)+" all the way home. Tomorrow we will try to go to the "+str(adj6)+" park again and hope it doesn't "+str(verb4)
            #This stops the while loop since a valid number was given. 
            break;
            
        else:
            #If the number chosen did not work, it would re-state the question and allow the user to choose again.
            print "Sorry! That was not a number to choose! Please type another number."
            choice = int(input('Pick a number between 1 through 3 for a different story!'))
    

MadLibs()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



