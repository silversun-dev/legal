# -*- coding: utf-8 -*-
"""
Genera el sistema de logos de Liquid Sun.

Cada marca se define una sola vez (símbolo + paleta) y de ahí salen dos
archivos: el icono cuadrado para las tiendas y el símbolo suelto para
documentos y web. Igual que gen.py con los textos legales: se edita aquí y se
ejecuta

    python3 gen_logos.py

Sistema común: lienzo de 512, símbolo dentro de un área segura de 320,
trazo de 30 con extremos redondeados, y un arco o un disco en todos los
símbolos para que se lean como familia.
"""
import os, html

AQUI = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Los símbolos.
#
# Tokens que se sustituyen al generar:
#   @P@    prefijo único para los id (dos SVG en la misma página chocarían)
#   @INK@  trazo principal
#   @ACC@  acento
#   @DP@   tono profundo, para las masas dentro del acento
# --------------------------------------------------------------------------

SIMBOLOS = {}

# Marca madre: el disco de sol con el líquido dentro, y la gota que cae.
SIMBOLOS["liquid-sun"] = """
<defs>
  <linearGradient id="@P@sol" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="@ACC@"/><stop offset="1" stop-color="@DP@"/>
  </linearGradient>
  <clipPath id="@P@disco"><circle cx="256" cy="206" r="132"/></clipPath>
</defs>
<circle cx="256" cy="206" r="132" fill="url(#@P@sol)"/>
<path d="M118 256 C 166 226 206 284 256 284 C 306 284 346 226 394 256 L 394 362 L 118 362 Z"
      clip-path="url(#@P@disco)" fill="@INK@" opacity="0.88"/>
<path d="M256 340 C 244 366 214 392 214 412 A 42 42 0 0 0 298 412 C 298 392 268 366 256 340 Z"
      fill="url(#@P@sol)"/>
"""

# Grabadora Forense: el sello alrededor de la onda. Lo que se graba, sellado.
SIMBOLOS["grabadora"] = """
<circle cx="256" cy="256" r="146" fill="none" stroke="@INK@" stroke-width="30"/>
<g fill="@ACC@">
  <rect x="156" y="228" width="24" height="56"  rx="12"/>
  <rect x="200" y="202" width="24" height="108" rx="12"/>
  <rect x="244" y="176" width="24" height="160" rx="12"/>
  <rect x="288" y="202" width="24" height="108" rx="12"/>
  <rect x="332" y="228" width="24" height="56"  rx="12"/>
</g>
"""

# Cuentakilómetros: el cuadrante y la aguja.
SIMBOLOS["cuentakm"] = """
<path d="M126 316 A 130 130 0 0 1 386 316" fill="none" stroke="@INK@"
      stroke-width="32" stroke-linecap="round"/>
<g stroke="@INK@" stroke-width="14" stroke-linecap="round" opacity="0.45">
  <path d="M154 236 L 175 251"/>
  <path d="M256 196 L 256 222"/>
  <path d="M358 236 L 337 251"/>
</g>
<path d="M256 316 L 340 228" stroke="@ACC@" stroke-width="30" stroke-linecap="round"/>
<circle cx="256" cy="316" r="26" fill="@INK@"/>
"""

# Sun Bell: la moneda que suena.
SIMBOLOS["sunbell"] = """
<circle cx="248" cy="256" r="114" fill="none" stroke="@INK@" stroke-width="32"/>
<circle cx="248" cy="256" r="42" fill="@INK@"/>
<path d="M344 172 A 128 128 0 0 1 344 340" fill="none" stroke="@ACC@"
      stroke-width="26" stroke-linecap="round"/>
<path d="M381 140 A 176 176 0 0 1 381 372" fill="none" stroke="@ACC@"
      stroke-width="26" stroke-linecap="round" opacity="0.6"/>
"""

# Sol: la carrera del sol sobre el horizonte, y dónde cae la ventana.
SIMBOLOS["sol"] = """
<path d="M126 348 A 130 130 0 0 1 386 348" fill="none" stroke="@INK@"
      stroke-width="16" stroke-linecap="round" stroke-dasharray="0.01 54" opacity="0.8"/>
<path d="M112 348 L 400 348" stroke="@INK@" stroke-width="28" stroke-linecap="round"/>
<circle cx="321" cy="235" r="56" fill="@ACC@"/>
"""

