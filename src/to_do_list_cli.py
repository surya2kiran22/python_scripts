import json

def file_read(file_name):
    file_tsk = []
    with open(file_name,'r') as file:
        file_tsk = json.load(file)
        return file_tsk

def save_file(file_name,data):
    with open(file_name,'w') as file:
        json.dump(data,file)
    return "updated file"

def cli_to_do_list():
    task = []
    file_name = 'tasks_lst.json'
    
    while True:
        cmd = input('enter what task action you want ADD,Search,Delete,View, EXIT: ')
        if cmd.upper() == 'VIEW':
            task = file_read(file_name)
            print(task)
            
        elif cmd.upper() == 'ADD':
            tsk_name = input("enter task name: ")
            tsk_status = input("enter task status: ")
            task = file_read(file_name)
            for i in range(len(task)):
                if task[i]['name'] == tsk_name:
                    print("name already exist")
            task1 = {"name":tsk_name,"done":tsk_status}
            task.append(task1)
            save_file(file_name,task)
        elif cmd.upper() == 'DELETE':
            tsk_name = input("enter task name to delete: ")
            task = file_read(file_name)
            for i in range(len(task)):
                if task[i]['name'] == tsk_name:
                    del task[i]
                    break
                else:
                    print("name not exist")
            save_file(file_name,task)
        elif cmd.upper() == 'EXIT':
            break



cli_to_do_list()
