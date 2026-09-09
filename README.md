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
| Grabadora Forense | https://silversun-dev.github.io/legal/grabadora/ |
| Cuentakilómetros | https://silversun-dev.github.io/legal/cuentakm/ |
| PingCoins | https://silversun-dev.github.io/legal/pingcoins/ |
| Sol · ventana de paseo | https://silversun-dev.github.io/legal/sol/ |

## Cómo se editan

Las páginas se generan con `gen.py`, que mantiene un único diseño y una única
sección de derechos para todas. Para cambiar un texto, edítalo en `gen.py` y
ejecuta:

```bash
python3 gen.py
```

Para añadir una app nueva, añade una entrada al array `APPS` con su `slug`,
`nombre`, `pkg`, `claim` y `cuerpo`. La carpeta y el enlace del índice se crean solos.

Responsable del tratamiento: Juan Antonio Hernández López · liquidsun.dev@gmail.com
