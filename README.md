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
| PingCoins | https://silversun-dev.github.io/legal/pingcoins.html |
| Sol · ventana de paseo | https://silversun-dev.github.io/legal/sol.html |

## Cómo se editan

Las páginas se generan con `gen.py`, que mantiene un único diseño y una única
sección de derechos para todas. Para cambiar un texto, edítalo en `gen.py` y
ejecuta:

```bash
python3 gen.py
```

Para añadir una app nueva, añade una entrada al array `APPS` con su `slug`,
`nombre`, `pkg`, `claim` y `cuerpo`. La página y el enlace del índice se crean solos.

`gen.py` escribe páginas **planas** (`grabadora.html`, no `grabadora/index.html`)
y sobrescribe las que ya existen: son las rutas dadas de alta en Play Console y
subir un ZIP desde el navegador de GitHub aplasta las carpetas. Después de
ejecutarlo, `git status` debe listar sólo lo que hayas cambiado a propósito; si
aparecen ficheros o carpetas nuevos, el generador y lo publicado se han separado.

Responsable del tratamiento: Juan Antonio Hernández López · liquidsun.dev@gmail.com
