import numpy as np

class IRSensor:

    def __init__(self,sensor_range,x_rel,y_rel):
        self.sensor_range = sensor_range
        # from the frame of reference of robot
        self.x = x_rel
        self.y = y_rel

    def read_data(self):
        pass