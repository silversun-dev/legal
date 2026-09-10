# Marca — iconos de tienda

Los cuatro iconos de 512×512 que pide Google Play, uno por app, generados desde
un mismo script para que se lean como una familia.

| App | Motivo | Fichero |
|---|---|---|
| Grabadora Forense | Micrófono con marcas de integridad | `grabadora-512.png` |
| Cuentakilómetros | Aguja sobre el tramo recorrido | `cuentakm-512.png` |
| PingCoins | Moneda y el sonido que sale de ella | `pingcoins-512.png` |
| Sol · ventana de paseo | Recorrido del sol sobre el horizonte | `sol-512.png` |

## Reglas que respetan

- **Sin texto.** Play escribe el nombre debajo del icono; a 48 px, que es como
  se ve en la lista de resultados, un texto dentro del icono no se lee.
- **Motivo dentro del 66% central.** El script lo comprueba midiendo la caja
  del motivo sin fondo y falla si alguno se sale.
- **Fondo a sangre y sin esquinas redondeadas.** Play redondea por su cuenta;
  redondear aquí también deja un borde doble.
- **Sin canal alfa.** Play rechaza los PNG con transparencia, así que el script
  convierte a RGB antes de guardar.

## Regenerar

```bash
pip install cairosvg pillow
python3 gen-iconos.py
```

Escribe el maestro `.svg` y el `.png` de cada app y verifica la zona segura.
Para cambiar un icono, edita su motivo en el diccionario `MOTIVOS` de
`marca.py`, que es de donde tiran los dos generadores; la paleta está en ese
mismo fichero, arriba del todo.

## El icono del lanzador

El de la ficha de Play y el que se ve en el teléfono son recursos distintos.
`gen-lanzador.py` produce el segundo desde el mismo motivo, y lo escribe
directamente en el `res/` de la app:

```bash
python3 gen-lanzador.py cuentakm  ../../gasolineras/android/app/src/main/res
python3 gen-lanzador.py pingcoins ../../ping-coin/android/app/src/main/res
```

Genera el fondo vectorial con el degradado, la capa de primer plano, la capa
monocroma de los iconos temáticos de Android 13, los PNG clásicos para Android
7.0 y 7.1, y el XML del icono adaptativo.

Un icono adaptativo es un lienzo de 108 dp del que cada lanzador recorta la
máscara que le da la gana; lo único garantizado es el **círculo** central de
66 dp, no el cuadrado del 66% que vale para Play. El generador mide el píxel
opaco más lejano del centro de cada motivo, calcula la reducción que necesita el
que peor cabe y se la aplica a los cuatro por igual, para que no acaben de
tamaños distintos.

Grabadora Forense no está en esa lista: tiene su propio icono de lanzador
vectorial, dibujado a mano y con capa monocroma, en su repositorio.
