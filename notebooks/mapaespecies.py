import os
import matplotlib.pyplot as plt
import seaborn as sns

GRID_DIM = (10,10)	



def buscaRegistros( nomeCamera ):
    # seu código aqui
    rootDir = "./ctraps"
    camDir = rootDir+"/"+nomeCamera
    spp=[]
    for file in os.listdir(camDir):
        fpath = camDir+"/"+file
        f = open(fpath,'r')
        sp = f.readline()
        f.close()
        
        spp = spp + [sp]
    return spp

def criaGrid( dim ):
    n_rows = dim[0]
    n_cols = dim[1]
    
    m=[]
    for i in range(n_rows):
        m += [[]]
        for j in range(n_cols):
            m[i] +=[None]
    return m

def pegaNomeCamera( numCamera ):
    # seu código aqui

    if numCamera >=100:
        nome="cam"+str(numCamera)
    elif numCamera>=10:
        nome="cam0"+str(numCamera)
    else:
        nome="cam00"+str(numCamera)
    return nome

def preencheGrid( g, dim ):
    # seu código aqui
    
    num_rows = dim[0] 
    num_cols = dim[1]
    
    ctr=1
    for i in range(num_rows):
        for j in range(num_cols):
            g[i][j] = buscaRegistros(pegaNomeCamera(ctr))
            ctr+=1
    return

def ocorrenciaEspecie( sp, grid, dim ):
    # seu código aqui
    n_rows = dim[0]
    n_cols = dim[1]
    
    addrs = []
    for i in range(n_rows):
        for j in range(n_cols):
            if sp in grid[i][j]:
                addrs += [(i,j)]
    celulas = addrs
    return celulas

def criaMapa( sp, g, dim ):
    # seu código aqui
    m = criaGrid(dim)
    
    n_rows = dim[0]
    n_cols = dim[1]
    
    for i in range(n_rows):
        for j in range(n_cols):
            if sp in g[i][j]:
                m[i][j]=1
            else:
                m[i][j]=0
    
    return m

def listaEspecies(g,dim):
    # seu código aqui
    spList=[]
    
    n_rows=10
    n_cols=10
    
    # constrói lista de espécies
    for i in range(n_rows):
        for j in range(n_cols):
            registros = g[i][j]
            for sp in registros:
                if sp not in spList:
                    spList += [sp]
    
    # constrói o dicionário com contagens zeradas
    d = {}
    for sp in spList:
        d[sp]=0
    
    for i in range(n_rows):
        for j in range(n_cols):
            registros = g[i][j]
            for sp in registros:
                d[sp] += 1
                
    return d



# Esta parte será executada
g = criaGrid(GRID_DIM)
preencheGrid(g,GRID_DIM)

print("===================================")
print("Bem vindo ao Mapa de Espécies v0.1!")
print("===================================")
print("")

while(True):
    sp = input("Insira o nome da espécie. Para sair digite 'q'.\n")
    if sp=='q':
        print("")
        print("---------------------------------")
        print("Obrigado por usar nosso programa!")
        print("---------------------------------")
        break
    else: 
        m = criaMapa(sp,g,GRID_DIM)
        sns.heatmap(m,cbar=False,linewidths=1,square=True)
        plt.show()


