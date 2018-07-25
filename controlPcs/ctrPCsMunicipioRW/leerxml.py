from xml.dom import minidom
    

def obtenerDataPC(self,nombreArchivo):
    xmlstock = minidom.parse("/home/adrian/djangoProjects/adminServTec/controlPcs" + nombreArchivo)
    mainsections = xmlstock.getElementsByTagName("mainsection")
    
    dataPc={}
    entradasDict={}

    for mainsection in mainsections: 
        sections=mainsection.getElementsByTagName("section")
        for section in sections:   
            tituloSection=section.attributes['title'].value
           
            entradas=section.getElementsByTagName("entry")

            lenEntradasParcial=len(entradas)  
            i=0    
            for entrada in entradas:
                   
                if 'title' in entrada.attributes:    
                    tituloEntrada=entrada.attributes['title'].value
                 
                if 'value' in entrada.attributes:
                    valor=entrada.attributes['value'].value 

                entradasDict[tituloEntrada]=valor

                i+=1
                if(lenEntradasParcial==i):
                    dataPc[tituloSection]=entradasDict
                    entradasDict={}
    return dataPc