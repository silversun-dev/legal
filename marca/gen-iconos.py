# -*- coding: utf-8 -*-
"""
Iconos de la ficha de Google Play: un maestro SVG y un PNG 512x512 por app.

Todos comparten la paleta de marca —el cielo y el sol— y se distinguen sólo por
el motivo, que vive en `marca.py`. Ninguno lleva texto: Play ya escribe el
nombre debajo del icono, y a 48 px, que es como se ven en la lista de
resultados, un texto dentro del icono no se lee.

El motivo se queda dentro del 66% central del lienzo. El fondo, en cambio, es a
sangre y sin esquinas redondeadas: Play redondea el icono por su cuenta, y
redondearlo aquí también deja un borde doble.

    python3 gen-iconos.py
"""

import io
import os

from marca import LADO, MOTIVOS, NOMBRES, SEGURO, png, svg_completo, svg_motivo


def revisar_zona_segura(slug):
    """El motivo, sin fondo, debe caber en el 66% central."""
    caja = png(svg_motivo(slug)).getbbox()
    margen = LADO * (1 - SEGURO) / 2
    holgado = (
        caja[0] >= margen and caja[1] >= margen
        and caja[2] <= LADO - margen and caja[3] <= LADO - margen
    )
    return caja, holgado


if __name__ == "__main__":
    aqui = os.path.dirname(os.path.abspath(__file__))
    margen = LADO * (1 - SEGURO) / 2
    print("zona segura: %d-%d en ambos ejes\n" % (margen, LADO - margen))

    fallos = 0
    for slug in sorted(MOTIVOS):
        fuente = svg_completo(slug)
        with io.open(os.path.join(aqui, "%s-512.svg" % slug), "w", encoding="utf-8") as f:
            f.write(fuente)

        # Play rechaza los iconos con transparencia.
        png(fuente).convert("RGB").save(
            os.path.join(aqui, "%s-512.png" % slug), "PNG", optimize=True)

        caja, holgado = revisar_zona_segura(slug)
        if not holgado:
            fallos += 1
        print("%-11s %-24s motivo en %s  %s" % (
            slug, NOMBRES[slug], caja, "ok" if holgado else "SE SALE"))

    if fallos:
        raise SystemExit("\n%d icono(s) con el motivo fuera de la zona segura." % fallos)
    print("\n%d iconos generados." % len(MOTIVOS))
