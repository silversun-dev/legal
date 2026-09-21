# ⚠️ Esta app lleva publicidad. Que los papeles lo digan.

> Aviso permanente. No lo borres aunque hoy la app no tenga anuncios todavía.

---

## La regla, en una línea

**Decir que hay anuncios y no tenerlos es inofensivo. Decir que no los hay y
tenerlos es el problema.**

Por eso en ninguna app de Liquid Sun se escribe «no muestra publicidad» ni «no
recopila datos» si la publicidad va a llegar. No se gana nada con esa frase y
obliga a acordarse de volver justo el día que menos tiempo hay.

## Por qué esto muerde, y en qué orden

**Google Play es el riesgo real.** Play cruza tres cosas: lo que dice tu
política de privacidad, lo que rellenaste en el formulario de Seguridad de los
datos, y lo que sus escáneres encuentran dentro del APK. El SDK de AdMob y el
acceso al identificador de publicidad **se detectan automáticamente**. Si el
escáner ve AdMob y tu ficha dice «no se recogen datos», salta la incoherencia:
te rechazan la actualización o te suspenden la ficha hasta corregirlo, y la
reincidencia escala a la cuenta de desarrollador.

**El consentimiento en la UE es un requisito aparte.** Mostrar anuncios en
Europa sin el formulario UMP de Google incumple, diga lo que diga tu política.

**La AEPD es la cola larga.** Requiere que alguien reclame. Para una app
gratuita de un desarrollador individual, lo típico de una primera reclamación
por transparencia es un apercibimiento y una orden de corregir. Aun así hay una
diferencia que sí pesa: informar de menos es un defecto, **afirmar algo falso
es otra cosa**.

## Los cuatro sitios que tienen que decir lo mismo

Cuando esta app muestre anuncios, estos cuatro tienen que estar alineados. Si
uno se queda atrás, es el que te delata:

| # | Dónde | Qué tiene que decir |
|---|---|---|
| 1 | Política de privacidad en el repo `legal` | Que hay publicidad de AdMob y que se usa el identificador de publicidad |
| 2 | Formulario de Seguridad de los datos de Play | Recoge «Identificadores del dispositivo» y «Actividad en la aplicación», se comparten con Google, para publicidad |
| 3 | Clasificación de contenido + casilla de la ficha | «Contiene anuncios»: Sí |
| 4 | Textos dentro de la propia app | Que se financia con publicidad |

## El orden, que no es indiferente

La página web es instantánea; la revisión de Play tarda días. Aprovecha esa
diferencia:

1. **La política va primero.** Puede ir por delante: describe el tratamiento
   previsto. No pasa nada por publicarla unos días antes.
2. **El formulario y el APK van juntos**, el mismo día. El formulario describe
   lo que hace la versión que está publicada *ahora*, ni antes ni después.

## Lo que ya prometiste por escrito

Las políticas del repo `legal` dicen, en «Cambios en esta política»:

> «Si una versión futura de la aplicación trata datos de otra forma, esta
> página se actualizará **antes** de publicar esa versión, y la fecha del
> encabezado lo reflejará.»

El procedimiento correcto ya está escrito y publicado con tu nombre debajo. Lo
que faltaba era algo que lo recordara cuando toca. Esto es ese algo.

## Antes de cada subida

Ningún script puede leer la Play Console.
Estas dos las miras tú, a mano, cada vez:

- [ ] ¿El APK lleva SDK de publicidad? → entonces la política y el formulario
      tienen que decirlo
- [ ] ¿Hay usuarios en la UE? → entonces el mensaje de consentimiento UMP tiene
      que estar creado en AdMob **y aparecer de verdad** al abrir la app

---

*Tener publicidad no es ningún problema: monetizar con anuncios es legítimo y
lo hace todo el mundo. Lo único que hay que cuidar es que el papel diga lo
mismo que hace la app.*
