import math

class Grafo:
    def init (self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range(0)]

    def es_en_vertices(self, v):
        if self.vertices.count(v)==0:
            return False
        return True
    
    def agrega_vertices(self, v):
        if self.es_en_vertices(v):
            return False
        self.vertices.append(v):

        filas=columnas=len(self.matriz)
        matriz_aux = [[None]*(filas+1) for i in range(columnas+1)]

        for f in range(filas):
            for c in range(columnas):
                 matriz_aux[f][c] = self.matriz[f][c]
        self.matriz = matriz_auxiliar
        return True
    

    def agregar_arista(self , inicio, fin, valor,dirigida):
        if not(self.es_en_vertices(inicioI)) or not(sel.es_en_vertices(fin)):
            return False
        self.matriz[sel.vertices.index(inicio)][sel.es_en_vertices(fin)] = valor

        if not dirigida:
            self.matriz[self.vertices.index(fin)][self.vertices(inicio)] = valor
    
    def imp_matriz(self,m):
        cadena = "\n"

        for c in range(len(m)):
            cadena += "\t" + str(self.vertices[c])
        
        cadena += "\n" + ('  ' * len(m))

        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + '  |'

            for c in range(len(m)):
                if f==c and (m[f][c] is None or m[c][f]== 0):
                    cadena+="\t" + "\\"
                else:
                    if m[f][c] is None:
                        cadena += "\t"+ "X"
                    elif math.isinf(m[f][c]):
                        cadena += "\t" + "-"
                    else:
                        cadena += "\t" + str(m[f][c])

        cadena += "\n"
        print(cadena) 



if __name__ == '__main__':
    g = Grafo()

    Cantidad_vertices = int(input("Introduce la cantidad de vertices"))
    for cv in Cantidad_vertices:
        g.agrega_vertices(cv)
        
