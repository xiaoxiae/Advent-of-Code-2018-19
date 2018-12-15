input = open("14.in", "r")
recipes = input.read().splitlines()[0]

# chocolates and elfs
chocolates = "37"
elf1 = 0
elf2 = 1

while recipes not in chocolates[-len(recipes):]:
    chocolates += str(int(chocolates[elf1]) + int(chocolates[elf2]))
    elf1 = (elf1 + int(chocolates[elf1]) + 1) % len(chocolates)
    elf2 = (elf2 + int(chocolates[elf2]) + 1) % len(chocolates)

print(chocolates.index(recipes))
