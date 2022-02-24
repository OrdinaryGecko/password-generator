import string, random

while True:
    length = int(input("Enter length of password: "))
    if length <= 0:
        print("Length of password should atleast be 1. Try again.")
        continue
    else:
        break

lf = lambda user_input: 1 if user_input.lower() == "y" or user_input.lower() == "yes" else 0

while True:
    lower = lf(user_input = input("Do you want lowercase characters? (Y/N): "))

    upper = lf(user_input = input("Do you want uppercase characters? (Y/N): "))

    digits = lf(user_input = input("Do you want digits? (Y/N): "))

    punctuations = lf(user_input = input("Do you want punctuations? (Y/N): "))

    if lower == 0 and upper == 0 and digits == 0 and punctuations == 0:
        print("You must select atleast one criterion. Try again.")
        continue
    else:
        break

ingredients_value = {"0": string.ascii_lowercase, "1": string.ascii_uppercase, "2": string.digits, "3": string.punctuation}

ingredients_value_selected = [idx for idx,val in enumerate([lower,upper,digits,punctuations],0) if val == 1]

ingredients_selected = []

for i in ingredients_value_selected:
    for v in ingredients_value[str(i)]:
        ingredients_selected.append(v)

password = "".join(random.choices(ingredients_selected, k = length))

print(password)
