
def readPuzzleFile(path: str) -> list[str]:
    with open(path, "r") as file:
        lines = file.readlines()
    return lines

def cleanPuzzleFileLines(lines: list[str]) -> list[str]:
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

def convertPuzzleFileToMatrix(puzzle: list[list[str]], puzzleSize: int) -> list[list[int]]:
    puzzleValues = set()
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            try:
                convertedValue = int(puzzle[row][col])
            except:
                raise ValueError("Puzzle values must be integers (e.g., 1, 2, 3, ...)")
            if convertedValue in puzzleValues:
                raise ValueError("Puzzle values must be unique")
            if convertedValue < 0 or convertedValue >= puzzleSize * puzzleSize:
                raise ValueError("Puzzle values are out of the allowed range.")
            puzzle[row][col] = convertedValue
            puzzleValues.add(convertedValue)
    return puzzle

def validatePuzzleFile(lines: list[str]) -> list[list[str]]:
    puzzle = []
    try:
        puzzleSize = int(lines[0])
    except ValueError:
        raise Exception("puzzle size is invalid")
    
    if puzzleSize < 3:
        raise ValueError("puzzle size has to be greater than 3")

    for line in lines[1:]:
        puzzle.append(line.strip().split())
    if len(puzzle) != puzzleSize:
        raise ValueError(f"puzzle height has to be match puzzle size: {puzzleSize}x{puzzleSize}")
    for line in puzzle:
        if len(line) != puzzleSize:
            raise ValueError(f"puzzle width has to be match puzzle size: {puzzleSize}x{puzzleSize}")
    convertPuzzleFileToMatrix(puzzle, puzzleSize)
    return puzzle

def main():
    try:
        lines = readPuzzleFile("./puzzle.txt")
        strippedLines = cleanPuzzleFileLines(lines)
        puzzle = validatePuzzleFile(strippedLines)
        print(puzzle)
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()
    