# -*- coding: utf-8 -*-

MARCA   = "Liquid Sun"
TITULAR = "Juan Antonio Hernández López"
EMAIL   = "liquidsun.dev@gmail.com"
FECHA   = "8 de septiembre de 2026"

CSS = """
:root{--bg:#fbfbfc;--fg:#1a1c22;--fg2:#4a4d59;--line:#e0e0e7;--acc:#2f3a8f;--card:#fff}
@media(prefers-color-scheme:dark){:root{--bg:#14151a;--fg:#e9e9f0;--fg2:#b0b2be;--line:#2e3038;--acc:#96a0f0;--card:#1c1e25}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:44rem;margin:0 auto;padding:2.5rem 1.25rem 5rem}
a{color:var(--acc)}
h1{font-size:1.85rem;line-height:1.2;margin:0 0 .4rem}
h2{font-size:1.15rem;margin:2.4rem 0 .6rem;padding-bottom:.35rem;border-bottom:1px solid var(--line)}
.sub{color:var(--fg2);font-size:.95rem;margin:0 0 .3rem}
.meta{color:var(--fg2);font-size:.85rem;margin:1.4rem 0 0;padding-top:1rem;border-top:1px solid var(--line)}
p{margin:.8rem 0}
ul{margin:.7rem 0;padding-left:1.3rem}
li{margin:.35rem 0}
table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.92rem;display:block;overflow-x:auto}
th,td{text-align:left;padding:.55rem .7rem;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:600;font-size:.78rem;text-transform:uppercase;letter-spacing:.05em;color:var(--fg2)}
.box{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--acc);padding:.9rem 1.1rem;margin:1.2rem 0;font-size:.95rem}
.box p{margin:.35rem 0}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.87em;background:var(--card);border:1px solid var(--line);padding:.1em .35em;border-radius:3px}
footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--line);font-size:.85rem;color:var(--fg2)}
"""

DERECHOS = """<h2>Tus derechos</h2>
<p>El Reglamento General de Protección de Datos te reconoce el derecho a acceder a tus datos,
rectificarlos, suprimirlos, limitar u oponerte a su tratamiento y solicitar su portabilidad.</p>
<p>En esta aplicación la mayoría de esos derechos los ejerces tú directamente y sin
intermediarios: los datos están en tu dispositivo, y desinstalar la aplicación o borrar sus
datos desde los ajustes de Android los elimina por completo. No conservamos ninguna copia
que podamos devolverte o borrar en tu nombre.</p>
<p>Para cualquier consulta sobre este tratamiento puedes escribir a <a href="mailto:{email}">{email}</a>.
Si consideras que tus datos no se han tratado correctamente, puedes presentar una reclamación
ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es">www.aepd.es</a>).</p>"""

MENORES = """<h2>Menores</h2>
<p>Esta aplicación no está dirigida a menores de 14 años y no recopila deliberadamente
datos de menores de esa edad.</p>"""

CAMBIOS = """<h2>Cambios en esta política</h2>
<p>Si una versión futura de la aplicación trata datos de otra forma, esta página se
actualizará antes de publicar esa versión, y la fecha del encabezado lo reflejará.</p>"""

