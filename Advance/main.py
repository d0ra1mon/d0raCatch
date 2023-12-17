try:
    import pandas as pd
    import glob
    import getpass
    import os
    from datetime import *
    import time
    import folium
    from time import date
except ImportError:
    import os
    print("> Installing dependencies...")
    os.system("pip3 install pandas")
    os.system("pip3 install folium")

today = date.today()
now = datetime.now()
current_time = now.strftime("%H")
real_date = (str(today)+"_"+str(current_time))

i = input("> Do you want to merge different file and drop duplicates? (y/n)")
if i == 'y':
    # Definisci il percorso dei file CSV da unire
    print("> Move all file to merge into ToMerge folder then press ENTER")
    input()
    user = getpass.getuser()
    path = '/home/'+user+'/Desktop/d0raCatch/Advance/ToMerge/*.csv'
    # Crea una lista dei nomi dei file CSV nel percorso specificato
    all_files = glob.glob(path)
    # Leggi i file CSV in un singolo DataFrame
    df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
    # Salva il DataFrame in un file CSV
    df.to_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/Wifi_merged_"+real_date+".csv", index=False)
    print("> Files merged")
    i1 = input("> Do you want to drop duplicates? (y/n)")
    if i1 == 'y':
        os.system("cp /home/"+user+"/Desktop/d0raCatch/Advance/Done/Wifi_merged_"+real_date+".csv /home/"+user+"/Desktop/d0raCatch/Advance/ToClean/")
        input_data = pd.read_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/Wifi_merged_"+real_date+".csv")
        input_data = input_data[(input_data != 0.000000).all(1)]
        filtered_data = input_data.drop_duplicates(subset=['MAC']) 
        filtered_data.to_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/Cleaned_Wifi_merged_"+real_date+".csv", index=False)
        print("> File Cleaned_Wifi_merged"+real_date+".csv cleaned")
        os.system("rm /home/"+user+"/Desktop/d0raCatch/Advance/Done/Wifi_merged_"+real_date+".csv")
        os.system("rm /home/"+user+"/Desktop/d0raCatch/Advance/ToClean/Wifi_merged_"+real_date+".csv")
        data = pd.read_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/Cleaned_Wifi_merged_"+real_date+".csv")
        map = folium.Map(location=(30, 10), zoom_start=3)
        folium.TileLayer('stamenterrain').add_to(map)
        #folium.TileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',name='google maps',attr='Google').add_to(map)
        for index, row in data.iterrows():
            #reference: https://www.netspotapp.com/blog/wifi-security/wifi-encryption-and-security.html
            if row['AuthMode'] == "[ESS]":
                col = 'red'
            elif row['AuthMode'] == "[WEP][ESS]":
                col = 'orange'
            elif row['AuthMode'] == "[WPA-PSK-CCMP+TKIP][ESS]":
                col = 'lightgreen'
            elif row['AuthMode'] == "[WPA2-PSK-CCMP+TKIP][ESS]":
                col = 'green'
            marker = folium.Marker(location=[row['Latitude'], row['Longitude']], icon=folium.Icon(color=col))
            popup = folium.Popup(f"<b>MAC:</b><br>{row['MAC']}</br> <b>SSID:</b><br>{row['SSID']}</br> <b>AuthMode:</b><br>{row['AuthMode']}</br> <b>Channel:</b><br>{row['Channel']}</br> <b>RSSI:</b><br>{row['RSSI']}</br> <b>Latitude:</b><br>{row['Latitude']}</br> <b>Longitude:</b><br>{row['Longitude']}</br>")
            popup.add_to(marker)
            marker.add_to(map)
            marker.add_to(map)
        map.save("/home/"+user+"/Desktop/d0raCatch/Advance/Map/map"+real_date+".html")
        print("> Map "+real_date+".html saved")
    else:
        exit(1)
else:
    print("> Move all file to merge into ToClean folder then press ENTER")
    input()
    file = input("Enter file name: ")
    user = getpass.getuser()
    input_data = pd.read_csv("/home/"+user+"/Desktop/d0raCatch/Advance/ToClean/"+file)
    filtered_data = input_data.drop_duplicates(subset=['MAC'])
    filtered_data.to_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/Cleaned_"+file+"_"+real_date, index=False)
    print("> File cleaned saved on /home/"+user+"/Desktop/d0raCatch/Advance/Done/")
