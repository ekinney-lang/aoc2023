# %%
with open("./input2.txt") as file:
    input_lines = [line.strip() for line in file]


# %%
def getGameNumber(myString):
    # Split out game based on colon
    output = myString.split(":")
    return output


def splitGames(myString):
    # Split out each game by the semicolon using split()
    # This could probably just be a lamda function.
    output = myString.split(";")
    return output


def splitColorsAndCubes(myString):
    # Split out each of the green, red or blue values using split().
    # This could probably just be a lamda function.
    tempoutput = myString.split(",")
    temp = [tempstr.split() for tempstr in tempoutput]
    output = temp
    return output


def evaluateGame(myList):
    # Check each of the inputs of the list
    # temp = sorted(gamesSplit[0].strip(),key=lambda x: len(x))
    # Check Red using redIsGood, as long as it doesn't return null
    # Check Green using greenIsGood, as long as it doesn't return null
    # Check blue using blueIsGood, as long as it doesn't return null

    # Return the evaluation state for the game. If

    output = True
    return output


def redIsGood(myString):
    # Check Red has 12 or less cubes
    print("")


def greenIsGood(myString):
    # check Green has 13 or less cubes
    print("")


def blueIsGood(myString):
    # Check Blue is 14 or less cubes
    print("")


# %%
# This is our main functions to run through and get values out.
final_val = 0
# List comprehension based on which values are real
for line in input_lines:
    # Get the output split between game number and output
    output = getGameNumber(line)
    # Get just the game number's int. Only used if needed.
    gameNum = int("".join(filter(str.isdigit, output[0])))
    # Get to the next level of all the strings
    gameFullString = output[1]
    # Split the full string into each set of game
    gamesSplit = splitGames(gameFullString)
    # Evaluate the game
    validGame = evaluateGame(gamesSplit)
    # If a valid game, add to the total
    if validGame:
        final_val = final_val + gameNum
