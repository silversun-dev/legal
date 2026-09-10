# -*- coding: utf-8 -*-
"""
Iconos de lanzador (los que se ven en el teléfono) desde los mismos maestros
que los de tienda.

    python3 gen-lanzador.py cuentakm  /home/user/gasolineras/android/app/src/main/res
    python3 gen-lanzador.py pingcoins /home/user/ping-coin/android/app/src/main/res

Un icono adaptativo es un lienzo de 108 dp del que el lanzador recorta una
máscara —círculo, cuadrado redondeado, gota— que él elige. Lo único garantizado
es el círculo central de 66 dp. Los motivos de gen-iconos.py están pensados para
el cuadrado central del 66%, que es lo que pide la ficha de Play; sus esquinas
se saldrían del círculo, así que aquí se reducen.

La reducción se mide, no se estima: para cada motivo se busca el píxel opaco más
lejano del centro y se calcula cuánto hay que encogerlo para que quepa. Se aplica
a los cuatro la misma reducción, la del peor, para que sigan viéndose del mismo
tamaño unos junto a otros.

Genera:
  drawable/ic_launcher_background.xml   fondo vectorial con el degradado del cielo
  mipmap-*/ic_launcher_foreground.png   motivo sobre transparente (108 dp)
  mipmap-*/ic_launcher_monochrome.png   silueta para los iconos temáticos (Android 13+)
  mipmap-*/ic_launcher.png              icono clásico, para Android 7.0 y 7.1
  mipmap-*/ic_launcher_round.png        idem, con máscara circular
  mipmap-anydpi-v26/ic_launcher*.xml    el icono adaptativo
"""

import io
import os
import sys

from PIL import Image, ImageDraw


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from marca import MOTIVOS, COLORES, LADO, png, svg_motivo, svg_completo  # noqa: E402

# El círculo garantizado de un icono adaptativo es de 66 dp sobre 108: el 61%.
SEGURO_ADAPTATIVO = 66.0 / 108.0

# Densidades: (carpeta, lado del icono clásico, lado del lienzo adaptativo)
DENSIDADES = [
    ("mdpi", 48, 108),
    ("hdpi", 72, 162),
    ("xhdpi", 96, 216),
    ("xxhdpi", 144, 324),
    ("xxxhdpi", 192, 432),
]

FONDO_VECTOR = """<vector xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:aapt="http://schemas.android.com/aapt"
    android:width="108dp" android:height="108dp"
    android:viewportWidth="108" android:viewportHeight="108">
    <path android:pathData="M0,0h108v108h-108z">
        <aapt:attr name="android:fillColor">
            <gradient android:type="linear"
                android:startX="54" android:startY="0"
                android:endX="54" android:endY="108">
                <item android:offset="0" android:color="%(cielo_alto)s"/>
                <item android:offset="1" android:color="%(cielo_bajo)s"/>
            </gradient>
        </aapt:attr>
    </path>
</vector>
"""

ADAPTATIVO = """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
    <monochrome android:drawable="@mipmap/ic_launcher_monochrome"/>
</adaptive-icon>
"""


def radio_maximo(slug):
    """Distancia del centro al píxel opaco más lejano del motivo, en el lienzo de 512."""
    alfa = png(svg_motivo(slug)).split()[-1]
    centro = LADO / 2.0
    peor = 0.0
    pixeles = alfa.load()
    for y in range(LADO):
        for x in range(LADO):
            if pixeles[x, y] > 8:
                d = ((x + 0.5 - centro) ** 2 + (y + 0.5 - centro) ** 2) ** 0.5
                if d > peor:
                    peor = d
    return peor


def escala_comun():
    """La reducción del motivo que peor cabe, aplicada a todos."""
    seguro = LADO * SEGURO_ADAPTATIVO / 2.0
    return min(seguro / radio_maximo(s) for s in MOTIVOS)


def con_escala(fuente, factor):
    """Encoge el grupo del motivo alrededor del centro del lienzo."""
    c = LADO / 2.0
    return fuente.replace(
        '<g id="motivo">',
        '<g id="motivo" transform="translate(%g %g) scale(%.4f) translate(%g %g)">'
        % (c, c, factor, -c, -c),
    )


def mascara(lado, radio):
    m = Image.new("L", (lado, lado), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, lado - 1, lado - 1], radius=radio, fill=255)
    return m


def escribir(slug, res, factor):
    fg = con_escala(svg_motivo(slug), factor)
    completo = con_escala(svg_completo(slug), factor)

    # Icono clásico (API 24-25): lo que el usuario vería a través de la máscara
    # de un icono adaptativo, es decir el lienzo recortado a su zona visible.
    recorte = int(round(LADO * 72.0 / 108.0))
    borde = (LADO - recorte) // 2
    visible = png(completo).convert("RGBA").crop((borde, borde, borde + recorte, borde + recorte))

    for carpeta, clasico, lienzo in DENSIDADES:
        destino = os.path.join(res, "mipmap-" + carpeta)
        os.makedirs(destino, exist_ok=True)

        png(fg, lienzo).save(os.path.join(destino, "ic_launcher_foreground.png"), optimize=True)

        # Capa monocroma: la misma silueta, plana. El sistema la tiñe.
        silueta = Image.new("RGBA", (lienzo, lienzo), (255, 255, 255, 0))
        silueta.putalpha(png(fg, lienzo).split()[-1])
        silueta.paste((255, 255, 255), (0, 0), silueta)
        silueta.save(os.path.join(destino, "ic_launcher_monochrome.png"), optimize=True)

        chico = visible.resize((clasico, clasico), Image.LANCZOS)
        cuadrado = chico.copy()
        cuadrado.putalpha(mascara(clasico, int(clasico * 0.22)))
        cuadrado.save(os.path.join(destino, "ic_launcher.png"), optimize=True)

        redondo = chico.copy()
        redondo.putalpha(mascara(clasico, clasico // 2))
        redondo.save(os.path.join(destino, "ic_launcher_round.png"), optimize=True)

    dib = os.path.join(res, "drawable")
    os.makedirs(dib, exist_ok=True)
    with io.open(os.path.join(dib, "ic_launcher_background.xml"), "w", encoding="utf-8") as f:
        f.write(FONDO_VECTOR % COLORES)

    anydpi = os.path.join(res, "mipmap-anydpi-v26")
    os.makedirs(anydpi, exist_ok=True)
    for nombre in ("ic_launcher.xml", "ic_launcher_round.xml"):
        with io.open(os.path.join(anydpi, nombre), "w", encoding="utf-8") as f:
            f.write(ADAPTATIVO)


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in MOTIVOS:
        raise SystemExit("uso: gen-lanzador.py {%s} RUTA/res" % "|".join(sorted(MOTIVOS)))
    slug, res = sys.argv[1], sys.argv[2]
    factor = escala_comun()
    escribir(slug, res, factor)
    print("%s -> %s  (motivo al %.0f%% para caber en el círculo de 66 dp)"
          % (slug, res, factor * 100))
