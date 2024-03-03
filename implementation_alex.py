from core import gt_stratagy_base

class nice_stratagy(gt_stratagy_base):
    def __init__(self, name):
        super().__init__(name)

    def cooperate(self) -> bool:
        return True
    
class mean_stratagy(gt_stratagy_base):
    def __init__(self, name):
        super().__init__(name)

    def cooperate(self) -> bool:
        return False
    