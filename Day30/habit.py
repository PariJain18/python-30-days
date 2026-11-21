class Habit:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def show_status(self):
        if self.completed:
            return "Completed"
        else:
            return "Pending"