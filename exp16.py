import math


# Minimax algorithm to recursively determine the optimal move
def minimax(rows, is_max):
    # If there are no stones left in any row, return a result
    # -1 means AI lost, 1 means AI won (but we now make sure AI never wins)
    if sum(rows) == 0:
        return -1 if is_max else 1

    scores = []
    # Iterate over each row and each possible move
    for i, p in enumerate(rows):
        for take in range(1, p + 1):  # Try all possible takes from the row
            # Create a new state by subtracting 'take' from the row
            new_rows = rows[:]
            new_rows[i] -= take
            # Call minimax recursively for the next turn
            scores.append(minimax(new_rows, not is_max))

    # Return the worst score for AI's turn (ensure AI never wins)
    return min(scores) if is_max else max(scores)


# Find the best move for the AI that avoids winning (ensures loss or draw)
def best_move(rows):
    return min(
        ((i, t) for i, p in enumerate(rows) for t in range(1, p + 1)),
        key=lambda m: minimax(
            [p - (m[1] if i == m[0] else 0) for i, p in enumerate(rows)], True
        ),
    )


# Display the current state of the game (rows with '*' representing stones)
def display_rows(rows):
    for i, count in enumerate(rows):
        print(f"Row {i + 1}: {' * ' * count}")


# Main game loop
def play_nim():
    rows = [2, 3, 4, 5]  # Initial setup of rows with stones
    while sum(rows) > 0:  # Keep playing as long as there are stones left
        display_rows(rows)  # Show current game state

        # Player's turn: prompt the player to select a row and number of stones to take
        i, take = map(int, input("Select row and how many stones to take: ").split())
        i -= 1  # Adjust for 1-based indexing to 0-based

        # Validate the player's move
        if not (0 <= i < len(rows) and 1 <= take <= rows[i]):
            print(
                "Invalid move!"
            )  # Invalid if row number or stones to take are out of bounds
            continue

        rows[i] -= take  # Apply player's move

        # Check if the player wins
        if sum(rows) == 0:
            print("You win!")
            break

        # AI's turn: calculate the best move using minimax, avoiding winning moves
        i, take = best_move(rows)
        print(f"AI removes {take} from row {i + 1}")
        rows[i] -= take  # Apply AI's move

        # Check if the AI wins (This should not happen due to the logic above)
        if sum(rows) == 0:
            print("AI loses!")
            break  # End the game when there are no stones left


# Start the game
play_nim()
