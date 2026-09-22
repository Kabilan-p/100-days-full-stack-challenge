# file = open("employee.txt", "w")

# file.write("Kabil - Developer")

# file.close()

# file = open("employee.txt", "a")

# file.write("\nArun - Tester")

# file.close()



# file=open("employee.txt","a")

# file.write("\nRAM-TESTER")
# file.close()


# #########Writelines########
# employees = ["Arun\n", "Vijay\n", "Priya\n"]

# with open("employee.txt", "w") as file:
#     file.writelines(employees)

#########SEEK()###########
# with open("employee.txt", "r") as file:
#     print(file.read())   # 1st time

#     file.seek(0)         # cursor goes back to beginning

#     print(file.read())   # 2nd time


#     file.read()     # cursor goes to the end
# file.seek(0)    # cursor comes back to position 0
# position = file.tell()  # returns 0




# w vs x
# w → File இல்லனா create; இருந்தா content overwrite ஆகலாம்
# x → File இல்லனா create; ஏற்கனவே இருந்தா open செய்யாது

# r → Read
# w → Write / overwrite
# a → Append
# x → Create only if file doesn't exist




    # Next — File Mode b (Binary)

    # இதுவரை நாம .txt மாதிரி text files பார்த்தோம்.

    # ஆனா image, PDF போன்ற files text கிடையாது; அவை binary data.

    # அதற்காக b mode use பண்ணலாம்:

    # "rb" → Read binary
    # "wb" → Write binary



#     r  → Read
# w  → Write / overwrite
# a  → Append
# x  → Create new file only

# t  → Text mode
# b  → Binary mode

# rb → Read binary
# wb → Write binary

    # Example:

    # with open("photo.jpg", "rb") as file:
    #     data = file.read()





# Next — + File Modes

# இதுவரை r, w, a தனித்தனியா பார்த்தோம். Python-ல + add பண்ணினா read + write இரண்டுமே செய்ய முடியும்.

# r+ → Read + Write
# w+ → Write + Read
# a+ → Append + Read

# முக்கிய difference மட்டும் first புரிஞ்சுக்கோ:

# r+ → file already இருக்கணும்
# w+ → file இல்லனா create ஆகும்; இருந்தா old content erase ஆகலாம்
# a+ → file இல்லனா create ஆகும்; write பண்ணுற data end-ல add ஆகும்

# Example:

# with open("employee.txt", "r+") as file:
#     data = file.read()
#     print(data)

#     file.write("\nArun - Tester")


# Next — encoding

# Text file open பண்ணும்போது sometimes:

# with open("employee.txt", "r", encoding="utf-8") as file:
#     data = file.read()
#     print(data)

# encoding="utf-8" use பண்ணினா English மட்டும் இல்லாமல் Tamil போன்ற Unicode text-ஐயும் properly handle பண்ண உதவும்



# open() ✅ → close() ✅ → with open() ✅ → r / w / a / x ✅ → read() ✅ → readline() ✅ → readlines() ✅ → write() ✅ → writelines() ✅ → seek() ✅ → tell() ✅ → b / t ✅ → r+ / w+ / a+ ✅ → encoding ✅


employees = ["Arun-Tester\n", "Vijay-Designer\n"]
with open("employee.txt","w") as file:
    data=file.write("Kabil- Developer")   
    data=file.writelines(employees) 
