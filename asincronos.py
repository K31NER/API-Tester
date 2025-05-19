import time
import httpx
import asyncio

async def metodo_post_async(url_base: str, ruta: str,
                header: bool = False,header_content: dict = None, 
                body:bool=False,body_content:dict = None) -> dict:
    
    """ Realiza solicitudes asincronas a los endpoints """
    try:
        
        inicio = time.perf_counter() # Inicia contador
        
        # Definimos el cliente asincrono
        async with httpx.AsyncClient(timeout=120) as cliente:
            # Validmos si esta bien definida la url base
            if not url_base.endswith("/"):
                url_base += "/"
            # Normalizamos la ruta para evitar errores
            ruta = ruta.lstrip("/")
            
            # Construimos la ruta objetivo
            url = f"{url_base}{ruta}"
            
            # Validamos los datos que ricibe el metodo
            request_args = {} # Dicionario vacio para guardar parametros extras
            
            if header and header_content: # Validar header
                request_args["headers"] = header_content
            if body and body_content: # Validar el body
                request_args["json"] = body_content
                
            # Pasamos la url y desempaquetamos las validaciones
            print("Realizando peticion")
            response = await cliente.post(url,**request_args) 
            
        duracion = time.perf_counter() - inicio # Finaliza
        
        # Validamos respuesta del servidor
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return {
                "status": response.status_code,
                "descripcion": f"Error en la solicitud: {response.status_code}"
            }
        
        # Si fue exitosa mandamos mensaje
        print("Solicitud completada con éxito")
        return {
            "status": response.status_code,
            "time": round(duracion, 5),
            "data": len(response.json().get("data",[]))
        }

    except httpx.ReadError as e:
        print(f"Error: {e}")
        return{
            "status":500,
            "Descripcion":str(e)
        }
        
async def simular_usuarios_post_async(peticiones: int, url_base: str, ruta: str,
                                    header: bool = False,header_content: dict=None,
                                    body: bool = False, body_content: dict = None):
    
    """ Simular multiples peticiones de manera asincrona """
    
    # Definimos una lista de tareas con el numero X de peticiones
    tareas = [
        metodo_post_async(url_base,ruta,header,header_content,body,body_content)
        for i in range(peticiones)
    ]
    
    # Esperamos la respuesta
    resultado = await asyncio.gather(*tareas, return_exceptions=True)
    return resultado

