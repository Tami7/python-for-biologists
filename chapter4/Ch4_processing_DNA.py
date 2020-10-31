input_text = open("input.txt", "r")
output_text = open("output.txt", "w")

for line in input_text:
    sequence = line[14:].strip()
    output_text.write(f"{sequence}\n")
    print(len(sequence))
output_text.close()
