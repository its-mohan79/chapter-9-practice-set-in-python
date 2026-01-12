#  a fantastic file problem
with open("fantastic_file.txt", "w") as file:
    file.write("Roses are red,\nViolets are blue,\nPython is great,\nAnd so are you.")
with open("fantastic_file.txt", "r") as file:
    content = file.read()
    print("Content of fantastic_file.txt:")
    print(content)
# Check for the presence of the word "fantastic" in the file
with open("fantastic_file.txt", "r") as file:

    content = file.read()
    if "fantastic" in content:
        print("The word 'fantastic' is present in the content.")
    else:
        print("The word 'fantastic' is not present in the content.")
    if "fantastic" in content:
        print("fantastic is present in the content")