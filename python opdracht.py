# Doel: Vragen beatwoorden door de computer.

# intput()
# print()
#variabelen

print("Wat is jou naam?")
naam = input()
print(naam)

print( "Wat is je achternaam?")
anaam = input()
print(anaam)

print("Jou volledige naam is dus:")
print ( naam + anaam)

print("Waar woon je?")
Woonplaats = input()
print("Leuk dus je woont in") 
print(Woonplaats)

print("Werk je al")
answer = input("zeg ja of nee : ")
if answer == "ja":
    print("Leuk waar werk je dan?")
    werk = input()
    print("leuk, ik werk bij new york pizza")
    

elif answer == "nee":
    print("wil je ergens werken?")
    antwoord = input("zeg ja of nee : ")
    
    if antwoord == "ja":
        print("Waar wil je werken?")
        werK = input()
        print("leuk, ik werk bij new york pizza")
        
    elif antwoord == "nee":
        print("oke maakt niet uit")


    
