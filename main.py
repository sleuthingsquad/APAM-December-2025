#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", "r") as name_list:
    names = name_list.readlines()
#Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as base_letter:
    letter = base_letter.read()
    for name in names:
        stripped_name = name.strip()
        individual_letter = letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/Letter_For_{stripped_name}.txt", mode='w') as invite_letter:
            invite_letter.write(individual_letter)
