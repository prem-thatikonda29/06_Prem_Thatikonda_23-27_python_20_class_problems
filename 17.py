class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Project:
    def __init__(self, project_name):
        self.project_name = project_name

    def get_project_name(self):
        return self.project_name


class TimeEntry:
    def __init__(self, employee, project, hours):
        self.employee = employee
        self.project = project
        self.hours = hours

    def get_employee(self):
        return self.employee

    def get_project(self):
        return self.project

    def get_hours(self):
        return self.hours


class TimeTrackingSystem:
    def __init__(self):
        self.time_entries = []

    def log_hours(self, employee, project, hours):
        time_entry = TimeEntry(employee, project, hours)
        self.time_entries.append(time_entry)

    def generate_timesheet(self):
        print("Timesheet:")
        for entry in self.time_entries:
            print(f"Employee: {entry.get_employee().get_name()}, "
                  f"Project: {entry.get_project().get_project_name()}, "
                  f"Hours: {entry.get_hours()}")

    def calculate_overtime(self):
        standard_hours_per_week = 40
        total_hours = sum(entry.get_hours() for entry in self.time_entries)
        return max(0, total_hours - standard_hours_per_week)


# Example usage:
employee1 = Employee("John Doe")
employee2 = Employee("Jane Smith")

project1 = Project("Project A")
project2 = Project("Project B")

time_tracker = TimeTrackingSystem()

time_tracker.log_hours(employee1, project1, 8)
time_tracker.log_hours(employee2, project1, 7)
time_tracker.log_hours(employee1, project2, 6)

time_tracker.generate_timesheet()
print(f"Overtime: {time_tracker.calculate_overtime()} hours")
