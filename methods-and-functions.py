import numpy as np


a = np.random.randint(1,5,(10,))
print(a)
print(np.sort(a))
print(np.unique(a))


#one-hot encoding functions

def one_hot_encoding(T):
    types = np.unique(T)
    targets = np.eye(0).reshape(0,types.size)
    for pos,item in enumerate(types):
        a = np.insert(np.zeros((types.size-1)),pos,1)
        block = np.tile(a,((np.array(T)==item).sum(),1))
        targets=np.vstack((targets,block))
    return targets

#-------------------------------------------------------------------------------------------

def one_hot_encoding2(T):    
    freq,lista = [],[]
    moving = np.array([1])[np.newaxis,:]
    types = np.unique(T)
    moving = np.delete(np.concatenate((moving,np.zeros((1,types.size))),axis=1),-1)
    e = list(T)
    for elem in types:
        freq.append(e.count(elem))
    for pos, item in enumerate(freq):
        for k in range(item):
            lista.append(np.roll(moving,pos))
    targets = np.array(lista).reshape(len(T), types.size)
    return targets  

#-------------------------------------------------------------------------------------------

def one_hot_encoding3(T):    
    freq,lista = [],[]
    types = np.unique(T)
    moving = np.eye(len(types))
    e = list(T)
    for elem in types:
        freq.append(e.count(elem))
    for pos, item in enumerate(freq):
        for k in range(item):
            lista.append(moving[pos])
    targets = np.array(lista).reshape(len(T), types.size)
    return targets     

#-------------------------------------------------------------------------------------------

def one_hot_encoding4(T):   
    freq = []
    types = np.unique(T)
    targets = np.zeros((len(T),types.size))
    moving = np.delete(np.r_[np.array([1]),np.zeros((1,types.size)).flatten()],-1)
    for elem in types:
        freq.append(list(T).count(elem))
    index=0
    for pos, item in enumerate(freq):
            targets[index:index+item]=np.roll(moving,pos)
            index+=item
    return targets    

#-------------------------------------------------------------------------------------------

def one_hot_encoding5(T):    
    types = np.unique(T)
    targets = np.zeros((len(T),types.size))
    moving = np.delete(np.hstack((np.eye(1),np.zeros((1,types.size)))),-1)
    freq={elem: list(T).count(elem) for elem in types}
    index=0
    for pos, item in enumerate(types):
            targets[index:index+freq[item]]=np.roll(moving,pos)
            index+=freq[item]
    return targets      

#-------------------------------------------------------------------------------------------

def one_hot_encoding6(T):    
    types = np.unique(T)
    targets = np.zeros((len(T),types.size))
    moving = np.delete(np.hstack((np.eye(1),np.zeros((1,types.size)))),-1)
    freq=list({elem: list(T).count(elem) for elem in types}.values())
    index=0
    for pos in range(len(types)):
            targets[index:index+freq[pos]]=np.roll(moving,pos)
            index=np.cumsum(freq)[pos]
    return targets    

#-------------------------------------------------------------------------------------------

def one_hot_encoding7(T):    
    types = np.unique(T)
    targets = np.zeros((len(T),types.size))
    moving = np.delete(np.hstack((np.eye(1),np.zeros((1,types.size)))),-1)
    freq={elem: list(T).count(elem) for elem in types}
    index=0
    for pos, item in enumerate(types):
            targets[index:index+freq[item]]=np.roll(moving,pos)
            index=np.cumsum(list(freq.values()))[pos]
    return targets

#-------------------------------------------------------------------------------------------

def one_hot_encoding8(T):
    types = np.unique(T)
    targets = np.array([]).reshape(0,types.size)
    for pos,item in enumerate(types):
        a = np.zeros_like(types,dtype=int)
        a[pos]=1
        block = np.tile(a,((np.array(T)==item).sum(),1))
        targets=np.vstack((targets,block))
    return targets

#-------------------------------------------------------------------------------------------

def one_hot_encoding9(T):
    types = np.unique(T)
    targets = np.eye(0).reshape(0,types.size)
    for pos,item in enumerate(types):
        block = np.tile(np.eye(len(types))[pos],((np.array(T)==item).sum(),1))
        targets=np.vstack((targets,block))
    return targets

#-------------------------------------------------------------------------------------------

def one_hot_encoding10(T):
    init,types = 0,np.unique(T)
    targets = np.zeros((len(T),types.size))
    w = np.ones_like(targets)
    for k,elem in enumerate(types):
        freq = list(T).count(elem)
        condlist = [w[init:init+freq]==1]
        choicelist=[np.eye(len(types))[k]]
        targets[init:init+freq]=np.select(condlist,choicelist)
        init+=freq
    return targets

#-------------------------------------------------------------------------------------------

def one_hot_encoding11(T):                                          
    init = 0
    types = np.unique(T)
    row = np.delete(np.insert(np.zeros_like(types,dtype=int),0,1),-1)
    targets = np.eye(0).reshape(0,types.size)
    array_ones = np.ones((len(T),types.size))
    for k,elem in enumerate(types):
        freq = list(T).count(elem)
        condlist = [array_ones[init:init+freq]==1]
        choicelist=[np.roll(row,k)]
        targets = np.vstack((targets,np.select(condlist,choicelist)))
        init+=freq
    return targets

#-------------------------------------------------------------------------------------------

def one_hot_encoding12(T):                               
    init = 0
    types = np.unique(T)
    targets = np.zeros((len(T),types.size))
    row = np.delete(np.insert(np.zeros_like(types,dtype=int),0,1),-1)
    array_ones = np.ones((len(T),types.size))
    for k,elem in enumerate(types):
        freq = list(T).count(elem)
        condlist = [array_ones[init:init+freq]==1]
        choicelist=[np.roll(row,k)]
        targets[init:init+freq]=np.select(condlist,choicelist)
        init+=freq
    return targets



#let's try!

print(one_hot_encoding(a).astype(int))