# NumisCore: el metal fino dentro del peso bruto.
SIMBOLOS["numiscore"] = """
<circle cx="256" cy="256" r="146" fill="none" stroke="@INK@" stroke-width="30"/>
<circle cx="256" cy="256" r="104" fill="none" stroke="@INK@" stroke-width="8"
        stroke-dasharray="2 24" stroke-linecap="round" opacity="0.65"/>
<circle cx="256" cy="256" r="66" fill="@ACC@"/>
"""

# Inglés: lo que se dice, dentro de la tarjeta.
SIMBOLOS["ingles"] = """
<path d="M124 132 H388 A40 40 0 0 1 428 172 V340 A40 40 0 0 1 388 380 H222 L150 436 V380
         H124 A40 40 0 0 1 84 340 V172 A40 40 0 0 1 124 132 Z"
      fill="none" stroke="@INK@" stroke-width="30" stroke-linejoin="round"/>
<g fill="@ACC@">
  <rect x="199" y="230" width="22" height="52" rx="11"/>
  <rect x="245" y="210" width="22" height="92" rx="11"/>
  <rect x="291" y="230" width="22" height="52" rx="11"/>
</g>
"""

# ON — UMBRA: el umbral, y detrás la luz que sólo se ve de canto.
SIMBOLOS["on-umbra"] = """
<defs>
  <mask id="@P@ecl">
    <circle cx="268" cy="272" r="62" fill="#fff"/>
    <circle cx="292" cy="256" r="60" fill="#000"/>
  </mask>
</defs>
<path d="M146 428 V 268 A 110 110 0 0 1 366 268 V 428" fill="none" stroke="@INK@"
      stroke-width="32" stroke-linecap="round"/>
<circle cx="268" cy="272" r="62" fill="@ACC@" mask="url(#@P@ecl)"/>
"""

# Descorche: el corcho ya fuera.
SIMBOLOS["descorche"] = """
<g transform="rotate(-16 258 104)"><rect x="230" y="60" width="56" height="76" rx="16" fill="@ACC@"/></g>
<path d="M226 190 V244 C226 284 186 292 186 340 V416 A28 28 0 0 0 214 444
         H298 A28 28 0 0 0 326 416 V340 C326 292 286 284 286 244 V190"
      fill="none" stroke="@INK@" stroke-width="30" stroke-linejoin="round"
      stroke-linecap="round"/>
<rect x="208" y="344" width="96" height="58" rx="12" fill="@ACC@"/>
"""

# Reflejo Interno: lo de arriba y lo de abajo, separados por la lámina de agua.
SIMBOLOS["reflejo-interno"] = """
<defs>
  <mask id="@P@agua">
    <rect x="0" y="0" width="512" height="512" fill="#000"/>
    <ellipse cx="256" cy="382" rx="88" ry="64" fill="#fff"/>
    <rect x="140" y="334" width="232" height="9" fill="#000"/>
    <rect x="140" y="378" width="232" height="7" fill="#000"/>
  </mask>
</defs>
<circle cx="256" cy="184" r="94" fill="@ACC@"/>
<path d="M116 296 L 396 296" stroke="@INK@" stroke-width="26" stroke-linecap="round"/>
<rect x="140" y="300" width="232" height="212" fill="@ACC@" opacity="0.4" mask="url(#@P@agua)"/>
"""

# --------------------------------------------------------------------------
# Las marcas: nombre, repositorio, qué es, y los dos juegos de color.
#
#   icono  — sobre el fondo del icono de la tienda
#   plano  — el símbolo suelto, sobre papel o sobre página blanca
# --------------------------------------------------------------------------

