class PDController:
    def __init__(self, Kp: float, Kd: float):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0.0

    def compute_action(self, reference_depth: float, current_depth: float, dt: float) -> float:
        error = reference_depth - current_depth
        derivative = (error - self.previous_error) / dt
        action = self.Kp * error + self.Kd * derivative
        self.previous_error = error
        return action