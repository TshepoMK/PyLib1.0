import time


name = raw_input("What is your name? ")
print "Hello, " + name, "Time to play hangman!"
print "\n"

time.sleep(1)
print "Start guessing, use CAPITAL LETTERS..."
time.sleep(0.5)

for i in word:
        word = "SECRET"
        guesses = ''
        turns = 10

while turns > 0:         

        failed = 0          

      
        for char in word:   

   
            if char in guesses:  
    
       
                print char,   

            else:   
        
                print "_",  
       
       
            failed += 1 

   
        if failed == 0:        
            print "\nYou won" 
    
            break             

        print   
        guess = raw_input("Guess a Character: ")     
        guesses += guess                    

   
        if guess not in word:  
    
            turns -= 1        
 
            print "Wrong\n"    
 
            print "You have", + turns, 'more guesses' 
 
        if turns == 0:           
    
                   print "You Loose\n" 