MARCAS = [
 dict(slug="liquid-sun", nombre="Liquid Sun", repo="—",
      que="El sol que se ha vuelto líquido: metal fundido dentro del disco, y la "
          "gota que ya ha caído.",
      bg=("#252B63", "#161A3D"), ink="#D2600A", acc="#FFCB5C", dp="#FFA51F",
      plano_ink="#D2600A", plano_acc="#F3B22E", plano_dp="#E0871A"),

 dict(slug="grabadora", nombre="Grabadora Forense", repo="grabadora",
      que="La onda encerrada en un sello. El anillo es la huella SHA-256 que "
          "rodea lo grabado: dentro no se toca nada.",
      bg=("#334155", "#1B2331"), ink="#E8EDF4", acc="#5EC2F5",
      plano_ink="#1F2937", plano_acc="#0369A1"),

 dict(slug="cuentakm", nombre="Cuentakilómetros", repo="gasolineras",
      que="El cuadrante con la aguja subida. Tres marcas de graduación, las "
          "justas para que se lea como tablero de coche y no como reloj.",
      bg=("#0F766E", "#083F3B"), ink="#EAFBF6", acc="#FFC24A",
      plano_ink="#0F766E", plano_acc="#D97706"),

 dict(slug="sunbell", nombre="Sun Bell", repo="ping-coin",
      que="La moneda golpeada y lo que sale de ella. Dos arcos, no cinco: es un "
          "ping, un golpe seco, no una campana repicando.",
      bg=("#475569", "#232B3A"), ink="#F1F5F9", acc="#FFC24A",
      plano_ink="#334155", plano_acc="#B45309"),

 dict(slug="sol", nombre="Sol · ventana de paseo", repo="sol",
      que="La carrera del sol punteada sobre el horizonte, con el sol ya "
          "cayendo. El disco marca la hora en la que se puede salir.",
      bg=("#2A4A9E", "#0D1638"), ink="#DCE6FF", acc="#FFC24A",
      plano_ink="#1E3A8A", plano_acc="#E2670C"),

 dict(slug="numiscore", nombre="NumisCore", repo="numiscode",
      que="El peso bruto fuera, la ley en el anillo punteado y el metal fino "
          "en el centro. El orden del cálculo, dibujado.",
      bg=("#3F3F46", "#18181B"), ink="#E4E4E7", acc="#FFC24A",
      plano_ink="#27272A", plano_acc="#B58A2B"),

 dict(slug="ingles", nombre="Inglés", repo="ingles",
      que="La tarjeta convertida en bocadillo, porque la app no es de leer "
          "fichas: es de decirlas en voz alta.",
      bg=("#2563EB", "#1436A4"), ink="#EFF6FF", acc="#FFC24A",
      plano_ink="#1D4ED8", plano_acc="#D97706"),

 dict(slug="on-umbra", nombre="ON — UMBRA", repo="ON",
      que="El umbral abierto y, dentro, el eclipse. Se entra por voluntad "
          "propia y se puede salir: el arco no tiene puerta.",
      bg=("#241B3A", "#0B0A1A"), ink="#8B7BB8", acc="#D9B45F",
      plano_ink="#4C3F73", plano_acc="#A67C1A"),

 dict(slug="descorche", nombre="Descorche", repo="vinos",
      que="El corcho ya fuera y la etiqueta en su sitio. Lo que hace la app "
          "está en ese hueco entre el corcho y la boca.",
      bg=("#881337", "#440A1C"), ink="#FDE8E8", acc="#E8B04B",
      plano_ink="#881337", plano_acc="#A16207"),

 dict(slug="reflejo-interno", nombre="Reflejo Interno", repo="reflejo-interno",
      que="Lo de arriba y lo de abajo separados por la lámina de agua. El "
          "reflejo llega roto, que es como llega de verdad.",
      bg=("#6D5A9C", "#332748"), ink="#EDE9FE", acc="#C4B5FD",
      plano_ink="#4C3A73", plano_acc="#8B77C4"),
]

# --------------------------------------------------------------------------

def pinta(slug, prefijo, ink, acc, dp):
    """Devuelve el símbolo con los colores y los id ya resueltos."""
    s = SIMBOLOS[slug]
    for token, valor in (("@P@", prefijo), ("@INK@", ink), ("@ACC@", acc), ("@DP@", dp)):
        s = s.replace(token, valor)
    return s.strip()


def icono(m):
    p = "i-%s-" % m["slug"]
    cuerpo = pinta(m["slug"], p, m["ink"], m["acc"], m.get("dp", m["acc"]))
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512" role="img" aria-label="%s">
<defs><linearGradient id="%sbg" x1="0" y1="0" x2="0.35" y2="1">
<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>
<rect width="512" height="512" rx="114" fill="url(#%sbg)"/>
%s
</svg>
""" % (html.escape(m["nombre"]), p, m["bg"][0], m["bg"][1], p, cuerpo)


def marca(m):
    p = "m-%s-" % m["slug"]
    cuerpo = pinta(m["slug"], p, m["plano_ink"], m["plano_acc"],
                   m.get("plano_dp", m["plano_acc"]))
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512" role="img" aria-label="%s">
%s
</svg>
""" % (html.escape(m["nombre"]), cuerpo)


