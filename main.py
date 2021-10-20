import fire
todo = []
def add(things):
    '''
    Add things to do
    '''
    with open("todolist.txt", "r") as f:
	    lines = f.readlines()
    for l in lines:
        todo.append(l.replace("\n", ""))
    
    todo.append(things)
    open('todolist.txt', 'w').close()
    file=open('todolist.txt','a')
    a = 0
    for items in todo:
        linewrite = str(todo[a])
        file.writelines(linewrite+ "\n")
        a += 1
    file.close()
    for i in todo:
    	print(i)
def clear():
    '''
    Clear everything in the todolist
    '''
    open('todolist.txt', 'w').close()

def delete(nb_del):
    '''
    delete a thing to do
    '''
    with open("todolist.txt", "r") as fd:
            lines = fd.readlines()
    for l in lines:
        todo.append(l.replace("\n", ""))
    if isinstance(nb_del, int) == True:
        nb_del = int(nb_del)
        del todo[nb_del]
    else:
        try:
            todo.remove(nb_del)
        except:
            print("This thing is not in the list")
    open('todolist.txt', 'w').close()
    b = 0
    fd=open('todolist.txt','a')   
    for items in todo:
        linewrite = str(todo[b])
        fd.writelines(linewrite+ "\n")
        b += 1
    fd.close()
def list():
    '''
    list all the things in the todolist
    '''
    with open("todolist.txt", "r") as f:
	    lines = f.readlines()
    for l in lines:
        todo.append(l.replace("\n", ""))
    for c in todo:
        print(c)

def reverse():
    '''
    Reverse the order of the things to do
    '''
    with open("todolist.txt", "r") as f:
            lines = f.readlines()
    for l in lines:
        todo.insert(0,l.replace("\n", ""))

    open('todolist.txt', 'w').close()
    file=open('todolist.txt','a')
    a = 0
    for items in todo:
        linewrite = str(todo[a])
        file.writelines(linewrite+ "\n")
        a += 1
    file.close()
if __name__ == '__main__':
    fire.Fire()

