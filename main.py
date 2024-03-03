from core import calculate_score, gt_stratagy_base

class game():
    def __init__(self, player1: gt_stratagy_base, player2: gt_stratagy_base) -> None:
        self.player1 = player1
        self.player2 = player2

    def start(self, count: int) -> list:
        list_of_scores = []
        for count in range(count):
            player1_score, player2_score = calculate_score(self.player1.cooperate(), self.player2.cooperate())
            self.player1.update_score(player1_score)
            self.player2.update_score(player2_score)
            list_of_scores.append((player1_score, player2_score))

        return list_of_scores
    
if __name__ == "__main__":
    from implementation_alex import nice_stratagy, mean_stratagy
    player1 = mean_stratagy("Alex")
    player2 = nice_stratagy("Person")
    game_instance = game(player1, player2)

    print(game_instance.start(10))