# --------------------------------------------------------------------------
# La hoja de marca. Se escribe dos veces: la página suelta para el repositorio
# y el cuerpo sin envoltorio, que es lo que come la herramienta de Artifacts.
# --------------------------------------------------------------------------

FUENTES = ("https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;1,400"
           "&family=Hanken+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap")

CSS_HOJA = """
:root{
  --papel:#F5F6FB; --sup:#FFFFFF; --linea:#DCDFEC; --linea2:#EAECF4;
  --tinta:#14172B; --tinta2:#565C7A; --acc:#2F3A8F; --oro:#9A6B0E;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --papel:#0E1122; --sup:#171B32; --linea:#2C3150; --linea2:#232842;
    --tinta:#E6E9F7; --tinta2:#A0A6C4; --acc:#96A0F0; --oro:#E0AE4A;
  }
}
:root[data-theme="dark"]{
  --papel:#0E1122; --sup:#171B32; --linea:#2C3150; --linea2:#232842;
  --tinta:#E6E9F7; --tinta2:#A0A6C4; --acc:#96A0F0; --oro:#E0AE4A;
}
*{box-sizing:border-box}
body{margin:0;background:var(--papel);color:var(--tinta);
  font:400 16px/1.6 "Hanken Grotesk",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  -webkit-font-smoothing:antialiased}
.w{max-width:62rem;margin:0 auto;padding-block:3rem 5rem;padding-left:1.25rem;padding-right:1.25rem}
.eyebrow{font:500 .72rem/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.14em;
  text-transform:uppercase;color:var(--tinta2);margin:0 0 1.1rem}
h1{font:600 clamp(2.6rem,7vw,4.2rem)/1.02 Spectral,Georgia,serif;margin:0 0 .5rem;
  letter-spacing:-.02em;text-wrap:balance}
.lede{font-size:1.12rem;color:var(--tinta2);max-width:38rem;margin:0}
h2{font:600 1.4rem/1.2 Spectral,Georgia,serif;margin:0;letter-spacing:-.01em}
.sec{margin-top:4rem;border-top:1px solid var(--linea);padding-top:1.6rem}
.sec-head{display:flex;align-items:baseline;gap:.9rem;flex-wrap:wrap;margin-bottom:1.6rem}
.sec-head p{margin:0;color:var(--tinta2);font-size:.95rem}

/* La marca madre manda: dos columnas y el icono al tamaño de la ficha real. */
.madre{display:grid;grid-template-columns:minmax(0,15rem) minmax(0,1fr);gap:2.4rem;align-items:start}
.madre .arte{display:flex;flex-direction:column;gap:1rem}
.madre svg{width:100%;height:auto;display:block;border-radius:0}
.madre .cuerpo p{margin:0 0 1rem;max-width:34rem}
@media (max-width:640px){.madre{grid-template-columns:1fr}}

.rej{display:grid;grid-template-columns:repeat(auto-fit,minmax(17rem,1fr));gap:1.4rem}
.f{background:var(--sup);border:1px solid var(--linea);border-radius:14px;padding:1.3rem 1.3rem 1.1rem;
  display:flex;flex-direction:column;gap:.9rem}
.f-top{display:flex;gap:1rem;align-items:center}
.f-top .ico{width:76px;height:76px;flex:0 0 76px}
.f-top .ico svg{width:100%;height:100%;display:block}
.f-nom{font:600 1.18rem/1.15 Spectral,Georgia,serif;margin:0;letter-spacing:-.01em}
.f-repo{font:400 .74rem/1.4 "JetBrains Mono",ui-monospace,monospace;color:var(--tinta2);margin:.25rem 0 0}
.f-que{margin:0;font-size:.92rem;color:var(--tinta2);flex:1}

/* La tira de comprobación: el mismo símbolo a los tamaños en que se va a ver
   de verdad, y suelto sobre papel. Si aguanta los 24, aguanta. */
.tira{display:flex;align-items:center;gap:.85rem;padding:.7rem .8rem;border-radius:10px;
  background:var(--linea2);border:1px solid var(--linea)}
.tira svg{display:block}
.t48 svg{width:44px;height:44px}
.t24 svg{width:24px;height:24px}
.papel{background:#FFFFFF;border-radius:8px;padding:5px;display:flex;box-shadow:0 1px 2px rgba(20,23,43,.14)}
.papel svg{width:34px;height:34px}
.tira-nota{font:400 .68rem/1.3 "JetBrains Mono",ui-monospace,monospace;color:var(--tinta2);
  margin-left:auto;text-align:right}

.pal{display:flex;gap:.4rem;flex-wrap:wrap}
.sw{font:400 .66rem/1 "JetBrains Mono",ui-monospace,monospace;padding:.42rem .5rem;border-radius:6px;
  border:1px solid rgba(127,132,160,.35);color:#fff;text-transform:uppercase}
.sw.claro{color:#14172B}

table{width:100%;border-collapse:collapse;font-size:.92rem;margin-top:.4rem}
th,td{text-align:left;padding:.55rem .7rem;border-bottom:1px solid var(--linea)}
th{font:500 .7rem/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.1em;
  text-transform:uppercase;color:var(--tinta2)}
td code,.mono{font:400 .84rem/1.5 "JetBrains Mono",ui-monospace,monospace;color:var(--acc)}
.tabla-caja{overflow-x:auto}
.nota{background:var(--sup);border:1px solid var(--linea);border-left:3px solid var(--oro);
  border-radius:0 10px 10px 0;padding:1rem 1.2rem;margin-top:1.4rem}
.nota p{margin:.35rem 0;font-size:.94rem}
.nota p:first-child{margin-top:0}
footer{margin-top:3.5rem;padding-top:1.2rem;border-top:1px solid var(--linea);
  color:var(--tinta2);font-size:.86rem}
a{color:var(--acc)}
"""


