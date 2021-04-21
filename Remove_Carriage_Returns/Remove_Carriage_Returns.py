#Simple script to remove carriage returns from a text file

infile = "Raw_Text.txt"
outfile = "Processed_text.txt"

with open(infile, "r") as f:
    content = f.read()
    content = content.replace('\n', ' ') #remove carriage return

with open(outfile, 'w') as file:
    file.write(content)
