from datetime import date, datetime, timedelta
import matplotlib.pyplot as plt

class day_object:
    def __init__(self, date, deadline_list, prep_list):
        self.date = date
        self.deadline_list = deadline_list
        self.prep_list = prep_list

class event_object:
    def __init__(self, name, date, duration):
        self.name = name
        self.date = date
        self.duration = duration

def main():
    myDates = [
        event_object("Real-Time Graphics Task 2", date(2020, 12, 2), 13),
        event_object("AR Task 1", date(2020, 12, 3), 5),
        event_object("3DG&R Task 1", date(2020, 12, 9), 10),
        event_object("VT Task A3", date(2020, 12, 10), 5),
        event_object("AR Task 2", date(2020, 12, 23), 5),
        event_object("Real-Time Graphics Task 2", date(2021, 1, 13), 13),
        event_object("SPL Exam", date(2021, 1, 14), 10),
        event_object("AR Task 3", date(2021, 1, 19), 5),
        event_object("Real-Time Graphics Documentation", date(2021, 1, 20), 3),
        event_object("VT Task A4", date(2021, 1, 21), 5),
        event_object("3DG&R Exam", date(2021, 1, 27), 5),
        event_object("Real-Time Graphics Exam", date(2021, 1, 27), 5),
        event_object("VT Exam", date(2021, 2, 3), 5),
    ]

    first = myDates[0]
    last = myDates[0]
    for myDate in myDates:
        print("current date = " + myDate.name + "\n");
        if (timedelta(days=0) < ((first.date - timedelta(days=first.duration)) - (
                myDate.date - timedelta(days=myDate.duration)))):
            first = myDate

        if (timedelta(days=0) > (first.date - myDate.date)):
            last = myDate

    startDate = first.date - timedelta(days=first.duration)
    endDate = last.date
    dateDelta = endDate - startDate

    print("final first date: " + first.name + " with date: " + str(first.date) + " starting on: " + str(startDate))
    print("final date: " + last.name + " on: " + str(endDate))

    calendar = []


    for i in range(dateDelta.days + 1):
        day = startDate + timedelta(days=i)
        # print(day)
        calendar.append(day_object(day, [], []))


    for myDate in myDates:
        day = myDate.date - startDate
        # print("seeing " + str(calendar[day.days].date) + " as " + str(myDate.date));
        calendar[day.days].deadline_list.append(myDate.name)
        for i in range(myDate.duration+1):
            calendar[day.days - i].prep_list.append(myDate.name)

    for i in range(dateDelta.days + 1):
        day = startDate + timedelta(days=i)
        print("Events on " + str(calendar[i].date) + ": " + str(calendar[i].deadline_list) + " preparing for: " + str(calendar[i].prep_list)
              + " workload: " + str(len(calendar[i].prep_list)))


    # x axis values
    x = []
    # corresponding y axis values
    y = []


    for calendar_entry in calendar:
        x.append(calendar_entry.date.strftime("%d.%m.%Y"))
        y.append(len(calendar_entry.prep_list))

    # plotting the points
    plt.plot(x, y)

    plt.xticks(rotation=90)
    # naming the x axise
    plt.xlabel("Date")
    # naming the y axis
    plt.ylabel("Workload")

    # giving a title to my graph
    plt.title('Workload Plot')

    # function to show the plot
    plt.show()

if __name__ == "__main__":
    main()

