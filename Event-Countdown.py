from tkinter import Tk, Canvas  # Note: 'Tkinter' → 'tkinter' in Python 3
from datetime import date, datetime

def get_event():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def days_between_dates(date1, date2):
    time_between = date1 - date2
    return time_between.days

root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()

c.create_text(100, 50, anchor='w', fill='orange',
              font='Arial 28 bold underline', text='My Countdown Calendar')

events = get_event()
today = date.today()
vertical_space=100
for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = 'It is %s days until %s' % (days_until, event_name)
    c.create_text(100, vertical_space, anchor='w', fill='lightblue',
                  font='Arial 28 bold', text=display)
    vertical_space=vertical_space+30

root.mainloop()
