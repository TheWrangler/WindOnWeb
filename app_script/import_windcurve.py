import os
import sqlite3

station_dict = {'huli':'湖里',  'haicang':'海沧', 'jimei':'集美', 'tongan':'同安', 'xiangan':'翔安', 'all':'全站'}

data_prefix_path = '/static/data/'

table = 'WindServer_windcurvemonth'
db_name = 'G:/WindOnWeb/db.sqlite3'
db_conn = sqlite3.connect(db_name)
db_cursor = db_conn.cursor()

dest_path = 'G:/WindOnWeb/WindServer/static/data/WS/同安/'
sub_files = os.listdir(dest_path)
for file in sub_files:
    pt = file.rfind('.')
    file_name = file[0:pt]
    sections = file_name.split('_')

    if station_dict.__contains__(sections[2].lower()):
        station = station_dict[sections[2].lower()]
    else: continue
    
    dt_from_to = sections[4].split('-')
    dt_str = dt_from_to[0]
    dt_from = dt_str[0:4] + '-' + dt_str[4:6] + '-' + '01'
    dt_str = dt_from_to[1]
    dt_to = dt_str[0:4] + '-' + dt_str[4:6] + '-' + '01'

    path = dest_path + file
    pt = path.find(data_prefix_path)
    img_src = path[pt : path.__len__()]

    sql_statement = "INSERT INTO " + table + "(station,date_from,date_to,img_src) VALUES (" + "'" + station + "','" + dt_from + "','" + dt_to + "','" + img_src +"')"
    db_cursor.execute(sql_statement)

db_conn.commit()
db_conn.close()