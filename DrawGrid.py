def drawGrid(width, height):
    endLine = "+"
    internalLine = "|"

    for i in range(width):
        endLine = endLine + "-"
        internalLine = internalLine + " "
    endLine = endLine + "+"
    internalLine = internalLine + "|"

    print(endLine)

    for i in range(height):
        print(internalLine)

    print(endLine)

drawGrid(3,4)