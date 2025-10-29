#  Despliegue del Proyecto Pokeneas en Docker Swarm (AWS)

##  Arquitectura del Clúster

El servicio fue desplegado utilizando **Docker Swarm** sobre instancias **EC2** en AWS.  
Se configuró un **clúster** compuesto por:

-  **1 nodo manager:** encargado de la orquestación del Swarm.  
-  **2 nodos worker:** ejecutan las tareas distribuidas.  
- **10 réplicas** del servicio `pokeneas`, publicada en **Docker Hub**.

---

##  Evidencia de Réplicas (Contenedores)

Pantallazo del comando:
```bash
sudo docker service ps pokeneas
```
<img width="1716" height="395" alt="image" src="https://github.com/user-attachments/assets/bd7c8d7d-49fc-4d90-95fe-f5893091beeb" />

<img width="1715" height="770" alt="image" src="https://github.com/user-attachments/assets/47987f3f-74ab-4656-a527-32e7273d6896" />

## Acceso a la Aplicación

La aplicación fue desplegada exitosamente y responde mediante balanceo de carga a través del puerto **80**.

**Rutas de prueba:**
- [http://34.202.161.61/filosofia](http://34.202.161.61/filosofia)
- [http://34.202.161.61/info](http://34.202.161.61/info)

> Estas rutas permiten verificar el correcto funcionamiento del servicio y el balanceo entre los contenedores desplegados en el clúster Docker Swarm.


