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
`gen-iconos.py`; la paleta es común y está arriba del todo.

## Lo que estos iconos NO son

Son los iconos de la **ficha de Play**. El icono del lanzador que se ve en el
teléfono es otro recurso, dentro de cada repositorio de app
(`res/mipmap-*/ic_launcher*`). Cuentakilómetros y PingCoins todavía llevan ahí
el icono por defecto de Capacitor.
