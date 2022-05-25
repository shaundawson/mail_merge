PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

#TODO: Create a letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    # TODO: For each name in invited_names.txt get letter contents
    for name in names:
        stripped_name = name.strip()
        # TODO: Replace the [name] placeholder with the actual name.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        # TODO: Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)






        









    



    




