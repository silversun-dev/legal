# INVENTARIO — legal

> Subinventario de este proyecto. Copia maestra en `silversun-dev/inventario` → `proyectos/legal.md`.
> **Estado: ✅ RELLENADO**

| Campo | Valor |
|---|---|
| Última actualización | 2026-09-22 |
| Actualizado por (sesión/rama) | sesión inventario (análisis inicial) |
| Tipo de app | **No es una app.** Web estática pública (GitHub Pages) con las políticas de privacidad de las apps de Liquid Sun, generadas por `gen.py` (una sola plantilla y una sola sección de derechos RGPD). Incluye `PUBLICIDAD.md`, un aviso permanente sobre cómo declarar anuncios. |
| **% listo para publicar** | 60 % (completitud para su propósito) |
| Justificación del % | Publicado y funcionando para 4 apps: Grabadora Forense (`com.forense.grabadora`, con AdMob y UMP), Cuentakilómetros (`app.nosceipsum.cuentakm`), Sun Bell (`com.sunbell.app`, con AdMob y alias `pingcoins.html`) y Sol (sin ID de paquete). `python3 gen.py` genera 5 páginas idénticas a las del repo. **Faltan políticas** de GymTonic (solo existe en una rama sin fusionar y no cuadra con la app real) e Ingles (destino Google Play). Probablemente también de Descorche (vinos), NumiScore (numiscode), ON Umbra (ON) y Reflejo Interno, que ya tienen logo en la rama `brand/`. No hay versión en inglés ni página de borrado de cuenta. |
| Destino previsto | Web pública: GitHub Pages, que en el plan gratuito exige repo público. Son las URL que se ponen en Play Console. |

## 1. Trabajo autónomo pendiente (lo que Claude puede hacer solo)
| # | Tarea | Tokens estimados |
|---|---|---|
| 1 | Traer la política de GymTonic de la rama `laughing-hawking` a `gen.py` y reescribirla según lo que hace de verdad el repo GymTonic: servidor Flask, datos de salud del art. 9 RGPD, cifrado, Open Food Facts y cobro | 100k |
| 2 | Política de Ingles: MyMemory, dictionaryapi.dev, compra Pro con Play Billing y, si se decide, AdMob | 80k |
| 3 | Políticas de las demás apps que se vayan a publicar (Descorche, NumiScore, ON Umbra, Reflejo Interno…): leer cada repo y redactarla, ~60k por app | 240k |
| 4 | Revisar la política de Sol: el repo usa OSRM para las rutas (la política dice OSM), y añadir el ID de paquete cuando exista | 30k |
| 5 | Fusionar a mano solo las carpetas `brand/` (rama `awesome-cori`) y/o `marca/` (rama `sweet-dijkstra`), sin arrastrar sus versiones antiguas de `gen.py` ni de las páginas | 50k |
| 6 | Página de eliminación de cuenta y datos, que Play exige cuando la app tiene cuentas (Sun Bell con Supabase), y actualizar la política de Sun Bell antes de conectar el backend | 80k |
| 7 | Versión en inglés de todas las políticas (`gen.py` con dos idiomas) | 120k |
| 8 | Script de coherencia: comparar cada política con el repo de su app (AdMob, permisos, `applicationId`) y avisar si no coinciden | 40k |
| | **TOTAL** | **~740k** |

## 2. Decisiones pendientes (las toma el usuario)
- [ ] Qué apps necesitan política ya (GymTonic, Ingles, Descorche, NumiScore, ON, Reflejo Interno…) y con qué nombre y paquete definitivos.
- [ ] Ramas sin fusionar: qué hacer con la política de GymTonic (`laughing-hawking`) y con los logos. ¿Se quedan en este repo público `brand/` (10 logos SVG, `awesome-cori`) o `marca/` (iconos de lanzador PNG de 512 px, `sweet-dijkstra`), o se van a otro sitio? Después, borrar las ramas obsoletas.
- [ ] Sol y Cuentakilómetros dicen «no muestra publicidad». Si alguna va a llevar anuncios, hay que cambiarlo antes, según la regla de `PUBLICIDAD.md`.
- [ ] ¿Publicar las políticas también en inglés, para fichas de Play fuera de España?
- [ ] Nombre definitivo de Sun Bell/PingCoins (`com.sunbell.app` frente a `com.pingcoins.app`), a decidir en el repo ping-coin. La política usa `com.sunbell.app`.