APPS = [
 dict(slug="grabadora", nombre="Grabadora Forense", pkg="com.forense.grabadora",
  claim="Graba audio y genera un informe de integridad con hora, ubicación y huella SHA-256.",
  cuerpo="""
<h2>Resumen en tres frases</h2>
<div class="box">
<p>Las grabaciones, la transcripción y los informes <strong>se quedan en tu teléfono</strong>. No hay
cuenta de usuario, no hay servidor propio y no se sube ningún audio a ninguna parte.</p>
<p>Lo único que sale del dispositivo es lo que exige la publicidad, y solo si tú lo autorizas.</p>
</div>

<h2>Qué datos trata la aplicación</h2>
<table>
<tr><th>Dato</th><th>Para qué</th><th>Dónde acaba</th></tr>
<tr><td>Grabaciones de audio</td><td>Es la función principal de la app</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Ubicación (GPS)</td><td>Incluir la coordenada en el informe. <strong>Opcional</strong>: si la rechazas, la app funciona igual</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Fecha, hora y zona horaria</td><td>Sellar el informe</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Identificador de publicidad</td><td>Mostrar anuncios</td><td>Google AdMob, solo con tu consentimiento</td></tr>
</table>

<h2>Publicidad</h2>
<p>La aplicación es gratuita y se financia con anuncios de <strong>Google AdMob</strong>. Antes de mostrar
ningún anuncio, la app te pide consentimiento mediante el formulario oficial de Google
(User Messaging Platform), tal y como exige la normativa europea.</p>
<p>Puedes cambiar o retirar tu consentimiento en cualquier momento desde las opciones de
privacidad dentro de la propia aplicación. Si lo rechazas, seguirás viendo anuncios, pero
no personalizados.</p>
<p>El tratamiento que Google hace de esos datos se rige por su propia política:
<a href="https://policies.google.com/privacy">policies.google.com/privacy</a>.</p>

<h2>Transcripción de voz</h2>
<p>La función de transcripción utiliza el <strong>reconocedor de voz del propio sistema Android</strong>.
Según la configuración de tu teléfono y el fabricante, ese reconocedor puede procesar el audio
en el dispositivo o enviarlo a los servidores de Google para convertirlo en texto. Ese
tratamiento lo realiza Google, no esta aplicación, y está sujeto a la política de privacidad
de Google enlazada arriba.</p>
<p>Si prefieres que no ocurra, simplemente no uses el botón de transcripción: la grabación
funciona sin él.</p>

<h2>Permisos que pide la aplicación</h2>
<ul>
<li><strong>Micrófono</strong> — imprescindible: sin él no hay grabación.</li>
<li><strong>Ubicación precisa y aproximada</strong> — opcional, solo para el informe.</li>
<li><strong>Notificaciones</strong> — para el aviso permanente mientras se graba, que Android exige.</li>
<li><strong>Servicio en primer plano (micrófono)</strong> — para que la grabación no se corte al apagar la pantalla.</li>
</ul>
<p>Mientras se graba, Android muestra siempre su propio indicador de micrófono en la barra de
estado, además de la notificación de la aplicación. Esta app no puede ocultar ninguno de los dos.</p>

<h2>Conservación</h2>
<p>Los archivos permanecen en tu dispositivo hasta que tú los borras. Al desinstalar la
aplicación se eliminan los que estén en su carpeta interna; los que hayas guardado en
Descargas o compartido con otras apps permanecen donde los pusiste.</p>

<h2>Un aviso sobre grabar conversaciones</h2>
<p>Las reglas sobre grabar una conversación cambian según el país. En España es legal grabar
una conversación en la que tú participas, pero difundirla puede no serlo. Esta aplicación es
una herramienta: el uso que hagas de las grabaciones es responsabilidad tuya.</p>
"""),

 dict(slug="cuentakm", nombre="Cuentakilómetros", pkg="app.nosceipsum.cuentakm",
  claim="Gasolineras con precios oficiales, reparto de gastos por tramos y consumo real por vehículo.",
  cuerpo="""
<h2>Resumen en tres frases</h2>
<div class="box">
<p>No hay cuenta de usuario, no hay registro y <strong>tus vehículos, repostajes y trayectos no
salen del teléfono</strong>.</p>
<p>La aplicación <strong>no muestra publicidad</strong> y no incorpora ningún sistema de analítica ni de
seguimiento.</p>
</div>

<h2>Qué datos trata la aplicación</h2>
<table>
<tr><th>Dato</th><th>Para qué</th><th>Dónde acaba</th></tr>
<tr><td>Ubicación (GPS)</td><td>Encontrar gasolineras cercanas y medir tramos. <strong>Opcional</strong>: puedes buscar por provincia sin dar ubicación</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Vehículos, repostajes y gastos</td><td>Calcular consumo real y coste de propiedad</td><td>Solo en tu dispositivo</td></tr>
</table>
<p>Tu ubicación se usa en el momento para ordenar resultados y calcular distancias. No se
envía a ningún servidor propio ni se guarda un historial de por dónde has pasado.</p>

<h2>Servicios de terceros que la aplicación consulta</h2>
<p>Para funcionar necesita pedir datos por internet. Cuando lo hace, el servicio consultado
recibe inevitablemente tu dirección IP, como en cualquier página web:</p>
<ul>
<li><strong>Ministerio para la Transición Ecológica</strong> — precios oficiales de carburantes.
La consulta pasa por un intermediario técnico propio alojado en Cloudflare, que no
almacena ningún dato personal.</li>
<li><strong>OpenStreetMap</strong> — las imágenes del mapa.
(<a href="https://osmfoundation.org/wiki/Privacy_Policy">política de OSM</a>)</li>
<li><strong>Google Fonts y cdnjs</strong> — tipografías y la librería del mapa.</li>
</ul>
<p>Ninguna de esas consultas incluye tus datos de vehículos, repostajes ni gastos.</p>

<h2>Permisos que pide la aplicación</h2>
<ul>
<li><strong>Ubicación precisa y aproximada</strong> — para las gasolineras cercanas y los tramos. Puedes denegarla y usar la búsqueda por provincia.</li>
<li><strong>Internet</strong> — para descargar los precios oficiales y el mapa.</li>
</ul>

<h2>Conservación</h2>
<p>Todo se guarda en el almacenamiento local de la aplicación y permanece hasta que tú lo
borras. Al desinstalarla, se elimina por completo.</p>
"""),

 dict(slug="pingcoins", nombre="PingCoins", pkg="com.pingcoins.app",
  claim="Analiza el sonido de una moneda al golpearla y lo compara con una biblioteca de firmas acústicas.",
  cuerpo="""
<h2>Resumen en tres frases</h2>
<div class="box">
<p>El micrófono <strong>solo se activa cuando pulsas el botón de escuchar</strong>, y se libera al salir de
esa pantalla o al pasar la app a segundo plano.</p>
<p><strong>No se graba audio y no se sube audio a ninguna parte.</strong> Del sonido solo se extraen
números: frecuencias de resonancia y tiempo de caída.</p>
</div>

<h2>Qué datos trata la aplicación</h2>
<table>
<tr><th>Dato</th><th>Para qué</th><th>Dónde acaba</th></tr>
<tr><td>Sonido captado por el micrófono</td><td>Calcular en el momento las frecuencias y el decaimiento</td><td>Se procesa y se descarta. No se almacena</td></tr>
<tr><td>Medidas resultantes (números)</td><td>Comparar la moneda con la biblioteca</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Fotos que añadas a una ficha</td><td>Documentar la pieza</td><td>Solo en tu dispositivo</td></tr>
</table>

<h2>Publicidad y analítica</h2>
<p>La aplicación <strong>no muestra publicidad</strong>, no incorpora analítica y no utiliza el
identificador de publicidad del dispositivo.</p>

<h2>Permisos que pide la aplicación</h2>
<ul>
<li><strong>Micrófono</strong> — imprescindible para analizar el sonido de la moneda. Android muestra su indicador mientras está activo.</li>
<li><strong>Internet</strong> — para actualizar la biblioteca de referencia.</li>
</ul>

<h2>Lo que esta aplicación no es</h2>
<p>El análisis acústico es <strong>orientativo</strong>. No es un peritaje ni un certificado de
autenticidad, y no sustituye la opinión de un profesional. Ninguna decisión de compra o
venta debería basarse únicamente en su resultado.</p>

<h2>Conservación</h2>
<p>Las medidas y las fotos se guardan en el almacenamiento local de la aplicación hasta que
tú las borras. Al desinstalarla, se eliminan.</p>
"""),

 dict(slug="sol", nombre="Sol · ventana de paseo", pkg="",
  claim="A qué hora salir a caminar o en bici: horas solares, meteorología y rutas.",
  cuerpo="""
<h2>Resumen en tres frases</h2>
<div class="box">
<p>No hay cuenta de usuario ni servidor propio. <strong>Tus ubicaciones guardadas y tu historial
se quedan en el almacenamiento local de tu navegador o dispositivo.</strong></p>
<p>La aplicación <strong>no muestra publicidad</strong> y no incorpora analítica.</p>
</div>

<h2>Qué datos trata la aplicación</h2>
<table>
<tr><th>Dato</th><th>Para qué</th><th>Dónde acaba</th></tr>
<tr><td>Ubicación (GPS o escrita por ti)</td><td>Calcular las horas solares y el tiempo de tu zona</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Últimas ubicaciones y ajustes</td><td>No tener que volver a escribirlos</td><td>Solo en tu dispositivo</td></tr>
</table>
<p>Puedes usar la aplicación sin dar acceso al GPS: basta con escribir el nombre de una
ciudad o pegar unas coordenadas.</p>

<h2>Servicios de terceros que la aplicación consulta</h2>
<p>Para dar el tiempo y los mapas hay que pedir datos por internet. El servicio consultado
recibe tu dirección IP y las coordenadas de la zona que estás mirando:</p>
<ul>
<li><strong>Open-Meteo</strong> — predicción meteorológica, calidad del aire, elevación y búsqueda de
ciudades. (<a href="https://open-meteo.com/en/terms">condiciones de Open-Meteo</a>)</li>
<li><strong>OpenStreetMap</strong> — las imágenes del mapa y el cálculo de rutas a pie y en bici.
(<a href="https://osmfoundation.org/wiki/Privacy_Policy">política de OSM</a>)</li>
</ul>
<p>Ninguno de esos servicios recibe un identificador tuyo: no hay cuenta que asociar.</p>

<h2>Conservación</h2>
<p>Todo lo guardado vive en el almacenamiento local de tu navegador o de la aplicación
instalada. Borrar los datos del sitio, o desinstalarla, lo elimina por completo.</p>
"""),
]

