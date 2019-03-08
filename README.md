# Python_Wheel_of_-Fortune_Game
Created Wheel_of_ Fortune_Game using python code

You will create a program that is a simple game of Wheel of Fortune
(http://en.wikipedia.org/wiki/Wheel_of_Fortune_(U.S._game_show)).

Here are the details of the Game:
1. Download a file named wheel_puzzles.txt, and wheel_values.txt
2. Read in a file that has puzzles and store the puzzles in a list. The file name is wheel_puzzles.txt.
3. Read in a file that has scores for the wheel and store the scores in a list. The file name is wheel_values.txt
4. Choose a random puzzle
5. Display the puzzle to the user as underscores
6. Ask three players to enter their name
7. Tell the first player his or her name and score (initially the score is 0)
8. Ask the player to spin or solve the puzzle
a. If the player chooses spin, randomly choose a value from the list of scores
i. A value of -1 is Bankrupt and the player loses his or her turn and the score is set to 0
ii. A value of -2 is Lose a Turn. The player loses his or her turn.
iii. If the player gets a value other than -1 and -2, ask the player to buy a letter.
iv. If the letter is in the puzzle, display the puzzle with the letter showing
v. If the letter is not in the puzzle, the player loses his or her turn
vi. If the letter is already guessed, the player loses his or her turn (this means you must use a list to keep up with previous guesses)
b. If the player choses solve the puzzle, ask the player to enter in the puzzle
i. Check to see if the player’s input matches the puzzle
ii. If the player’s input matches the puzzle, show the player his or her current score, and end the game
iii. If the player’s input does not match the puzzle, the player loses his or her turn
9. If the player guesses a correct letter
a. Show the player his/her score
b. Display the puzzle with the letter the player guesses
10. If the player goes bankrupt or loses his turn
a. Show the next player his/her score
b. Ask the player if he/she wants to spin or solve
11. Continue playing the game until a player solves the puzzle or guesses all letters
