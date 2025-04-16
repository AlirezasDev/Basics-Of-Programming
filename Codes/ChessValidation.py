piece = input()
startx = int(input())
starty = int(input())
endx = int(input())
endy = int(input())

if piece == "Bishop":
    if startx - endx == starty - endy and (startx - endx != 0):
        print("Bishop move is valid")
    else:
        print("Bishop move is not valid")

elif piece == "Knight":
    if ((abs(startx - endx)) == 2 and abs((starty - endy)) == 1) or (abs((startx - endx)) == 1 and abs((starty - endy)) == 2):
        print("Knight move is valid")
    else:
        print("Knight move is not valid")

elif piece == "Rook":
    if int(startx == endx) ^ int(starty == endy):
        print("Rook move is valid")
    else:
        print("Rook move is not valid")
