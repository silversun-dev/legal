# Marcas de Liquid Sun

Los logos de las diez marcas de la casa, en vector. **La hoja de marca con todo
junto está en [`index.html`](index.html)**: ábrelo en el navegador.

Igual que los textos legales, esto se genera. Se edita `gen_logos.py` y se
ejecuta:

```bash
python3 gen_logos.py
```

Sin dependencias: sólo Python 3 estándar.

## Qué sale

| Ruta | Qué es | Dónde va |
|---|---|---|
| `icono/<app>.svg` | Icono cuadrado con fondo, esquinas de radio 114 | Play Console, launcher, favicon |
| `marca/<app>.svg` | Símbolo suelto, sin fondo, a dos tintas | Web, documentos, cabeceras |
| `index.html` | La hoja de marca | Para mirar y para enseñar |

`hoja-artifact.html` es el mismo contenido sin envoltorio, para publicarlo como
Artifact. No se versiona.

## El sistema

Todas comparten rejilla: lienzo de 512, símbolo dentro de un área segura de 320,
trazo de 30 con extremos redondeados. Y todas llevan un disco o un arco — es lo
que las hace familia sin obligarlas a parecerse.

El oro y el naranja de Liquid Sun no se repiten en ninguna app: una app que use
el color de la casa compite con su propia marca. El azul `#2F3A8F` sí se repite,
porque ya venía de las páginas legales y es el color del editor, no de un
producto.

## Añadir una marca

Dos sitios, los dos en `gen_logos.py`:

1. El símbolo en `SIMBOLOS`, con los tokens `@P@` (prefijo de los `id`), `@INK@`
   y `@ACC@` en vez de colores literales. El prefijo importa: dos SVG en la
   misma página con el mismo `id` de gradiente se pisan, y el segundo sale con
   los colores del primero.
2. La entrada en `MARCAS`, con los colores del icono (`bg`, `ink`, `acc`) y los
   del símbolo suelto (`plano_ink`, `plano_acc`), que son distintos porque uno
   va sobre fondo oscuro y el otro sobre papel.

Comprueba el resultado a 24 px antes de darlo por bueno. Casi todo se cae ahí.

## PNG para las tiendas

Play Store pide un PNG de 512×512 sin transparencia:

```bash
rsvg-convert -w 512 -h 512 icono/sol.svg -o sol-512.png
```

El vector es el original. Los PNG se regeneran cuando hacen falta y no se
versionan.

## Faltan dos

`spam` y `e-SIM` se han dejado fuera a propósito: puede que su marca se esté
resolviendo por otro lado, y dos identidades para la misma app es peor que
ninguna.
