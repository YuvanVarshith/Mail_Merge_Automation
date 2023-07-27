def automation_invitation():
    with open("/mail-merge-project-start/Input/Names/invited_names.txt", mode="r") as names:
        name_list = names.readlines()
        perfect_name = [elements.strip() for elements in name_list]
    
    
    with open("/mail-merge-project-start/Input/Letters/starting_letter.txt", mode="r") as mail:
        mail_list = mail.read()
        for lp in perfect_name:
            replace = mail_list.replace("[name]", lp)
            with open(f"/mail-merge-project-start/Output/ReadyToSend/letter_for_{lp}.txt", mode="w") as invitation:
                invitation.write(replace)

automation_invitation()
