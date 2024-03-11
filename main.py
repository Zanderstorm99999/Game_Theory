from core import calculate_score, gt_stratagy_base
from typing import List
from implementation_alex import nice_stratagy, mean_stratagy

def make_list_of_tuples(list_of_strategies):
    list_of_tuple_pairs = []
    
    for i in range(len(list_of_strategies)):
        for strategy in list_of_strategies[i:]:
            list_of_tuple_pairs.append((list_of_strategies[i:][0], strategy))
            
        # for strategy in list_of_strategies[1:]:
        #     list_of_tuple_pairs.append((list_of_strategies[1:][0], strategy))
            
        # for strategy in list_of_strategies[2:]:
        #     list_of_tuple_pairs.append((list_of_strategies[2:][0], strategy))
        
    return list_of_tuple_pairs
    

class Game():
    
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
    

class GameRunner():
    
    def __init__(self, players: List[gt_stratagy_base]):
        self.player_pairs = make_list_of_tuples(players) # TODO: add a function to create the play_pair tuple
    
    def run(self, count: int):
        for player_tuple in self.player_pairs:
            player1, player2 = player_tuple
            game_instance = Game(player1, player2)
            print(game_instance.start(count))
            
    
if __name__ == "__main__":
    runner = GameRunner([mean_stratagy("Alex"), nice_stratagy("Person")])
    runner.run(10)
    
    # player1 = mean_stratagy("Alex")
    # player2 = nice_stratagy("Person")
    # game_instance = Game(player1, player2)

    # print(game_instance.start(10))