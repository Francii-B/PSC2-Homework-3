import random, timeit, statistics as st, numpy as np
import Sort_Module as s, Max_Heap as h, Tree_Module as t
import matplotlib.pyplot as plt


#a: generate the different lenght of the lists
#b: generate the largest list. Every smaller list is taken from it
a = np.logspace(1.4, np.log10(10000, dtype=float), base=10, endpoint=False, dtype=int)
b = random.choices(range(a[-1] + 1), k=a[-1])


#Function to measure the sorting time, and plotting the results
def Sorting_t(a,b):
    c=[]
    d=[]
    for i in a:
        ct=st.median(timeit.repeat(lambda: s.merge(b[:i]),repeat=10,number=1))
        c.append(ct)
        dt=st.median(timeit.repeat(lambda : s.QuickSort(b[:i]), repeat=10,number=1))
        d.append(dt)

    plt.figure(0)
    Show_graph(a,[c,d], ['Merge sort', 'Quick sort'])
    plt.title('Sorting time')
    
#Measurements of the Binary Search Tree (insertion of the whole tree, get and delete a random element, find max)
def Tree_t(a,b,Graph=True):

    Tree_d={'tot':[], 'init_l' : [] , 'max_l': [], 'get_l':[] , 'delete_l':[]}
    for i in a:
        #measure the time, and find the median
        bst = t.BinarySearchTree()
        init_t =st.median(timeit.repeat(lambda: bst.insertArr(b[:i]), repeat=10,number=1))
        max_t= st.median(timeit.repeat(lambda: bst.findMax(),repeat=40,number=1))
        get_t= st.median(timeit.repeat(lambda: bst.get(random.choice(bst.tree_el)),repeat=40,number=1))
        delete_t= st.median(timeit.repeat(lambda: bst.delete(random.choice(bst.tree_el)),repeat=20,number=1))

        #record the datas
        Tree_d['init_l'].append(init_t)
        Tree_d['max_l'].append(max_t)
        Tree_d['get_l'].append(get_t)
        Tree_d['delete_l'].append(delete_t)
        Tree_d['tot'].append(init_t + max_t + get_t + delete_t)

    if Graph: #plot only if it is required
        plt.figure(1)
        plt.subplot(211)
        plt.title('Binary Search Tree pt.1')
        Show_graph(a,[Tree_d['tot']], ['Total time'])
        plt.subplot(212)
        Show_graph(a,[Tree_d['init_l']], ['Insertion Time'])


        plt.figure(2)
        plt.title('Binary Search Tree pt.2')
        Show_graph(a, [Tree_d['get_l'],Tree_d['delete_l'],Tree_d['max_l']], ['Random Get', 'Random Delete', 'Find max'])

    return Tree_d


#Measurements for Max Heap (insertion of the whole array, get max, delete max)
def Heap_t(a,b, Graph=True):
    Heap_d={'tot':[],'init_l':[], 'max_l':[], 'deleteM_l':[]}

    for i in a:
        #measure the time
        mhp = h.MaxBinHeap()
        init_t = st.median(timeit.repeat(lambda: mhp.insertArr(b[:i]),repeat=10, number=1))
        max_t = st.median(timeit.repeat(lambda: mhp.getMax(),repeat=10, number=1))
        deleteM_t = st.median(timeit.repeat(lambda: mhp.delMax(),repeat=24, number=1))
        #record the datas
        Heap_d['init_l'].append(init_t)
        Heap_d['max_l'].append(max_t)
        Heap_d['deleteM_l'].append(deleteM_t)
        Heap_d['tot'].append(init_t + max_t + deleteM_t)

    if Graph: #plot only if it is required
        plt.figure(3)
        plt.subplot(211)
        plt.title('Max Heap pt.1')
        Show_graph(a,[Heap_d['tot']],['Total time'])
        plt.subplot(212)
        Show_graph(a,[Heap_d['init_l']],['Element Insertion'])


        plt.figure(4)
        plt.title('Max Heap pt.2')
        Show_graph(a, [Heap_d['max_l'],Heap_d['deleteM_l']],['Find max', 'Max delete'])
    return Heap_d

#Comparisons between the Tree and the Heap (total time, insertion of the whole list, insertion of a random element, get max)
def Comparisons(TD, HD):
    plt.figure(5)

    plt.subplot(211)
    plt.title('Comparisons between Heap and Tree')
    Show_graph(a, [TD['tot'], HD['tot']],['Tree total time','Heap total time'])

    plt.subplot(212)
    Show_graph(a, [TD['init_l'], HD['init_l']], ['Tree insertion', 'Heap insertion'])


#Plot the data when it is required
def Show_graph(a,l,lab):
    plt.grid(True)
    plt.xscale('symlog')
    plt.xlim(a[0],a[-1]+1)
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
    if True in answ_l:
        plt.show()

if __name__ == '__main__':
    Questions()
