def start():

    fig = input("KIES EEN FIGUUR OM DE OPPERVLAKTE VAN TE BEREKENEN:\n" "1. Vierkant\n" "2. Rechthoek\n" 
    "3. Driehoek\n""4. Cirkel\n")
    
    print("\n")
        
    if fig == "1":
        print("VIERKANT")
        zijde = input("Geef de zijde van het vierkant\n")
        print("\n")
        zijde = float(zijde)
        opp = zijde * zijde
        opp = str(opp)
        print("OPPERVLAKTE IS"" " + opp)
        print("\n")
        start()
       
    if fig == "2":
        print("RECHTHOEK")
        lengte = input("Geef de lengte\n")
        print("\n")
        breedte = input("Geef de breedte\n")
        print("\n")
        lengte = float(lengte)
        breedte = float(breedte)
        opp = lengte * breedte
        opp = str(opp)
        print("OPPERVLAKTE IS" " " + opp)
        print("\n")
        start()
       
    if fig == "3":
        print("DRIEHOEK")
        lengte = input("Geef de lengte\n")
        basis = input("Geef de basis\n")
        lengte = float(lengte)
        basis = float(basis)
        opp = (lengte * basis)/2
        opp = str(opp)
        print("OPPERVLAKTE IS" " " + opp)
        print("\n")
        start()
        
    if fig == "4":
        print("CIRKEL")
        import math
        straal = input("Geef de straal\n")
        straal = float(straal)
        opp = straal * straal * math.pi
        opp = str(opp)
        print("OPPERVLAKTE IS" " " + opp)
        print("\n")
        start()
start()
    
