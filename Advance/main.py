try:
    import pandas as pd
    import glob
    import getpass
except ImportError:
    import os
    print("Installing dependencies...")
    os.system("pip install pandas")

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
    df.to_csv('/home/'+user+'/Desktop/d0raCatch/Advance/Done/Wifi_merged.csv', index=False)
    print("Files merged")
else:
    file = input("Enter file name: ")
    input_data = pd.read_csv(file)
    filtered_data = input_data.drop_duplicates(subset=['MAC'])
    user = getpass.getuser()
    filtered_data.to_csv("/home/"+user+"/Desktop/d0raCatch/Advance/Done/C_"+file, index=False)