def _es_claro(hex_color):
    """Luminancia burda, sólo para decidir si el hex va en negro o en blanco."""
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    return (0.299 * r + 0.587 * g + 0.114 * b) > 150


def _swatches(m):
    colores = [m["bg"][0], m["bg"][1], m["acc"], m["ink"]]
    vistos, out = set(), []
    for c in colores:
        if c.upper() in vistos:
            continue
        vistos.add(c.upper())
        clase = "sw claro" if _es_claro(c) else "sw"
        out.append('<span class="%s" style="background:%s">%s</span>' % (clase, c, c.upper()))
    return '<div class="pal">' + "".join(out) + "</div>"


def cuerpo_hoja():
    ico = {m["slug"]: icono(m) for m in MARCAS}
    mar = {m["slug"]: marca(m) for m in MARCAS}
    madre = MARCAS[0]
    resto = MARCAS[1:]

    p = []
    p.append('<div class="w">')
    p.append('<p class="eyebrow">Sistema de marca · %s</p>' % FECHA_HOJA)
    p.append("<h1>Liquid Sun</h1>")
    p.append('<p class="lede">Diez marcas construidas sobre la misma rejilla: lienzo de 512, '
             'símbolo dentro de un área segura de 320 y trazo de 30 con los extremos redondeados. '
             'Cada una lleva un disco o un arco, que es lo que las hace familia sin obligarlas a '
             'parecerse.</p>')

    p.append('<div class="sec"><div class="sec-head"><h2>La marca de la casa</h2>'
             '<p>El sol líquido</p></div>')
    p.append('<div class="madre"><div class="arte">%s<div class="tira">'
             '<span class="t48">%s</span><span class="t24">%s</span>'
             '<span class="papel">%s</span>'
             '<span class="tira-nota">48 · 24 · papel</span></div></div>'
             % (ico[madre["slug"]], ico[madre["slug"]], ico[madre["slug"]], mar[madre["slug"]]))
    p.append('<div class="cuerpo"><p>%s</p>' % madre["que"])
    p.append("<p>El oro y el naranja profundo son de la casa y no se repiten en ninguna app: "
             "una app que use el oro de Liquid Sun compite con su propia marca. Lo que sí se "
             "repite es el azul <span class=\"mono\">#2F3A8F</span>, que ya venía de las "
             "páginas legales y aquí queda como el color del editor, no de ningún producto.</p>")
    p.append(_swatches(madre))
    p.append("</div></div></div>")

    p.append('<div class="sec"><div class="sec-head"><h2>Las aplicaciones</h2>'
             '<p>Nueve marcas, una por repositorio</p></div><div class="rej">')
    for m in resto:
        p.append('<div class="f">')
        p.append('<div class="f-top"><div class="ico">%s</div><div><p class="f-nom">%s</p>'
                 '<p class="f-repo">%s</p></div></div>' % (ico[m["slug"]], m["nombre"], m["repo"]))
        p.append('<p class="f-que">%s</p>' % m["que"])
        p.append('<div class="tira"><span class="t48">%s</span><span class="t24">%s</span>'
                 '<span class="papel">%s</span>'
                 '<span class="tira-nota">48 · 24<br>papel</span></div>'
                 % (ico[m["slug"]], ico[m["slug"]], mar[m["slug"]]))
        p.append(_swatches(m))
        p.append("</div>")
    p.append("</div></div>")

    p.append('<div class="sec"><div class="sec-head"><h2>Los archivos</h2>'
             '<p>Vectores, sin ningún PNG que mantener</p></div>')
    p.append('<div class="tabla-caja"><table><thead><tr><th>Ruta</th><th>Qué es</th>'
             '<th>Dónde va</th></tr></thead><tbody>')
    p.append('<tr><td><code>brand/icono/&lt;app&gt;.svg</code></td><td>Icono cuadrado con fondo, '
             'esquinas de radio 114</td><td>Play Console, launcher, favicon</td></tr>')
    p.append('<tr><td><code>brand/marca/&lt;app&gt;.svg</code></td><td>Símbolo suelto, sin fondo, '
             'a dos tintas</td><td>Web, documentos, cabeceras</td></tr>')
    p.append('<tr><td><code>brand/gen_logos.py</code></td><td>La definición de las diez marcas'
             '</td><td>Se edita aquí y se ejecuta</td></tr>')
    p.append("</tbody></table></div>")
    p.append('<div class="nota"><p><strong>Play Store pide un PNG de 512×512 sin transparencia.'
             '</strong> Sale del SVG con una sola orden:</p>'
             '<p class="mono">rsvg-convert -w 512 -h 512 icono/sol.svg -o sol-512.png</p>'
             '<p>O abriendo el SVG en el navegador y exportando. El vector es el original; '
             'el PNG se regenera cuando haga falta y no se versiona.</p></div>')
    p.append('<div class="nota"><p><strong>Faltan dos.</strong> <span class="mono">spam</span> y '
             '<span class="mono">e-SIM</span> se han dejado fuera a propósito: puede que su marca '
             'se esté resolviendo por otro lado, y dos identidades para la misma app es peor que '
             'ninguna.</p></div>')
    p.append("</div>")

    p.append('<footer>Liquid Sun · Juan Antonio Hernández López · '
             '<a href="mailto:liquidsun.dev@gmail.com">liquidsun.dev@gmail.com</a></footer>')
    p.append("</div>")
    return "\n".join(p)


