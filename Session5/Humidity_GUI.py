from tkinter import *
import math

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

m = Tk()
m.title('Humidity')

# Define parameters
humidity = 100
center_x = CANVAS_WIDTH/2
center_y = CANVAS_HEIGHT/2
radius = 150
start_angle = 20
end_angle = 160
canvas = Canvas(m,width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')

# Calculate the angle on the arc (in degrees)

h_angle = humidity*140/100
angle_on_arc = 160 - h_angle

# Calculate the coordinates of the arc endpoint
angle_radians = math.radians(angle_on_arc)
end_x = center_x + radius * math.cos(angle_radians)
end_y = center_y - radius * math.sin(angle_radians)

# Draw the arc
arc1 = canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
start=start_angle, extent=end_angle - start_angle, width=30, style='arc', outline='green')

arc2=canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
start=start_angle+25, extent=25, width=30, style='arc', outline='yellow')

arc3=canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
start=start_angle, extent=25, width=30, style='arc', outline='red')

# Draw the line to the point on the arc
canvas.create_line(center_x, center_y, end_x, end_y, width=2)

canvas.create_text(center_x, center_y + 20, text=str(humidity)+"%", font=("Arial", 14))


canvas.grid(row=0,column=0)

m.mainloop()