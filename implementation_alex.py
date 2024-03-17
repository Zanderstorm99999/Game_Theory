from core import gt_stratagy_base
from random import randint

class AlexNiceStratagy(gt_stratagy_base):
    def __init__(self, append_random_name = False):
        super().__init__(append_random_name)

    def cooperate(self) -> bool:
        return True
    
class AlexMeanStratagy(gt_stratagy_base):
    def __init__(self, append_random_name = False):
        super().__init__(append_random_name)

    def cooperate(self) -> bool:
        return False
    
class AlexPassiveUntilAttackedStrategy(gt_stratagy_base):
    def __init__(self, append_random_name = False):
        super().__init__(append_random_name)
        
class AlexRandomStrategy(gt_stratagy_base):
    def __init__(self, append_random_name = False):
        super().__init__(append_random_name)
        
    def cooperate(self) -> bool:
        if randint(1, 2) == 1:
            return True
        else:
            return False
        
class AlexSwapStratagy(gt_stratagy_base):
    def __init__(self, append_random_name = False):
        super().__init__(append_random_name)
        