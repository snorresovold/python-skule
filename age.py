age = input("Hvor mange år er du? ")
remaining_age = 90 - int(age)
print("Du har \n",
    remaining_age * 365, "dager igen å leve \n",
    remaining_age * 52, "uker igjen å leve \n",
    remaining_age * 12, "måneder igen å leve ", "dersom du blir 90 år gammel"
)