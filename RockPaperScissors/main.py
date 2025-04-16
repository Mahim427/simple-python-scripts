import random
import sys


class RPS:
    def __init__(self):
        print("Welcome to Rock Paper Scissors!")

        self.user_score = 0
        self.ai_score = 0

        self.moves: dict = {"rock": '🪨', "paper": '📜', "scissors": '✂'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input("Rock, Paper or Scissors? -> ").lower()
        if user_move == 'exit':
            print("Thank you for playing!")
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move. Please enter a valid move.")
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)
        self.display_scores()

    def display_scores(self):
        print(f"You: {self.user_score} / AI: {self.ai_score}")
        print("-----")

    def display_moves(self, user_move: str, ai_move: str):
        print('-----')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('-----')

    def check_moves(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print("It's a draw!")
        elif (
            (user_move == 'rock'and ai_move == 'scissors')
            or (user_move == 'paper'and ai_move == 'rock')
            or (user_move == 'scissors' and ai_move == 'paper')
        ):
            print("You Win!")
            self.user_score += 1
        else:
            print("Ai Wins!")
            self.ai_score += 1


if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()
