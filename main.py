#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/mail-merge-project-start/Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.readlines()
    perfect_name = [elements.strip() for elements in name_list]


with open("/mail-merge-project-start/Input/Letters/starting_letter.txt", mode="r") as mail:
    mail_list = mail.read()
    for lp in perfect_name:
        replace = mail_list.replace("[name]", lp)
        with open(f"/mail-merge-project-start/Output/ReadyToSend/letter_for_{lp}.txt", mode="w") as invitation:
            invitation.write(replace)

