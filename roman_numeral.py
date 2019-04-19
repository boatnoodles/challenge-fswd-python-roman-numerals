user_num = input("Enter a number: ")

try:
    user_num = int(user_num)
except ValueError:
    print("I asked for a number, not gibberish!")

pairs = [
    {'M': 1000},
    {'CM': 900},
    {'D': 500},
    {'CD': 400},
    {'C': 100},
    {'XC': 90},
    {'L': 50},
    {'XL': 40},
    {'X': 10},
    {'IX': 9},
    {'VI': 6},
    {'V': 5},
    {'IV': 4},
    {'I': 1}]

counter = user_num
rom_num = ""

for pair in pairs:
    for key, value in pair.items():
        while counter // value > 0:
            counter -= value
            rom_num += key

print(f"Your number {user_num} in Roman days would have been {rom_num}")
