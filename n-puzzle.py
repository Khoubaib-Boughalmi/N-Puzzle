from parse import parsePuzzleFile
import sys

def generateFinalPuzzle(puzleSize: int) -> list[list[int]]:
    pass

def main(*args):
    try:
        initPuzzle = parsePuzzleFile(args[1])
        print(initPuzzle)
        finalPuzzle = generateFinalPuzzle(len(initPuzzle))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Wrong number of arguments please provide puzzle file name")
    main(*sys.argv)