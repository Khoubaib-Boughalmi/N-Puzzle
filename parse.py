
def readFile(path: str) -> list[str]:
    with open(path, "r") as file:
        lines = file.readlines()
    return lines

def cleanFileLines(lines: list[str]) -> list[str]:
    cleanedLines = []
    for line in lines:
        try:
            shebangIndex = line.index("#")
            line = line[:shebangIndex].strip()
        except Exception as e:
            pass
        if line != "":
            cleanedLines.append(line)
    return cleanedLines

def parseFile(lines: list[str]) -> list[list[str]]:
    puzzle = []
    try:
        puzzleSize = int(lines[0])
    except ValueError:
        raise Exception("puzzle size is invalid")
    
    if puzzleSize < 3:
        raise ValueError("puzzle size has to be greater than 3")

    for line in lines[1:]:
        puzzle.append(line)

def main():
    try:
        lines = readFile("./puzzle.txt")
        strippedLines = cleanFileLines(lines)
        puzzle = parseFile(strippedLines)
        print(puzzle)
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()
    