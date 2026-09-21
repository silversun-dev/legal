# Liquid Sun — textos legales

Este repositorio es **público a propósito** y contiene únicamente las políticas de
privacidad de las aplicaciones publicadas por Liquid Sun. No hay aquí código de
ninguna aplicación: los repositorios de código son privados.

Google Play exige que la política de privacidad de cada app esté accesible en una
URL pública. GitHub Pages sólo sirve repositorios públicos en el plan gratuito, de
ahí que estas páginas vivan separadas del código.

## Páginas

| App | URL |
|---|---|
| Grabadora Forense | https://silversun-dev.github.io/legal/grabadora.html |
| Cuentakilómetros | https://silversun-dev.github.io/legal/cuentakm.html |
| Sun Bell | https://silversun-dev.github.io/legal/sunbell.html |
| Sol · ventana de paseo | https://silversun-dev.github.io/legal/sol.html |

Las páginas son **planas** (`sunbell.html`), no carpetas: estas se suben desde el
navegador y subir una carpeta la aplasta. El README listaba antes URL con carpeta
que no existían.

`pingcoins.html` sigue vivo y sirve el mismo texto que `sunbell.html`: la app cambió
de nombre, pero esa URL puede estar ya dada de alta en Play Console y una política
que deja de responder es motivo de rechazo. Para eso está el campo `alias`.

## Cómo se editan

Las páginas se generan con `gen.py`, que mantiene un único diseño y una única
sección de derechos para todas. Para cambiar un texto, edítalo en `gen.py` y
ejecuta:

```bash
python3 gen.py
```

Para añadir una app nueva, añade una entrada al array `APPS` con su `slug`,
`nombre`, `pkg`, `claim` y `cuerpo`. El archivo y el enlace del índice se crean solos.
Campos opcionales: `fecha` (si no, se usa la global — así cambiar una app no vuelve a
fechar las demás como si también se hubieran revisado) y `alias` (nombres antiguos que
deben seguir sirviendo la misma página).

## Antes de publicar una versión con anuncios

Decir que hay anuncios y no tenerlos es inofensivo; decir que no los hay y tenerlos, no.
Por eso el texto puede ir por delante de la app. El formulario de **Seguridad de los
datos** de Play, en cambio, describe la versión que está publicada *ahora*: se actualiza
el mismo día que sale el APK con anuncios, ni antes ni después. La página primero,
porque es estática y está viva al subirla; el formulario y el APK, juntos.

Responsable del tratamiento: Juan Antonio Hernández López · liquidsun.dev@gmail.com
