class Person:
    def __init__(self, arrivalTime, priority, serviceTime):
        self.arrivalTime = arrivalTime
        self.priority = priority
        self.serviceTime = serviceTime
        self.startServiceTime = None
        self.departureTime = None
