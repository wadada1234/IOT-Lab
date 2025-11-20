#(d) Read a file line by line and print the word count of each line.
 
# ...existing code...
L = ["Geeks\n", "for\n", "Geeks\n"]

# write to file
with open('myfile.txt', 'w') as file1:
    file1.writelines(L)

# read file line by line and print the word count of each line
with open('myfile.txt', 'r') as file1:
    for idx, line in enumerate(file1, start=1):
        word_count = len(line.split())
        print(f"Line {idx}: {word_count} word(s) -- {line.strip()}")
# ...existing code...