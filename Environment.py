import Layouts

class Environment:

    def __init__(self, num_sensors:int = 3,layout:list = Layouts.layout1,facing:str = Layouts.layout1f) -> None:
        self.num_sensors = num_sensors
        self.layout = layout
        for i in range(len(self.layout)):
            for j in range(len(self.layout[i])):
                if self.layout[i][j]=='T':
                    self.bot_position = (i,j)
        self.facing = facing

    def get_state(self)->tuple:
        # this method returns the current state which is only the tuple of all the sensor values floored in that bin
        # for now, we simulate the sensor data received from the self.bot_position
        pass