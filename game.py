import time
import random


def game():

     print ("Welcome to the Game!")
     print ("*********************")

     time.sleep(2)

     name=str(input("Enter your name:"))


     print ("Wait\t",name,"\tYou have entered the Monster's Cave")
     time.sleep(2)
     print ("\n Watch out while you move, Take something with you for your protection\n")

     ch1=str(input("There is a sword, Do you want to take it? :[y/n]"))

     if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print("Whoa! Now you have a sword")
        time.sleep(2)
        sword = 1


     else:
          print("You have chosen not to take the sword")
          sword = 0

     print ("As you proceed further into the cave, you hear growling sound..")
     time.sleep(3)
     print("\n The growling repeats...\n")
     print("\t\t Grrhhhh..!!!\t\t")
     ch2 = str(input("Do you want to approach the mysterious sound? [y/n]"))


     if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print ("Be careful when you move closer")
        time.sleep(2)
        print ("OMG!, It's the giant MONSTER!")
        time.sleep(1)
        print ("He has spotted you!, Get ready to fight! Show him what you have got")
        ch3 = str(input("Do you want to fight it? [Y/N]"))


        if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:


           if sword == 1:
              print ("You have a sword to fight with!")
              print ("Use your skills to fight and kill the Monster")
              time.sleep(2)
              print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
              print ("               Wooshhh!!!                   ")
              print ("   YOU MUST HIT ABOVE A 5 TO KILL THE MONSTER    ")
              print ("IF THE MONSTER HITS HIGHER THAN YOU, YOU WILL DIE")
              print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
              time.sleep(2)
              fdmg1 = int(random.randint(4, 9))
              edmg1 = int(random.randint(1, 6))
              print ("your point is", fdmg1)
              print ("the monster hits a", edmg1)
              time.sleep(2)

              if edmg1 > fdmg1:
                 print ("The monster is about to kill you!")
                 complete = 0
     return complete
              elif fdmg1 < 5:
                   print ("You have weakened the monster, RUN AWAY and escape now")
                   complete = 1
     return complete

              else:
                   print ("Hurrayyy!!! You killed the monster!")
                   complete = 1
     return complete


           else:
                print("You don't have anything to fight with!")
                time.sleep(2)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("                  Fighting...                   ")
                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE MONSTER   ")
                print ("IF THE MONSTER HITS HIGHER THAN YOU, YOU WILL DIE")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                fdmg1 = int(random.randint(2, 7))
                edmg1 = int(random.randint(3, 5))
                print ("you scored a", fdmg1)
                print ("the monster scored a", edmg1)
                time.sleep(2)

                if edmg1 > fdmg1:
                   print ("The monster has wounded you!!!")
                   complete = 0
     return complete

                elif fdmg1 < 5:
                     print ("You didn't do enough damage to kill the monster, but you can run and escape now")
                     complete = 1
     return complete

                else:
                     print ("You killed the monster!")
                     complete = 1
                     return complete


        print ("You choose not to fight the monster.")
        time.sleep(1)
        print ("Bad Luck , The monster had caught you!!")
        complete = 0
     return complete

     else:
          print ("You turn away from the sound, and attempt to leave the cave...")
          time.sleep(1)
          print ("But something won't let you go....Bwuahhahaa!")
          time.sleep(2)
          complete = 0
     return complete

# game loop
alive = True
while alive:

      complete = game()
      if complete == 1:
         alive = input('You managed to escape the cave alive! Would you like to play again? [y/n]: ')
         if alive in ['y', 'Y', 'YES', 'yes', 'Yes',]:
         alive

         else:
              break

     else:
          alive = input('You have died! Would you like to play again? [y/n]: ')
          if alive in ['y', 'Y', 'YES', 'yes', 'Yes',]:
          alive

          else:
               break