FECHA_HOJA = "10 de septiembre de 2026"


def escribe_hoja():
    cuerpo = cuerpo_hoja()
    cabeza = ('<title>Marcas Liquid Sun</title>\n'
              '<link rel="stylesheet" href="%s">\n<style>%s</style>\n' % (FUENTES, CSS_HOJA))

    with open(os.path.join(AQUI, "index.html"), "w", encoding="utf-8") as f:
        f.write('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
                + cabeza + "</head>\n<body>\n" + cuerpo + "\n</body>\n</html>\n")

    ruta_art = os.path.join(AQUI, "hoja-artifact.html")
    with open(ruta_art, "w", encoding="utf-8") as f:
        f.write(cabeza + cuerpo + "\n")
    return ruta_art


def main():
    for carpeta in ("icono", "marca"):
        os.makedirs(os.path.join(AQUI, carpeta), exist_ok=True)

    for m in MARCAS:
        with open(os.path.join(AQUI, "icono", m["slug"] + ".svg"), "w", encoding="utf-8") as f:
            f.write(icono(m))
        with open(os.path.join(AQUI, "marca", m["slug"] + ".svg"), "w", encoding="utf-8") as f:
            f.write(marca(m))
        print("  %-18s icono/%s.svg  marca/%s.svg" % (m["nombre"], m["slug"], m["slug"]))

    ruta = escribe_hoja()
    print("  hoja de marca      index.html  %s" % os.path.basename(ruta))
    print("\n%d marcas, %d archivos." % (len(MARCAS), len(MARCAS) * 2 + 2))


if __name__ == "__main__":
    main()
