import pandas as pd
#reads in file with data about elements
data = pd.read_pickle('aufbau.pkl')

#selects columns of elements name and atomic number
data = data[['Element Name', 'Atomic Number']]
data.set_index('Element Name', inplace=True)

element = input("Enter name of element: ")
try:
    element = data.loc[element]
    print('Element Found')
    electrons = int(element)
except:
    print('Element Not Found')
    exit()

#determines if user wants noble gas notation
possible_responses = ["y", "yes", "yup", "ye", "yeah"]
nb_notation = input("Do you want noble gas notation? ").lower() in possible_responses

#dictionary storing max number of electrons in each orbital
aufbau_dict = {"1s":2, "2s":2, "2p":6, "3s":2, "3p":6, "4s":2, "3d":10, "4p":6, "5s":2, "4d":10, "5p":6, "6s":2, "4f":14, "5d":10, "6p":6, "7s":2, "5f":14, "6d":10, "7p":6}
#replaces orbital with aternate notation if noble gas notation is desired
replacements = {"1s": "[He]", "2p": "[Ne]", "3p": "[Ar]", "4p": "[Kr]", "5p": "[Xe]", "6p":"[Rn]"}

#stores electron configuration as a string, whenever new orbitals are needed, the string gets appended
config = ""
for orbital in aufbau_dict:
    max_electrons = aufbau_dict[orbital]
    #if number of unfilled electrons is greater than max electrons in subshell
    if electrons >= max_electrons:
        #fill subshell by allocating max number of electrons
        config += orbital + str(max_electrons)
        #number of unfilled electrons decreases since we filled subshell with max electons
        electrons -= max_electrons
        #adds hyphen to string to look neater if we still have electrons remaining to fill
        if electrons > 0:
            config += "-"
        #efficient method to replace string with noble gas notation
        if nb_notation and electrons > 0:
            config = replacements[orbital]
    #if electrons is less than max for subshell, simply allocate the remaining electrons into subshell and append to string
    else:
        config += orbital + str(electrons)
        break
print(config)