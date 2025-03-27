"""EX02 - Wordle - A simple word-guessing game implementation."""

__author__ = "730565431"  

WHITE_BOX: str = "\U00002B1C"  
GREEN_BOX: str = "\U0001F7E9"  
YELLOW_BOX: str = "\U0001F7E8"  


def contains_char(word: str, char: str) -> bool:
    """Checks if a given character is present in the word."""
    assert len(char) == 1, f"len('{char}') is not 1"  
    
    for letter in word:
        if letter == char:
            return True  
    
    return False  

def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis representing the correctness of a Wordle guess."""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    result: str = ""

    
    for index in range(len(guess)):
        if guess[index] == secret[index]:  
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):  
            result += YELLOW_BOX
        else:  
            result += WHITE_BOX

    return result


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess of the correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """Runs the main game loop for Wordle, allowing up to 6 guesses."""
    max_turns: int = 6  
    current_turn: int = 1
    game_won: bool = False  

    while current_turn <= max_turns and not game_won:
        print(f"=== Turn {current_turn}/{max_turns} ===")

        guess: str = input_guess(len(secret))  
        result: str = emojified(guess, secret)  
        print(result)

        if guess == secret:
            game_won = True
            print(f"You won in {current_turn}/{max_turns} turns!")  
        else:
            current_turn += 1  

    if not game_won:
        print("X/6 - Sorry, try again tomorrow!")  

if __name__ == "__main__":
    main(secret="codes") 
