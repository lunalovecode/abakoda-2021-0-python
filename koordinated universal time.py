import math

arg_1 = input()
arg_2 = input()

def to_mins(string):
	parts = string.split()

	hrs = abs(int(parts[0]))
	mins = abs(int(parts[1]))

	if len(parts) == 2:
		return (hrs * 60) + mins

	if parts[2] == "AM":
		if parts[0] == 12:
			return mins

		return (hrs * 60) + mins

	if parts[2] == "PM":
		if parts[0] == 12:
			return 720 + mins
		
		return 720 + (hrs * 60) + mins

def to_AM_PM(total_mins):
	hrs = math.floor(total_mins / 60)

	mins = total_mins % 60
	
	return hrs + " " + str(mins) + " AM";

	if hrs > 12:
		return str(hrs - 12) + " " + str(mins) + " PM"
 
	if hrs == 12:
		return "12 " + str(mins) + " PM"
    
 
	if hrs == 0:
		hrs = 12


def get_time_diff(string):
	parts = string.split()
	tz = to_mins(string)

	if int(parts[0]) < 0:
		tz = tz * -1

	return 480 - tz

def get_coord_time(current_time, time_zone):
	current_time_mins = to_mins(current_time)
	time_diff = get_time_diff(time_zone)
	coordinated_time_mins = current_time_mins - time_diff

	if coordinated_time_mins < 0:
		coordinated_time_mins = (24 * 60) + coordinated_time_mins;
		return to_AM_PM(coordinated_time_mins);

print(get_coord_time(arg_1, arg_2));