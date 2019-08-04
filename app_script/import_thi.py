import os
import sqlite3

station_dict = {'huli':'湖里',  'haicang':'海沧', 'jimei':'集美', 'tongan':'同安', 'xiangan':'翔安', 'all':'全站'}
thi_dict = {'hwind':'水平风', 'zwind':'垂直风'}

data_prefix_path = '/static/data/'

table = 'WindServer_windthi'
db_name = 'G:/WindOnWeb/db.sqlite3'
db_conn = sqlite3.connect(db_name)
db_cursor = db_conn.cursor()

dest_path = 'G:/WindOnWeb/WindServer/static/data/thi/翔安/'
sub_files = os.listdir(dest_path)
for file in sub_files:
    pt = file.rfind('.')
    file_name = file[0:pt]
    sections = file_name.split('_')

    if thi_dict.__contains__(sections[1].lower()):
        thi = thi_dict[sections[1].lower()]
    else: continue

    if station_dict.__contains__(sections[2].lower()):
        station = station_dict[sections[2].lower()]
    else: continue
    
    dt_str = sections[3]
    date_time = dt_str[0:4] + '-' + dt_str[4:6] + '-' + dt_str[6:8] + ' ' + dt_str[8:10] + ':' + dt_str[10:12] + ':' + dt_str[12:14]

    path = dest_path + file
    pt = path.find(data_prefix_path)
    img_src = path[pt : path.__len__()]

    sql_statement = "INSERT INTO " + table + "(direction,station,date_time,img_src) VALUES (" + "'" + thi + "','" + station + "','" + date_time + "','" + img_src +"')"
    db_cursor.execute(sql_statement)

db_conn.commit()
db_conn.close()