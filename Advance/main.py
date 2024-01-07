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
real_date = (str(today) + "_" + str(current_time))

def read_csv_with_error_handling(file_path):
    try:
        df = pd.read_csv(file_path)
        return df, None
    except pd.errors.ParserError as e:
        return None, f"Error reading file {file_path}: {e}"

i = input("> Do you want to merge different files and drop duplicates? (y/n)")
if i == 'y':
    print("> Move all files to merge into ToMerge folder then press ENTER")
    input()
    user = getpass.getuser()
    path = '/home/' + user + '/Desktop/d0raCatch/Advance/ToMerge/*.csv'
    all_files = glob.glob(path)

    dfs = []
    error_files = []

    for file_path in all_files:
        df, error = read_csv_with_error_handling(file_path)
        if df is not None:
            dfs.append(df)
        else:
            error_files.append(error)

    if error_files:
        print("Files with parsing errors:")
        for error in error_files:
            print(error)
        print("Exiting.")
        exit(1)

    if not dfs:
        print("No valid CSV files found. Exiting.")
        exit(1)

    df = pd.concat(dfs, ignore_index=True)
    df.to_csv("/home/" + user + "/Desktop/d0raCatch/Advance/Done/Wifi_merged_" + real_date + ".csv", index=False)
    print("> Files merged")

    i1 = input("> Do you want to drop duplicates? (y/n)")
    if i1 == 'y':
        os.system("cp /home/" + user + "/Desktop/d0raCatch/Advance/Done/Wifi_merged_" + real_date + ".csv /home/" + user + "/Desktop/d0raCatch/Advance/ToClean/")
        input_data = pd.read_csv("/home/" + user + "/Desktop/d0raCatch/Advance/Done/Wifi_merged_" + real_date + ".csv")
        input_data = input_data[(input_data != 0.000000).all(1)]
        filtered_data = input_data.drop_duplicates(subset=['MAC'])
        filtered_data.to_csv("/home/" + user + "/Desktop/d0raCatch/Advance/Done/Cleaned_Wifi_merged_" + real_date + ".csv", index=False)
        print("> File Cleaned_Wifi_merged" + real_date + ".csv cleaned")
        os.system("rm /home/" + user + "/Desktop/d0raCatch/Advance/Done/Wifi_merged_" + real_date + ".csv")
        os.system("rm /home/" + user + "/Desktop/d0raCatch/Advance/ToClean/Wifi_merged_" + real_date + ".csv")
        data = pd.read_csv("/home/" + user + "/Desktop/d0raCatch/Advance/Done/Cleaned_Wifi_merged_" + real_date + ".csv")
        map = folium.Map(location=(30, 10), zoom_start=3)
        folium.TileLayer('stamenterrain').add_to(map)

        for index, row in data.iterrows():
            if row['AuthMode'] == "[ESS]" or not pd.isna(row['Password']):
                col = 'red'
            elif row['AuthMode'] == "[WEP][ESS]":
                col = 'orange'
            elif row['AuthMode'] == "[WPA-PSK-CCMP+TKIP][ESS]":
                col = 'lightgreen'
            elif row['AuthMode'] == "[WPA2-PSK-CCMP+TKIP][ESS]":
                col = 'green'
            marker = folium.Marker(location=[row['Latitude'], row['Longitude']], icon=folium.Icon(color=col))
            popup = folium.Popup(
                f"<b>MAC:</b><br>{row['MAC']}</br> <b>SSID:</b><br>{row['SSID']}</br> <b>AuthMode:</b><br>{row['AuthMode']}</br> <b>Channel:</b><br>{row['Channel']}</br> <b>RSSI:</b><br>{row['RSSI']}</br> <b>Latitude:</b><br>{row['Latitude']}</br> <b>Longitude:</b><br>{row['Longitude']}</br> <b>Password:</b><br>{row['Password']}</br>")
            popup.add_to(marker)
            marker.add_to(map)
            marker.add_to(map)
        map.save("/home/" + user + "/Desktop/d0raCatch/Advance/Map/map" + real_date + ".html")
        print("> Map " + real_date + ".html saved")
    else:
        exit(1)
else:
    print("> Move all files to merge into ToClean folder then press ENTER")
    input()
    file = input("Enter file name: ")
    user = getpass.getuser()
    input_data = pd.read_csv("/home/" + user + "/Desktop/d0raCatch/Advance/ToClean/" + file)
    filtered_data = input_data.drop_duplicates(subset=['MAC'])
    filtered_data.to_csv("/home/" + user + "/Desktop/d0raCatch/Advance/Done/Cleaned_" + file + "_" + real_date, index=False)
    print("> File cleaned saved on /home/" + user + "/Desktop/d0raCatch/Advance/Done/")
