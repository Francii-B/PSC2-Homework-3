import random
import timeit
import numpy as np
import Sort_Module as s
import Max_Heap as h
import Tree_Module as t
import matplotlib.pyplot as plt

#a: generate the different lenght of the lists
#b: generate the largest list. Every smaller list is taken from it
a = np.logspace(1.0, np.log10(10000, dtype=float), base=10, endpoint=False, dtype=int)
b = random.choices(range(a[-1] + 1), k=a[-1])


#Function to measure the sorting time, and plotting the results
def Sorting_t(a,b):
    c=[]
    d=[]
    for i in a:
        ct=timeit.timeit(lambda: s.merge(b[:i]),number=10 )
        c.append(ct)
        dt=timeit.timeit(lambda : s.QuickSort(b[:i]), number=10)
        d.append(dt)

    Show_graph(a,[c,d], ['Merge sort', 'Quick sort'])
    plt.title('Sorting time')
    plt.show()

#Measurements of the Binary Search Tree (insertion of the whole tree, get and delete and insert a random element, find max)
def Tree_t(a,b,Graph=True):
    Tree_d={'tot':[], 'init_l' : [] , 'max_l': [], 'get_l':[] , 'delete_l':[], 'insert_l':[]}
    for i in a:
        random_el = random.choice(b[:i]) #use always the same random element
        #measure the time
        bst = t.BinarySearchTree()
        init_t = timeit.timeit(lambda: bst.insertArr(b[:i]), number=10)/10
        max_t= timeit.timeit(lambda: bst.findMax(), number=10)/10
        get_t= timeit.timeit(lambda: bst.get(random_el), number=10)/10
        insert_t = timeit.timeit(lambda: bst.put(random_el), number=10)/10
        delete_t=timeit.timeit(lambda: bst.delete(random_el), number=10)/10
        
        #record the datas
        Tree_d['init_l'].append(init_t)
        Tree_d['max_l'].append(max_t)
        Tree_d['get_l'].append(get_t)
        Tree_d['delete_l'].append(delete_t)
        Tree_d['insert_l'].append(insert_t)
        Tree_d['tot'].append(init_t + max_t + get_t + delete_t+ insert_t)

    if Graph: #plot only if it is required
        plt.figure(1)
        plt.subplot(211)
        plt.title('Binary Search Tree pt.1')
        Show_graph(a,[Tree_d['tot']], ['Total time'])
        plt.subplot(212)
        Show_graph(a,[Tree_d['init_l']], ['Insertion Time'])

        plt.figure(2)
        plt.title('Binary Search Tree pt.2')
        Show_graph(a, [Tree_d['get_l'],Tree_d['delete_l'],Tree_d['max_l'], Tree_d['insert_l']], ['Random Get', 'Random Delete', 'Find max', 'Random Insert'])
        plt.show()

    return Tree_d

#Measurements for Max Heap (insertion of the whole array, insetion of a random element, get max, delete max)
def Heap_t(a,b, Graph=True):
    Heap_d={'tot':[],'init_l':[], 'max_l':[], 'deleteM_l':[], 'insert_l': []}

    for i in a:
        random_el = random.choice(b[:i]) #generate a random element
        #measure the time
        mhp = h.MaxBinHeap()
        init_t = timeit.timeit(lambda: mhp.insertArr(b[:i]), number=10)/10
        max_t = timeit.timeit(lambda: mhp.getMax(), number=10)/10
        deleteM_t = timeit.timeit(lambda: mhp.delMax(), number=10)/10
        insert_t = timeit.timeit(lambda: mhp.insert(random_el), number=10)/10
        #record the datas
        Heap_d['init_l'].append(init_t)
        Heap_d['max_l'].append(max_t)
        Heap_d['deleteM_l'].append(deleteM_t)
        Heap_d['insert_l'].append(insert_t)
        Heap_d['tot'].append(init_t + max_t + deleteM_t + insert_t)

    if Graph: #plot only if it is required
        plt.figure(3)
        plt.subplot(211)
        plt.title('Max Heap pt.1')
        Show_graph(a,[Heap_d['tot']],['Total time'])
        plt.subplot(212)
        Show_graph(a,[Heap_d['init_l']],['Element Insertion'])

        plt.figure(4)
        plt.title('Max Heap pt.2')
        Show_graph(a, [Heap_d['max_l'],Heap_d['deleteM_l'], Heap_d['insert_l']],['Find max', 'Random delete', 'Random Insert'])
        plt.show()
    return Heap_d

#Comparisons between the Tree and the Heap (total time, insertion of the whole list, insertion of a random element)
def Comparisons(TD, HD):
    plt.figure(5)
    plt.subplot(311)
    plt.title('Comparisons between Heap and Tree')
    Show_graph(a, [TD['tot'], HD['tot']],['Tree total time','Heap total time'])

    plt.subplot(312)
    Show_graph(a, [TD['init_l'], HD['init_l']], ['Tree insertion', 'Heap insertion'])

    plt.subplot(313)
    Show_graph(a, [TD['insert_l'], HD['insert_l']], ['Tree Random insertion', 'Heap Random insertion'])
    plt.show()

#Plot the data when it is required
def Show_graph(a,l,lab):
    plt.grid(True)
    plt.xscale('symlog')
    plt.xlim(10,8800)
    for j in range(len(lab)):
        plt.plot(a, l[j], '.-', label=lab[j])
    plt.ylabel('Time')
    plt.xlabel('Lenght of the list')
    plt.legend(loc='upper left', shadow=True)

#Ask what the user wants to visualize
def Questions():
    answ_l=[]
    print('Please, answer "YES" to the following questions,if you are interested','Would you like to visualize...', sep='\n')
    for q in ['...the Sorting time?', '...the BST time?', '...the Max Heap time?', '...and the Comparisons between BST and Heap?']:
        answ=input(q).strip()
        if answ.upper()=='YES':
            answ_l.append(True)
        else:
            answ_l.append(False)

    #Call the functions, according to the user's choices
    if answ_l[0]:
        Sorting_t(a,b)
    if answ_l[3] :
        Comparisons(Tree_t(a,b, answ_l[1]), Heap_t(a,b, answ_l[2]))
    else:
        if answ_l[1]:
            Tree_t(a,b)
        if answ_l[2]:
            Heap_t(a,b)

Questions()
