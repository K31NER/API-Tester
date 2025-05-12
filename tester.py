import time
import requests
from utils import *
from concurrent.futures import ThreadPoolExecutor, as_completed


URL_BASE = "http://127.0.0.1:80/"

def metodo_get(url_base: str, ruta: str, header: bool = False,
                header_content: dict = None) -> dict:
    
    """Realizar peticiones GET. Por defendo la manda sin header """
    try:
        inicio = time.perf_counter() # <- Inicar conteo

        if header and header_content:
            solicitud = requests.get(f"{url_base}{ruta}", headers=header_content)
        else:
            solicitud = requests.get(f"{url_base}{ruta}")

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
            # "data": solicitud.json()  # Descomenta esta línea si necesitas los datos de la respuesta
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
    

def simular_usuarios(peticiones:int,url_base: str, 
                    ruta: str, header: bool = False,
                    header_content: dict = None):
    
    """ Simular X usuarios para hacer peticiones """
    
    # Inicamos los X hilos 
    with ThreadPoolExecutor(max_workers=peticiones) as executor:
        
        # Creamos todas las X tareas 
        tareas = [
            executor.submit(metodo_get,url_base,ruta,header,header_content)
            for i in range(peticiones)
        ]
        
        # Guardamos los resultados
        resultados = [ future.result() for future in as_completed(tareas)]
        
    return resultados
    

    
if __name__ == "__main__":
    simulacion = simular_usuarios(10,URL_BASE,"users")
    codigos_estado = [i["status"] for i in simulacion if "status" in i]
    latencias = [t["time"] for t in simulacion if "time" in t]
    stast = estadisticas(latencias)
    print("\n------------------------- Estadisticas --------------------------\n")
    for k,v in stast.items():
        print(f"📍 {k.ljust(22)}: {v:.5f}s")
    graficar_resultados(latencias,codigos_estado)

