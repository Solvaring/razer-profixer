import os

naga_profs = os.listdir()

naga_profs.remove('prof_name_check.py')

count = 0
for profile in naga_profs:
    current = open(profile)
    data = current.read()
    current.close()
    if "<ProfileName>" in data:
        print("<ProfileName> Tag IN: ", profile)
    elif "<ProfileName>" not in data:
        answer = input("Deleting Razer Profile: {} due to missing tag Y/N?".format(profile))
        if answer.upper() == 'Y':
            os.remove(profile)
            count += 1
print("Razer Profile Checker deleted {} profiles lacking the <ProfileName> tag. Press any key to exit".format(count))
input("")
