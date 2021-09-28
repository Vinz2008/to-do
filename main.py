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
    print(todo)
    todo.append(things)
    open('todolist.txt', 'w').close()
    file=open('todolist.txt','a')
    a = 0
    for items in todo:
        linewrite = str(todo[a])
        file.writelines(linewrite+ "\n")
        a += 1
    file.close()
    print(todo)
if __name__ == '__main__':
    fire.Fire()
