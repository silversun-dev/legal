# -*- coding: utf-8 -*-
"""
Iconos de tienda de Liquid Sun: un maestro SVG y un PNG 512x512 por app.

Todos comparten la misma paleta —el cielo y el sol de la marca— y se distinguen
sólo por el motivo. Ninguno lleva texto: Google Play ya escribe el nombre de la
app debajo del icono, y a 48 px de la lista de resultados un texto dentro del
icono no se lee.

El motivo se queda dentro del 66% central del lienzo (de 87 a 425 de 512). El
fondo, en cambio, es a sangre y sin esquinas redondeadas: Play redondea el icono
por su cuenta, y redondearlo aquí también deja un borde doble.

    python3 gen-iconos.py

Necesita cairosvg y pillow:

    pip install cairosvg pillow
"""

import io
import os

import cairosvg
from PIL import Image

LADO = 512
SEGURO = 0.66  # fracción central que Play y los iconos adaptativos respetan

CIELO_ALTO, CIELO_BAJO = "#1b2330", "#4a2a12"
SOL_CLARO, SOL_OSCURO = "#ffd08a", "#ff7a45"
AMBAR = "#ffb043"
TINTA = "#e9eff6"

PLANTILLA = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{cielo_alto}"/><stop offset="1" stop-color="{cielo_bajo}"/>
    </linearGradient>
    <linearGradient id="sol" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{sol_claro}"/><stop offset="1" stop-color="{sol_oscuro}"/>
    </linearGradient>
  </defs>
{fondo}
  <g id="motivo">
{motivo}
  </g>
</svg>
"""

FONDO = '  <rect width="512" height="512" fill="url(#cielo)"/>'

# --- Motivos -----------------------------------------------------------------
# Coordenadas pensadas para caber en [87, 425]. gen-iconos.py lo comprueba.

MOTIVOS = {
    "grabadora": """
    <!-- Micrófono: cápsula, horquilla, pie. Grabar es el gesto de la app. -->
    <rect x="214" y="112" width="84" height="168" rx="42" fill="url(#sol)"/>
    <path d="M168 252 a88 88 0 0 0 176 0" fill="none" stroke="{ambar}"
          stroke-width="18" stroke-linecap="round"/>
    <rect x="246" y="332" width="20" height="52" rx="10" fill="{ambar}"/>
    <rect x="192" y="380" width="128" height="20" rx="10" fill="{ambar}"/>
    <!-- Huella de integridad: tres marcas dentro de la cápsula -->
    <rect x="236" y="150" width="40" height="10" rx="5" fill="{cielo_alto}" opacity=".38"/>
    <rect x="236" y="176" width="40" height="10" rx="5" fill="{cielo_alto}" opacity=".38"/>
    <rect x="236" y="202" width="40" height="10" rx="5" fill="{cielo_alto}" opacity=".38"/>
""",
    "cuentakm": """
    <!-- Cuentakilómetros: arco de la aguja, tramo recorrido y horizonte. -->
    <path d="M116 330 a140 140 0 0 1 280 0" fill="none" stroke="{tinta}"
          stroke-width="26" stroke-linecap="round" opacity=".22"/>
    <path d="M116 330 A140 140 0 0 1 326 209" fill="none" stroke="url(#sol)"
          stroke-width="26" stroke-linecap="round"/>
    <path d="M256 330 L304 247" fill="none" stroke="{ambar}"
          stroke-width="18" stroke-linecap="round"/>
    <circle cx="256" cy="330" r="22" fill="{ambar}"/>
    <rect x="120" y="386" width="272" height="14" rx="7" fill="{ambar}" opacity=".5"/>
""",
    "pingcoins": """
    <!-- Moneda golpeada: el disco y el sonido que sale de él. Las ondas sólo
         salen por un lado, así que el grupo se desplaza para que el centro
         óptico caiga en el del lienzo. -->
    <circle cx="207" cy="256" r="92" fill="url(#sol)"/>
    <circle cx="207" cy="256" r="62" fill="none" stroke="{cielo_alto}"
            stroke-width="11" opacity=".34"/>
    <path d="M319 182 A124 124 0 0 1 319 330" fill="none" stroke="{ambar}"
          stroke-width="16" stroke-linecap="round" opacity=".9"/>
    <path d="M349 148 A166 166 0 0 1 349 364" fill="none" stroke="{ambar}"
          stroke-width="16" stroke-linecap="round" opacity=".5"/>
""",
    "sol": """
    <!-- El recorrido del sol y la ventana de paseo bajo él. -->
    <path d="M110 330 C182 174, 330 174, 402 330" fill="none" stroke="{ambar}"
          stroke-width="16" stroke-linecap="round" opacity=".55"/>
    <circle cx="256" cy="228" r="64" fill="url(#sol)"/>
    <rect x="110" y="330" width="292" height="16" rx="8" fill="{ambar}" opacity=".85"/>
    <path d="M186 412 l28-54 22 17 26-41 24 35 22-24 19 67z" fill="{tinta}" opacity=".38"/>
""",
}

NOMBRES = {
    "grabadora": "Grabadora Forense",
    "cuentakm": "Cuentakilómetros",
    "pingcoins": "PingCoins",
    "sol": "Sol · ventana de paseo",
}

COLORES = dict(
    cielo_alto=CIELO_ALTO, cielo_bajo=CIELO_BAJO,
    sol_claro=SOL_CLARO, sol_oscuro=SOL_OSCURO,
    ambar=AMBAR, tinta=TINTA,
)


def svg(slug, con_fondo=True):
    return PLANTILLA.format(
        fondo=FONDO if con_fondo else "",
        motivo=MOTIVOS[slug].format(**COLORES),
        **COLORES
    )


def png(fuente):
    datos = cairosvg.svg2png(
        bytestring=fuente.encode("utf-8"),
        output_width=LADO, output_height=LADO,
    )
    return Image.open(io.BytesIO(datos))


def revisar_zona_segura(slug):
    """El motivo, sin fondo, debe caber en el 66% central."""
    caja = png(svg(slug, con_fondo=False)).getbbox()
    margen = LADO * (1 - SEGURO) / 2
    limites = (margen, margen, LADO - margen, LADO - margen)
    holgado = (
        caja[0] >= limites[0] and caja[1] >= limites[1]
        and caja[2] <= limites[2] and caja[3] <= limites[3]
    )
    return caja, limites, holgado


if __name__ == "__main__":
    aqui = os.path.dirname(os.path.abspath(__file__))
    margen = LADO * (1 - SEGURO) / 2
    print("zona segura: %d-%d en ambos ejes\n" % (margen, LADO - margen))

    fallos = 0
    for slug in sorted(MOTIVOS):
        fuente = svg(slug)
        with io.open(os.path.join(aqui, "%s-512.svg" % slug), "w", encoding="utf-8") as f:
            f.write(fuente)

        imagen = png(fuente).convert("RGB")  # Play rechaza iconos con transparencia
        imagen.save(os.path.join(aqui, "%s-512.png" % slug), "PNG", optimize=True)

        caja, _, holgado = revisar_zona_segura(slug)
        if not holgado:
            fallos += 1
        print("%-11s %-24s motivo en %s  %s" % (
            slug, NOMBRES[slug], caja, "ok" if holgado else "SE SALE"))

    if fallos:
        raise SystemExit("\n%d icono(s) con el motivo fuera de la zona segura." % fallos)
    print("\n%d iconos generados." % len(MOTIVOS))
