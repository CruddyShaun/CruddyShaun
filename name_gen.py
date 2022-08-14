#NAME GENERATOR

import random, time

first_name = ('Shaun','Hulk','Tony', 'Wendy', 'Noah', 'Liam', 'Fay', 'Leander', 'André', 'Nicole', 'Gavin', 'Jason', 'Grace', 'Fleur', 'Anaïs')

last_name = ('Dendikke', 'Degroote', 'Dedunne', 'Dedomme', 'Deschone', 'Desimpele', 'Dezage', 'Depoeper', 'Demaagd', 'Dezeure', 'Pannekoeke', 'Devis', 'Hawk','Hogan', 'Green', 'Morel')

print("Welcome to random name generator\n")

while True:
    first = random.choice(first_name)
    
    last = random.choice(last_name)
    
    print("\n\n")
    time.sleep(1)    
    print("\t{} {}".format(first, last))
    print("\n\n")
    
    try_again = input("\nTry again? (Press Enter or n to quit)")
    if try_again.lower() == "n":
        break
        
input("Press Enter to exit.") 


