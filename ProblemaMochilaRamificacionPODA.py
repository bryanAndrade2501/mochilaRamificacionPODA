n = 5
W = 1100
p = [60,48,14,31,10]
w = [800,600,300,400,200]
rpw = [0.075,0.08,0.0466666667,0.0755,0.05]

#Sirve para almacenar el nodo a evaluar.
class Nodo:
    def __init__(self, nivel, ganancia, peso):
        self.nivel = nivel
        self.ganancia = ganancia
        self.peso = peso
        self.items = []

#Representa la cola de prioridades.
class CP:
    def __init__(self):
        self.cp = []
        self.longitud = 0
    
    def insert(self,nodo):        
        for i in self.cp:
            obtener_beneficio(i)            
        i = 0
        while i < len(self.cp):
            if self.cp[i].beneficio > nodo.beneficio:
                break
            i+=1
        self.cp.insert(i,nodo)
        self.longitud += 1
        
    def remove(self):
        try:
            resultado = self.cp.pop()
            self.longitud -= 1
        except:
            print("No se puede remover, CP está vacío")
        else:
            return resultado
            
    def imprimir_cp(self):
        for i in list(range(len(self.cp))):
            print("cp ",i,"=",self.cp[i].beneficio)
            
#Obtener beneficio de un nodo
def obtener_beneficio(nodo):
    if nodo.peso >= W:
        return 0
    else:
        resultado = nodo.ganancia
        j = nodo.nivel + 1
        peso_total = nodo.peso
        while j <= n-1 and peso_total + w[j] <= W:
            peso_total = peso_total + w[j]
            resultado = resultado + p[j]
            j+=1
        k = j
        if k<=n-1:
            resultado = resultado + (W - peso_total) * rpw[k]
        return resultado

nodos_generados = 0
cola_prioridad = CP()

nodo_raiz = Nodo(-1, 0, 0) # nodo_raiz initialized to be the root with nivel = 0, ganancia = $0, peso = 0
nodos_generados+=1
beneficio_maximo = 0 # beneficio_maximo initialized to $0
nodo_raiz.beneficio = obtener_beneficio(nodo_raiz)


cola_prioridad.insert(nodo_raiz)

while cola_prioridad.longitud != 0:
    nodo_raiz = cola_prioridad.remove() #Remover el que tiene el mejor beneficio   
    
    if nodo_raiz.beneficio > beneficio_maximo: #El nodo es prometedor, vale la pena ramificar?
        #Igualar al nodo hijo que contiene el siguiente elemento.
        nodo_tmp = Nodo(0, 0, 0)
        nodos_generados += 1
        nodo_tmp.nivel = nodo_raiz.nivel + 1
        nodo_tmp.ganancia = nodo_raiz.ganancia + p[nodo_tmp.nivel]
        nodo_tmp.peso = nodo_raiz.peso + w[nodo_tmp.nivel]
        #tomar
        nodo_tmp.items = nodo_raiz.items.copy()
        nodo_tmp.items.append(nodo_tmp.nivel)
        
        if nodo_tmp.peso <= W and nodo_tmp.ganancia>beneficio_maximo:
            beneficio_maximo = nodo_tmp.ganancia
            elementos_escogidos = nodo_tmp.items
        
        nodo_tmp.beneficio = obtener_beneficio(nodo_tmp)
        
        if nodo_tmp.beneficio > beneficio_maximo:
            cola_prioridad.insert(nodo_tmp)
        
        nodo_aux = Nodo(nodo_tmp.nivel, nodo_raiz.ganancia, nodo_raiz.peso)
        nodos_generados+=1
        nodo_aux.beneficio = obtener_beneficio(nodo_aux)
        nodo_aux.items = nodo_raiz.items.copy()
        
        if nodo_aux.beneficio > beneficio_maximo:
            cola_prioridad.insert(nodo_aux)
            
#Mostrar resultados
print("Beneficio Máximo = ",beneficio_maximo," nodos generados: ",nodos_generados)
print("Items a tomar: ",elementos_escogidos)
        
        



