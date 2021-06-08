VISUALIZACION DE RESULTADOS EN TIEMP REAL, ELECCIONES PRESIDENCIALES SEGUNDA VUELTA - AMBITO TODO, PERU 2021

![ONPE RESULTADOS](resultados-onpe.png)

### Requisitos:
- git
- pip3 
- virtualenv 
- python3.6.x 
- requiests

### Requisitos S.O:
- Windows, linux o mac.

### Ejecucion en modo usuario
En windows ejecutar el archivo :
abrir el ejecutable `resultados_segunda_vuelta_onpe.exe`

En linux y mac ejecutar el archivo:
>>  abrir el archivo ejecutable  `resultados_segunda_vuelta_onpe`

### Ejecución en modo desarrollador:

Crear un entorno virtual(opcional)
```
virtualenv -p python3 env_resultados_onpe && source env_resultados_onpe/bin/activate
```
Clonar el proyecto:
```
git@github.com:yachaycode/api-resultados-onpe-2021.git
```
Instalación de dependencias
```
pip install -r install requeriments.txt
```
ejecutar el script

```
python resultados_segunda_vuelta_onpe.py
```

