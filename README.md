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
| GymTonic | https://silversun-dev.github.io/legal/gymtonic.html |

> **Estas URLs planas son las dadas de alta en Play Console.** Las rutas con
> carpeta (`/legal/grabadora/`) no existen y nunca se han publicado: el README
> las anunciaba por error. El motivo de que las páginas sean planas es que subir
> el ZIP desde el navegador de GitHub aplasta las carpetas, así que la ruta con
> carpeta se rompería en cuanto alguien editase desde la web.
>
> Queda escrito aquí para no volver a abrir la duda en cada revisión.

## Cómo se editan

Las páginas se generan con `gen.py`, que mantiene un único diseño y una única
sección de derechos para todas. Para cambiar un texto, edítalo en `gen.py` y
ejecuta:

```bash
python3 gen.py
```

Para añadir una app nueva, añade una entrada al array `APPS` con su `slug`,
`nombre`, `pkg`, `claim` y `cuerpo`. El fichero `<slug>.html` y el enlace del índice
se crean solos.

Cada app puede llevar además una clave `fecha` con su propia fecha de última
actualización; si no la lleva, usa la global `FECHA`. Así, al tocar el texto de una
sola app no se mueve la fecha de las demás. `FECHA_IDX` es la del índice.

Responsable del tratamiento: Juan Antonio Hernández López · liquidsun.dev@gmail.com