PAG = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Política de privacidad · {nombre}</title>
<style>{css}</style>
</head>
<body>
<div class="w">
<h1>Política de privacidad</h1>
<p class="sub"><strong>{nombre}</strong>{pkgtxt}</p>
<p class="sub">{claim}</p>
<p class="meta">Editor: {marca} · Responsable del tratamiento: {titular}<br>Contacto:
<a href="mailto:{email}">{email}</a> · Última actualización: {fecha}</p>
{cuerpo}
{derechos}
{menores}
{cambios}
<footer><a href="./index.html">Volver al índice</a></footer>
</div>
</body>
</html>
"""

IDX = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Liquid Sun · Políticas de privacidad</title>
<style>{css}</style>
</head>
<body>
<div class="w">
<h1>Liquid Sun</h1>
<p class="sub">Políticas de privacidad de las aplicaciones publicadas por {marca} ({titular}).</p>
<p class="meta">Contacto: <a href="mailto:{email}">{email}</a> · Última actualización: {fecha}</p>
<h2>Aplicaciones</h2>
<ul>
{items}
</ul>
<footer>Este repositorio contiene únicamente textos legales. El código de las aplicaciones no es público.</footer>
</div>
</body>
</html>
"""

items = []
for a in APPS:
    pkgtxt = ' — <code>%s</code>' % a["pkg"] if a["pkg"] else ""
    # Página plana: "grabadora.html", no "grabadora/index.html". Subir el ZIP
    # desde el navegador de GitHub aplasta las carpetas, así que la ruta con
    # carpeta se rompería en cuanto alguien editase desde la web. Las URLs
    # planas son además las que están dadas de alta en Play Console.
    with open("%s.html" % a["slug"], "w", encoding="utf-8") as f:
        f.write(PAG.format(css=CSS, marca=MARCA, nombre=a["nombre"], pkgtxt=pkgtxt, claim=a["claim"],
                           titular=TITULAR, email=EMAIL, fecha=FECHA, cuerpo=a["cuerpo"],
                           derechos=DERECHOS.format(email=EMAIL), menores=MENORES, cambios=CAMBIOS))
    items.append('<li><a href="./%s.html">%s</a> — %s</li>' % (a["slug"], a["nombre"], a["claim"]))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(IDX.format(css=CSS, marca=MARCA, titular=TITULAR, email=EMAIL, fecha=FECHA, items="\n".join(items)))
print("generadas:", len(APPS) + 1, "paginas")
