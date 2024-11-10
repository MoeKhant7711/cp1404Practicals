class Project:
    """Represent a project with details such as name, start date, priority, cost, and completion percentage."""

    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __repr__(self):
        return (f"Project(name={self.name}, start_date={self.start_date.strftime('%d/%m/%Y')}, "
                f"priority={self.priority}, cost_estimate=${self.cost_estimate:.2f}, "
                f"completion_percentage={self.completion_percentage}%)")

    def __lt__(self, other):
        return self.priority < other.priority
