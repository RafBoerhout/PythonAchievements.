print("Je alarm gaat af, sta je op of slaap je door?")
print("Kies uit opstaan of slapen.")

keuze = input()

if keuze == 'opstaan':
    print("je bent opgestaan en je bent moe.")
    print("Je gaat ontbijten want je moet zo naar school.")
    print("Wat ga je eten?")
    print("Eet je een boterham of yogurt?")
    ontbijt = input()
    
    if ontbijt == 'boterham':
        print("je eet je boterham.")
        
    elif ontbijt == 'yogurt':
        print("je eet je yogurt.")
        
    print("je moet gaan fietsen naar het station, maar het regen, pak je de bus of fiets je naar het station.")

    vervoer = input()
    
    if vervoer == 'fiets':
        print("je fietst door de regen en je komt optijd op het station.")
        print("je stapt de trein is en komt op tijd opschool.")

    elif vervoer == 'bus':
        print("je staat bij de bus halte en je moet 15 min wachten op de bus.")
        print("je komt op het station en mist de trein omdat je op de bus moest wachten.")
        print("je neemt de eerst volgende trein naar school maar je komt te laat.")
    
elif keuze == 'slapen':
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzz")        
    print("je wekker gaat weer en je word wakker.")
    print("je ziet dat je je heb verslapen en dat je te laat komt op school.")
    print("ga je ontbijten of ga je gelijk naar school?")

    keuze1 = input()

    if keuze1 == 'ontbijten':
    print("Je gaat ontbijten want je bent toch al te laat voor school.")
    print("Wat ga je eten?")
    print("Eet je een boterham of yogurt?")
    ontbijt = input()
    
    if ontbijt == 'boterham':
        print("je eet je boterham.")
        
    elif ontbijt == 'yogurt':
        print("je eet je yogurt.")

    print("je bent klaar met eten en je gaat naar school.")
    print("je moet gaan fietsen naar het station, maar het regen, pak je de bus of fiets je naar het station.")
    
    vervoer1 = input()
    
    if vervoer1 == 'fiets':
        print("je fietst door de regen en je komt op het station.")
        print("je stapt de trein is en je baalt want je bent te laat.")

    elif vervoer1 == 'bus':
        print("je staat bij de bus halte en je moet 15 min wachten op de bus.")
        print("je komt op het station en mist de trein omdat je op de bus moest wachten.")
        print("je neemt de eerst volgende trein naar school. het boeit je niet meer of je nog later op school komt want je bent toch al te laat.")
    
elif keuze1 == 'naar school':
    print("je moet gaan fietsen naar het station, maar het regen, pak je de bus of fiets je naar het station.")
    
    vervoer1 = input()
    
    if vervoer1 == 'fiets':
        print("je fietst door de regen en je komt op het station.")
        print("je stapt de trein is en je baalt want je bent te laat.")

    elif vervoer1 == 'bus':
        print("je staat bij de bus halte en je moet 15 min wachten op de bus.")
        print("je komt op het station en mist de trein omdat je op de bus moest wachten.")
        print("je neemt de eerst volgende trein naar school. het boeit je niet meer of je nog later op school komt want je bent toch al te laat.")      