## 3. Pruebas manuales que tiene que hacer el usuario
- [ ] Abrir en el navegador las 5 páginas y el índice (incluida `pingcoins.html`) y comprobar que cargan.
- [ ] Comprobar en Settings → Pages que GitHub Pages sigue activo sobre `main` (raíz).
- [ ] En Play Console, comprobar que cada app apunta a su URL plana (`…/legal/<app>.html`), no a una con carpeta, que da 404.
- [ ] Comprobar que el paquete de cada política (`com.forense.grabadora`, `app.nosceipsum.cuentakm`, `com.sunbell.app`) coincide con el `applicationId` real del AAB.
- [ ] Comprobar que el formulario de Seguridad de los datos y la casilla «Contiene anuncios» de cada ficha dicen lo mismo que su política.

## 4. Cómo probar la app
- Enlace / acceso directo: https://silversun-dev.github.io/legal/ (índice). Páginas: `grabadora.html`, `cuentakm.html`, `sunbell.html` (y su alias `pingcoins.html`), `sol.html`. No se ha podido comprobar desde aquí.
- Instrucciones: en local, `python3 gen.py` regenera las páginas; luego `python3 -m http.server` y abrir `http://localhost:8000/`.

## 5. Peligros, problemas y avisos
- ⚠️ **La política de GymTonic de la rama `laughing-hawking` describe otra app.** Habla de una app móvil sin servidor propio, con todo guardado en el teléfono. El repo GymTonic es un servidor Flask con datos de salud cifrados (lesiones, medicación, peso) y un plan de pago. Publicarla tal cual sería afirmar algo falso, que es justo lo que `PUBLICIDAD.md` prohíbe.
- ⚠️ **Ramas con trabajo sin fusionar**:
  - `awesome-cori` (10 sep): `brand/` con 10 logos y su generador.
  - `sweet-dijkstra` (10 sep): `marca/` con iconos de lanzador.
  - `laughing-hawking` (21 sep): política de GymTonic.
  
  Las tres son anteriores a Sun Bell: una fusión normal borraría `sunbell.html` y devolvería `pingcoins.html` a su versión antigua. Hay que traer solo las carpetas o bloques nuevos. `sunbell-politica-anuncios` ya está en `main`.
- ⚠️ **Faltan políticas**: Ingles y GymTonic tienen Google Play como destino posible. Descorche, NumiScore, ON Umbra y Reflejo Interno tienen logo preparado pero no política. Play rechaza una app sin URL de política.
- ⚠️ **Sol y Cuentakilómetros afirman «no muestra publicidad».** El inventario de Sol contempla AdMob si se publica con Capacitor. Si llegan anuncios sin cambiar la página, la política quedaría falsa.
- ⚠️ **Sol**: la política atribuye el cálculo de rutas a OpenStreetMap, pero el repo usa OSRM (servidor de demostración, solo uso no comercial). Hay que declarar bien los terceros. El `pkg` está vacío.
- ⚠️ **Sun Bell**: la política dice que solo la publicidad saca datos del dispositivo. El repo ping-coin prevé Supabase (cuentas, fotos, medidas): antes de conectarlo hay que actualizar la política y añadir una URL de eliminación de cuenta.
- ⚠️ El paquete `com.sunbell.app` depende de una decisión aún abierta en ping-coin. Si cambia, hay que actualizar la política y mantener los alias.
- ⚠️ Solo en español: las fichas de Play en otros países necesitan, como mínimo, la política en inglés.
- ⚠️ Repo público a propósito: contiene el nombre completo y el correo del responsable, como exige el RGPD. No se han encontrado secretos ni claves. `gen.py` regenera exactamente los HTML versionados.

## 6. Historial de sesiones
| Fecha | Qué se hizo | % tras la sesión |
|---|---|---|
| 2026-09-22 | Creada plantilla vacía de inventario | — |
| 2026-09-22 | Análisis inicial y relleno del inventario | 60% |
