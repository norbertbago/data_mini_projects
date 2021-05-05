import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from scipy import stats



date_data = pd.read_csv("clean_data.csv") 
# sun_rise = date_data['sun_rise']
# days = date_data['days']
x = [1,2,3]
y = [2,4,6]

plt.plot(x,y)
plt.title('Our first graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,2,3,4])
plt.xticks([0,2,3,4,5,8,10])

plt.show()

# date_list_hours = []
# date_list_minutes = []

# hours_in_int = []
# minutes_in_int = []

# for time in sun_rise:

#     hours_in_int.append(int(time[:2]))
#     minutes_in_int.append(int(time[3:]))

#     date_time = datetime.strptime(time,'%H:%M')
    
#     date_list_hours.append(date_time.hour)
#     date_list_minutes.append(date_time.minute)

# # Average 
# avg_hour        = int(np.mean(date_list_hours))
# avg_minute      = int(np.mean(date_list_minutes))

# print('Average time of sun rise is {}:{}'.format(avg_hour, avg_minute))

# # Median 
# median_hour     = int(np.median(date_list_hours))
# median_minutes  = int(np.median(date_list_minutes))

# print('Median time of sun rise is {}:{}'.format(median_hour, median_minutes))

# Mode 
# mode_hour       = int(stats.mode(hours_in_int))
# mode_minutes    = int(stats.mode(minutes_in_int))

# print("Mode time of sun ruse is {}:{}".format(hours_in_int, minutes_in_int))