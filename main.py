import sys
sys.path.append('./calculatrice')
from calculatrice import calcul
from calculatrice import addition
from calculatrice import subtraction
from calculatrice import multiplication
from calculatrice import division

print("Welcome in the calculator, the n3dh4ck3r!\n")
print("which are addition, multiplication, subtraction, division individually.\n"
      "And I also propose a normal calculation which mixes everything. \n")
print("If you want to do an addition type addition and the same for the others.\n"
      "And for a simple calculation type calculation.")

while True:
    choice = input("make your choice:")
    if choice.lower() == "addition":
        addition()
    elif choice.lower() == "subtraction":
        subtraction()
    elif choice.lower() == "multiplication":
        multiplication()
    elif choice.lower() == "division":
        division()
    elif choice.lower() == "calculation":
        calcul()
    else:
        print("Invalid choice.")
    answer = input("Do you want another operation? (Yes/No):")
    if answer.lower() == "no":
        print("Goodbye!")
        break




