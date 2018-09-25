"""
A nutritionist who works for a fitness club helps members by evaluating their diets. As part
of her evaluation, she asks members for the number of fat grams, carbohydrate grams, and protein
grams that they consumed in a day. Then, she calculates the number of calories that result from
the fat, using the following formula:

calories from fat = fat grams X 9

Next, she calculates the number of calories that result from the carbohydrates, using the following formula:

calories from carbs = carb grams X 4

Next, she calculates the number of calories that result from the proteins, using the following formula:

calories from protein = protein grams X 4
"""


def main():
    # fat_calc, carb_calc, prot_calc used as next function
    fat_total = fat_calc()
    print("You ate " + str(fat_total) + " calories from fat today.")
    carb_total = carb_calc()
    print("You ate " + str(carb_total) + " calories from fat today.")
    protein_total = prot_calc()
    print("You ate " + str(protein_total) + " calories from fat today.")
    total = str(format(fat_total + carb_total + protein_total, ","))  # formatting for comma use
    print("You ate a total of " + total + " calories today.")


def fat_calc():
    fat_grams = int(input("How many grams of fat did you eat today?: "))
    return fat_grams * 9  # calculation for fat into calories


def carb_calc():
    carb_grams = int(input("How many grams of carbs did you eat today?: "))
    return carb_grams * 4  # calculation for carbs into calories


def prot_calc():
    prot_grams = int(input("How many grams of protein did you eat today?: "))
    return prot_grams * 4  # calculation for protein into calories


main()
