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
    splitAll = [splitColorsAndCubes(game) for game in myList]
    # Check Red using redIsGood, as long as it doesn't return null
    # for game in splitAll:
    #     if game[1] == 'red'
    #         redValGood = 
    # Check Green using greenIsGood, as long as it doesn't return null
    # Check blue using blueIsGood, as long as it doesn't return null

    # Return the evaluation state for the game. If

    output = True
    return output


def redIsGood(myString):
    # Check Red has 12 or less cubes
    inVal = int(myString)
    if inVal<=12:
        isGood = True
    else
        isGood = False
    return isGood
    


def greenIsGood(myString):
    # check Green has 13 or less cubes
        inVal = int(myString)
    if inVal<=12:
        isGood = True
    else
        isGood = False
    return isGood


def blueIsGood(myString):
    # Check Blue is 14 or less cubes
        inVal = int(myString)
    if inVal<=12:
        isGood = True
    else
        isGood = False
    return isGood

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

# %%
examplePass = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']
exampleFail = ['Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red']


# %%
