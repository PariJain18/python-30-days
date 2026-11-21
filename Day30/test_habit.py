from habit import Habit


def test_habit_name():
    habit = Habit("Reading")
    assert habit.name == "Reading"


def test_habit_initial_status():
    habit = Habit("Exercise")
    assert habit.completed is False


def test_mark_completed():
    habit = Habit("Study")
    habit.mark_completed()
    assert habit.completed is True


def test_show_pending():
    habit = Habit("Walking")
    assert habit.show_status() == "Pending"


def test_show_completed():
    habit = Habit("Coding")
    habit.mark_completed()
    assert habit.show_status() == "Completed"