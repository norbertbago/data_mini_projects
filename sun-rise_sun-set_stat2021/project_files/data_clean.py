import json 
import csv

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
days = 1

with open('output.json', 'r') as json_file, \
     open('clean_data.csv','w') as output_csv:
     
     df = json.load(json_file)
     fields = ['days','days_in_month','month', 'sun_rise', 'sun_set']
     output_writer = csv.DictWriter(output_csv, fieldnames=fields)
     output_writer.writeheader()

     for key, values in df.items():
         for k,j in values.items():

            actual_month = months[values['number of month']-1]
            days_in_month = values['days in month']

           
        
         for p,s in values['days data'].items():

             sun_rise = s[s.index('Východ:')+len("Východ:"):s.index("Západ:")]
             sun_set  = s[s.index('Západ:')+len('Západ:'):] 

             output_writer.writerow({'days': days, 'days_in_month': int(p), 'month': actual_month, 'sun_rise': sun_rise, 'sun_set': sun_set})

             days += 1
             
                
     
     
