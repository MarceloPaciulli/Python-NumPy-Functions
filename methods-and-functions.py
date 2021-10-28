import numpy as np


a = np.random.randint(1,5,(10,))
print(a)
print(np.sort(a))
print(np.unique(a))

#-------------------------------------------------------------


def get_targets_1(T):    
    freq,lista = [],[]
    rodar = np.array([1])[np.newaxis,:]
    clases = np.unique(T)
    rodar = np.delete(np.concatenate((rodar,np.zeros((1,clases.size))),axis=1),-1)
    e = list(T)
    for elem in clases:
        freq.append(e.count(elem))
    for pos, item in enumerate(freq):
        for k in range(item):
            lista.append(np.roll(rodar,pos))
    resultado = np.array(lista).reshape(len(T), clases.size)
    return resultado         

#----------------------------------------------------------------


def get_targets_2(T):    
    freq,lista = [],[]
    clases = np.unique(T)
    rodar = np.eye(len(clases))
    e = list(T)
    for elem in clases:
        freq.append(e.count(elem))
    for pos, item in enumerate(freq):
        for k in range(item):
            lista.append(rodar[pos])
    resultado = np.array(lista).reshape(len(T), clases.size)
    return resultado          

#-----------------------------------------------------------------


def get_targets_3(T):   
    freq = []
    clases = np.unique(T)
    t = np.zeros((len(T),clases.size))
    rodar = np.delete(np.r_[np.array([1]),np.zeros((1,clases.size)).flatten()],-1)
    for elem in clases:
        freq.append(list(T).count(elem))
    index=0
    for pos, item in enumerate(freq):
            t[index:index+item]=np.roll(rodar,pos)
            index+=item
    return t                  

#----------------------------------------------------------------


def get_targets_4(T):    
    clases = np.unique(T)
    t = np.zeros((len(T),clases.size))
    rodar = np.delete(np.hstack((np.eye(1),np.zeros((1,clases.size)))),-1)
    freq={elem: list(T).count(elem) for elem in clases}
    index=0
    for pos, item in enumerate(clases):
            t[index:index+freq[item]]=np.roll(rodar,pos)
            index+=freq[item]
    return t                  
#----------------------------------------------------------------

def get_targets_5(T):    
    clases = np.unique(T)
    t = np.zeros((len(T),clases.size))
    rodar = np.delete(np.hstack((np.eye(1),np.zeros((1,clases.size)))),-1)
    freq=list({elem: list(T).count(elem) for elem in clases}.values())
    index=0
    for pos in range(len(clases)):
            t[index:index+freq[pos]]=np.roll(rodar,pos)
            index=np.cumsum(freq)[pos]
    return t                  

#------------------------------------------------------------------

def get_targets_6(T):    
    clases = np.unique(T)
    t = np.zeros((len(T),clases.size))
    rodar = np.delete(np.hstack((np.eye(1),np.zeros((1,clases.size)))),-1)
    freq={elem: list(T).count(elem) for elem in clases}
    index=0
    for pos, item in enumerate(clases):
            t[index:index+freq[item]]=np.roll(rodar,pos)
            index=np.cumsum(list(freq.values()))[pos]
    return t                  


#----------------------------------------------------------------

def get_targets_7(T):
	clases = np.unique(T)
	target = np.array([]).reshape(0,clases.size)
	for pos,item in enumerate(clases):
		a = np.zeros_like(clases)
		a[pos]=1
		block = np.tile(a,((T==item).sum(),1))
		target=np.vstack((target,block))
	return target
#-----------------------------------------------------------------        

def get_targets_8(T):
	clases = np.unique(T)
	target = np.eye(0).reshape(0,clases.size)
	for pos,item in enumerate(clases):
		a = np.insert(np.zeros((clases.size-1)),pos,1)
		block = np.tile(a,((T==item).sum(),1))
		target=np.vstack((target,block))
	return target
#------------------------------------------------------------------

def get_targets_9(T):
	clases = np.unique(T)
	target = np.eye(0).reshape(0,clases.size)
	for pos,item in enumerate(clases):
		block = np.tile(np.eye(len(clases))[pos],((T==item).sum(),1))
		target=np.vstack((target,block))
	return target

#-----------------------------------------------------------------

def get_targets_10(t):
	init,clases = 0,np.unique(t)
	t1 = np.zeros((len(t),clases.size))
	w = np.ones_like(t1)
	for k,elem in enumerate(clases):
		cantidad = list(t).count(elem)
		condlist = [w[init:init+cantidad]==1]
		choicelist=[np.eye(len(clases))[k]]
		t1[init:init+cantidad]=np.select(condlist,choicelist)
		init+=cantidad
	return t1
#-----------------------------------------------------------------
            
def get_targets_11(t):                                          
	init = 0
	clases = np.unique(t)
	fila = np.delete(np.insert(np.zeros_like(clases),0,1),-1)
	target = np.eye(0).reshape(0,clases.size)
	w = np.ones((len(t),clases.size))
	for k,elem in enumerate(clases):
		cantidad = list(t).count(elem)
		condlist = [w[init:init+cantidad]==1]
		choicelist=[np.roll(fila,k)]
		target = np.vstack((target,np.select(condlist,choicelist)))
		init+=cantidad
	return target

#------------------------------------------------------------------

def get_targets_12(t):                               
	init = 0
	clases = np.unique(t)
	t1 = np.zeros((len(t),clases.size))
	fila = np.delete(np.insert(np.zeros_like(clases),0,1),-1)
	w = np.ones((len(t),clases.size))
	for k,elem in enumerate(clases):
		cantidad = list(t).count(elem)
		condlist = [w[init:init+cantidad]==1]
		choicelist=[np.roll(fila,k)]
		t1[init:init+cantidad]=np.select(condlist,choicelist)
		init+=cantidad
	return t1


#let's try!

print(get_targets_1(a))


