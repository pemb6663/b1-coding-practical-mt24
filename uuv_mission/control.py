import numpy as np

class Controller:
    def __init__(self, Kp=0.1, Kd=0.65):
        self.Kp = Kp
        self.Kd = Kd
        self.err_prev = 0

    def compute_control(self, reference, depth):
        err = reference - depth
        u = self.Kp * err + self.Kd * (err - self.err_prev)
        self.err_prev = err
        return u