

class Environment:

    def __init__(self, num_sensors:int = 3) -> None:
        self.num_sensors = num_sensors

    def get_state(self)->tuple:
        # this method returns the current state which is only the tuple of all the sensor values floored in that bin
        # for now, we simulate the sensor data
        pass


