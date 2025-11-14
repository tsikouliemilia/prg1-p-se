run = True

bag = []

while run:

    print("vissa innehållet[v]")
    print ("spara i påsen [S]")
    print("Avsluta programet[Q]")
    
    choice = input ("välj:")
    if choice.lower () == "v":
        for thing in bag:
            print(thing)
            print(f"öppnar påsen* {bag}")
    elif choice.lower() == "s":
           bag.append(input ("skriv vad du vill spara:"))
    elif choice.lower() == "q":
            run = False
    elif choice.lower () == "f":
        query = input ("vad vill du söka efter:")
        if query.lowe()in bag:
             print(f"hittade {query} i påsen")
    else:
           query = input ("vad vill du söka efter:")

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)

    def style_text(code):
        return "\33[{code}m".format(code=code)

    def color_text(code):
        return "\33[{code}m".format(code=code)


example_ansi = ANSI.background(
    97) + ANSI.color_text(35) + ANSI.style_text(4) + " TESTE ANSI ESCAPE CODE"
print(example_ansi)

