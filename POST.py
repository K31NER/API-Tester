import time
import requests
from utils import *
from concurrent.futures import ThreadPoolExecutor, as_completed


URL_BASE = "http://127.0.0.1:8000/"

def metodo_post(url_base: str, ruta: str,
                header: bool = False,header_content: dict = None, 
                body:bool=False,body_content:dict = None) -> dict:
    
    """Realizar peticiones post. Por defendo la manda sin header """
    try:
        inicio = time.perf_counter() # <- Inicar conteo

        # Validamos los datos que recibe el metodo
        if header and header_content:
            solicitud = requests.post(f"{url_base}{ruta}", headers=header_content)
        elif body and body_content:
            solicitud = requests.post(f"{url_base}{ruta}",json=body_content)
        elif header and body and header_content and body_content:
            solicitud = requests.post(f"{url_base}{ruta}",
                                    json=body_content, headers= header_content)
        else:
            solicitud = requests.post(f"{url_base}{ruta}")
        
            

        final = time.perf_counter() - inicio # <- Finalizar conteo

        # Validar estado de respuesta
        if solicitud.status_code != 200:
            print(f"Error en la solicitud: Código de estado {solicitud.status_code}")
            return {
                "status": solicitud.status_code,
                "descripcion": f"Error en la solicitud: Código de estado {solicitud.status_code}"
            }
        
        # Mostrar resultados
        print("Solicitud completada con éxito")
        return {
            "status": solicitud.status_code,
            "time": round(final, 5),
            "data": solicitud.json()  
        }

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return {
            "status": 500,
            "descripcion": str(e)
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": 500,
            "descripcion": str(e)
        }
    

def simular_usuarios_post(peticiones:int,url_base: str,ruta: str, 
                        header: bool = False,header_content: dict = None,
                        body:bool = False, body_content: dict = None):
    
    """ Simular X usuarios para hacer peticiones """
    
    # Inicamos los X hilos 
    with ThreadPoolExecutor(max_workers=peticiones) as executor:
        
        # Creamos todas las X tareas 
        tareas = [
            executor.submit(metodo_post,url_base,ruta,
                            header,header_content,
                            body,body_content)
            for i in range(peticiones)
        ]
        
        # Guardamos los resultados
        resultados = [ future.result() for future in as_completed(tareas)]
        
    return resultados
    
if __name__ == "__main__":
    
    # Simulamos la data 
    data = {"Nombre": "Keiner",
            "Edad": 19,
            "Cargo": "Ingeniero en sistemas"}
    
    # Hacer peticiones
    simulacion = simular_usuarios_post(1000,URL_BASE,"user_create",body=True, body_content=data)
    
    # Recopilar datos
    codigos_estado = [i["status"] for i in simulacion if "status" in i]
    latencias = [t["time"] for t in simulacion if "time" in t]
    #contenido = [c["data"] for c in simulacion]
    
    # Graficar y mostrar
    stast = estadisticas(latencias)
    print("\n------------------------- Estadisticas --------------------------\n")
    for k,v in stast.items():
        print(f"📍 {k.ljust(22)}: {v:.5f}s")
    graficar_resultados(latencias,codigos_estado)

