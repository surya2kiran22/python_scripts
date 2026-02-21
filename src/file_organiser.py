import os
import shutil

# print(os.getcwd())

#os.chdir(f'C:\\Users\\hp\\OneDrive\\Desktop\\python_rel\\test_folder')

# print(os.getcwd())
# os.mkdir('new_dir')


# print(os.listdir())

Extension_map = {"Documents": [".pdf", ".docx", ".txt"], "Images": [".jpg", ".png"], "Music": [".mp3"]}
file_count = {}

def chk_file_cnt():
    #to get count of file patterns
    for ext in Extension_map:
        #os.mkdir(ext)
        for pattern in Extension_map[ext]:
            print(pattern)
            print(os.listdir())
            file_count[pattern] = 0
            for file in os.listdir():
                if file.endswith(pattern):
                    file_count[pattern] = file_count[pattern]  + 1
                    print(file)
                    #shutil.move(file,ext)

def get_folder_name(pat):
    for category,pattern in Extension_map.items():
        if pat in pattern:
            #print(pat ,"is found",category)
            return category
        #else:
            #print(pat ,"not found",category)
    return "Other"

def chk_file(file,folder_path,folder):
    chk_folder = os.path.join(folder_path,folder)
    chk_file_path = os.path.join(chk_folder,file)
    i =0
    if file in os.listdir(chk_folder):
        print("file exist")
        file_nm = os.path.splitext(file)[0]
        ext = os.path.splitext(file)[1]
        while os.path.exists(chk_file_path):
            i=i+1
            new_name = f"{file_nm}_{i}{ext}"
            new_file_path = os.path.join(chk_folder,new_name)
            old_file_path = os.path.join(folder_path,file)
        shutil.move(old_file_path,new_file_path)
        
    else:
        print("file not exist")
        print("moved to ", folder)
        shutil.move(file,folder)
        

def org_folder(folder_path):
    os.chdir(folder_path)
    for file in os.listdir(folder_path):
        #print(file)
        if os.path.isfile(file):
            folder = get_folder_name(os.path.splitext(file)[1])
            try:
                if os.path.exists(folder):
                    chk_file(file,folder_path,folder)
                else:
                    os.mkdir(folder)
                    chk_file(file,folder,folder_path)
            except:
                print("unable to move file")
        else:
            print("not a file")
            continue

path = 'C:\\Users\\hp\\OneDrive\\Desktop\\python_rel\\test_folder'
org_folder(path)
#print(get_folder_name(".xlsx"))         

            

#print(file_count)


