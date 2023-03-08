try:
    import pandas as pd
    import glob
    import getpass
    import os
    from datetime import *
    import time
except ImportError:
    import os
    print("Installing dependencies...")
    os.system("pip3 install pandas")

today = date.today()
now = datetime.now()
current_time = now.strftime("%H")
real_date = (str(today)+"_"+str(current_time))

i = input("Do you want to merge different file and drop duplicates? (y/n)")
if i == 'y':
    # Definisci il percorso dei file CSV da unire
    print("Move all file to merge into ToMerge folder then press ENTER")
    input()
    user = getpass.getuser()
    path = '/home/'+user+'/Desktop/d0raCatch/Advance/ToMerge/*.csv'
    # Crea una lista dei nomi dei file CSV nel percorso specificato
    all_files = glob.glob(path)
    # Leggi i file CSV in un singolo DataFrame
    df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
    # Salva il DataFrame in un file CSV
    df.to_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/Wifi_merged_"+real_date+".csv", index=False)
    print("Files merged")
    i1 = input("Do you want to drop duplicates? (y/n)")
    if i1 == 'y':
        os.system("cp /home/"+user+"/Desktop/d0raCatch/Advance/Done/Wifi_merged_"+real_date+".csv /home/"+user+"/Desktop/d0raCatch/Advance/ToClean/")
        input_data = pd.read_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/Wifi_merged_"+real_date+".csv")
        filtered_data = input_data.drop_duplicates(subset=['MAC'])
        filtered_data.to_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/Cleaned_Wifi_merged_"+real_date, index=False)
        print("File Wifi_merged_"+real_date+".csv cleaned")
    else:
        exit(1)
else:
    print("Move all file to merge into ToClean folder then press ENTER")
    input()
    file = input("Enter file name: ")
    user = getpass.getuser()
    input_data = pd.read_csv("/home/"+user+"/Desktop/d0raCatch/Advance/ToClean/"+file)
    filtered_data = input_data.drop_duplicates(subset=['MAC'])
    filtered_data.to_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/Cleaned_"+file+"_"+real_date, index=False)
    print("File cleaned saved on /home/"+user+"/Desktop/d0raCatch/Advance/Done/")