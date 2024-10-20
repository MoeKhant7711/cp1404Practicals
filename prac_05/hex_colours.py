"""
CP1404/CP5632 Practical  
Hexadecimal colour lookup  
"""

COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "BlueViolet": "#8a2be2"
}

print("Hexadecimal Colour Lookup")
colour_name = input("Enter colour name: ").strip().title() 
while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").strip().title()

print("Goodbye!")
