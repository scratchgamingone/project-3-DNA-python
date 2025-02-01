################################################################################
#
# Computer Project 03
#
#
#
#
#
#
#
#
#
#
#
################################################################################


banner = r"""
============================================
    PROJECT HELIX: DNA ALIGNMENT
============================================
    🧬 Optimizing DNA Storage & Transmission   
    🚀 Accelerating Bioinformatics Research  

    A--T   C--G   G--C   T--A   A--T   G--C
    |      |      |      |      |      |
    T--A   G--C   C--G   A--T   T--A   C--G
============================================
"""

menu = '''\nPlease choose one of the options below:
\tA. DNA Sequence Alignment
\tH. Display the menu of options.
\tX. Exit.'''

action = '''\n:~What do you want to do:
    a (add indel)
    d (delete indel)
    s (score)
    q (quit) ~:'''


dna_letters = "ATCGatcg".lower()

print(banner) #will print out the banner
print(menu) #will print out the menu

choose_option = input("\n:~Enter option ~:").lower()


if choose_option =="h" or choose_option =="a" or choose_option =="x":

    while choose_option == "h": #will display the menu of option
        print(menu)
        choose_option = input("\n:~Enter option ~:").lower()

    while choose_option =="a": #will add in the strings of letter
        string_1 = input("\n:~Input String 1 ~:").lower() # will ask the user to enter in string 1
        while string_1 == "": #will ask the user to enter again if the string is empty
            print("Invalid characters in the DNA sequence\n")
            string_1 = input("\n:~Input String 1 ~:").lower()  # will ask the user to enter in string 1

        while any(letter not in dna_letters for letter in string_1):
            print("Invalid characters in the DNA sequence\n")
            string_1 = input("\n:~Input String 1 ~:").lower()  # Prompt again if invalid characters are found

        string_2 = input(":~Input String 2 ~:")  # will ask the user to enter in string 2
        while string_2 == "": #will ask the user to enter again if the string is empty
            print("Invalid characters in the DNA sequence\n")
            string_2 = input("\n:~Input String 1 ~:").lower()  # will ask the user to enter in string 1

        while any(letter not in dna_letters for letter in string_2):
            print("Invalid characters in the DNA sequence\n")
            string_2 = input(":~Input String 2 ~:").lower()  # Prompt again if invalid characters are found

        subaction = input(action).lower() #will print out the action on what to do

        while subaction == "s":

            print(string_1)
            print(string_2)

        while subaction == "a": #will add a string
            pick_string = int(input("\n:~Work on which string (1 or 2) ~:")) #will ask the user to enter which string to add on

            while pick_string != 1 and pick_string != 2:
                print("Invalid options. Please try again.")  #wil ask the user to enter in again if it didn't match 1 or 2
                pick_string = int(input("\n:~Work on which string (1 or 2) ~:")) #wil ask the user to enter in again if it didn't match 1 or 2

            if pick_string == 1: #will add a string to string 1 if string 1 is chosen
                pick_index = int(input(":~Before what index ~:"))  # will ask the user to enter in indel

                while pick_index < 0 or pick_index >= len(string_1):  # check if index is out of range
                    print("Insert index out of range\n")
                    pick_index = int(input(":~Before what index ~:"))  # will ask again if the index is out of range
                #will add the "-" to the string where before that index

                break


"""
for example: 
:~Input String 1 ~:aaatttccc
:~Input String 2 ~:aatttcccc
:~What do you want to do:
 a (add indel)
 d (delete indel)
 s (score)
 q (quit) ~:s
Matches: 7 Mismatches: 2
String 1: aaAttTccc
String 2: aaTttCccc
:~What do you want to do:
 a (add indel)
 d (delete indel)
 s (score)
 q (quit) ~:a
:~Work on which string (1 or 2) ~:2
:~Before what index ~:2
:~What do you want to do:
 a (add indel)
 d (delete indel)
 s (score)
 q (quit) ~:s
Matches: 8 Mismatches: 2
String 1: aaAtttcccString 2: aa-tttcccC
                    """








print("Exiting program...") #will exist the program
print("Beware of computational biologist they screw genes and protein!")

