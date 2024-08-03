import Actions

class Agent:

    def __init__(self,env = None) -> None:
        self.cur_state = None
        self.actions = [Actions.MOVE, Actions.STOP]     # left right actions will be taken care of statically, in simulation we will even code the agent to always follow one path
        self.environment = env
        if(self.environment):
            self.cur_state = self.environment.get_state()

    def get_actions(self)->list:
        return self.actions
    
    def get_legal_actions(self)->list:
        # return the actions possible from the cur_state
        return self.actions     # assuming that the path never has a end, it is always in the loop and no intersection