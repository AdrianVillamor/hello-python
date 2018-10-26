import sys

Vla = sys.argv[1]

Vla = float(Vla)

if Vla >= 220.0:
    print("Super Typhoon") 
elif Vla >= 118.0:
    print("Typhoon")
elif Vla >= 89.0:
    print("Severe Tropical Storm")
elif Vla >= 62.0:
    print("Tropical Storm")
if Vla < 61:
    print("Tropical Depression")

