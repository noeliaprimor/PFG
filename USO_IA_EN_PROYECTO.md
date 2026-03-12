# Uso de IA en el Proyecto (Enfoque Academico y Tecnico)

## 1. Objetivo del documento
Este documento define el marco de uso de Inteligencia Artificial (IA) en el proyecto PFG, con criterios de rigor academico, validez tecnica y transparencia metodologica.

Se establecen:
- el alcance real de la asistencia con IA,
- los controles de calidad aplicados,
- la trazabilidad de los cambios,
- y los limites de uso para preservar la autoria y revision humana.

## 2. Alcance del uso de IA
La IA se utiliza como herramienta de apoyo en tareas de:
- redaccion tecnica y mejora de claridad didactica,
- propuesta de preguntas de autoevaluacion,
- refactorizacion de texto y normalizacion editorial,
- soporte en tareas repetitivas de maquetacion HTML/Markdown.

## 3. Exclusiones (decisiones no delegadas)
La IA no reemplaza:
- la validacion final del contenido docente,
- la revision tecnica final del codigo,
- la aprobacion academica de objetivos, prerequisitos y evaluacion,
- la responsabilidad autoral del equipo humano.

## 4. Metodologia de trabajo con IA
Se adopta un flujo de trabajo en 5 fases:

1. **Planteamiento del problema**
   - Definicion de alcance, contexto y restricciones.
2. **Generacion asistida**
   - Obtencion de propuesta inicial (texto, preguntas, estilo o codigo).
3. **Revision experta humana**
   - Verificacion de exactitud tecnica y coherencia pedagogica.
4. **Ajuste contextual**
   - Adaptacion al temario, nivel del alumnado y estilo del proyecto.
5. **Validacion final**
   - Comprobacion funcional y editorial antes de publicar.

## 5. Criterios de calidad academica
Para cualquier salida generada con apoyo de IA se exige:
- alineacion con resultados de aprendizaje del tema,
- coherencia con el contenido de las lecciones,
- lenguaje adecuado al nivel formativo,
- ausencia de contradicciones conceptuales,
- trazabilidad de la decision final.

## 6. Criterios de calidad tecnica
En cambios sobre web y autoevaluacion:
- consistencia entre `data-module-id` y `js/questions-data.json`,
- validacion de rutas y navegacion entre indices/lecciones,
- verificacion de carga de componentes (`partials/autoevaluacion.html`),
- comprobacion de comportamiento de correccion y reseteo.

## 7. Control especifico de preguntas de autoevaluacion
Cada pregunta debe cumplir:
- correspondencia directa con contenidos impartidos,
- una unica respuesta correcta,
- distractores plausibles,
- nivel de dificultad progresivo,
- cobertura equilibrada del tema.

En preguntas con codigo, se verifica ademas:
- validez sintactica basica,
- uso correcto del concepto evaluado,
- legibilidad del ejemplo para aprendizaje.

## 8. Riesgos y mitigaciones
### Riesgo 1: contenido tecnicamente plausible pero incorrecto
**Mitigacion:** revision tecnica obligatoria por persona responsable.

### Riesgo 2: desalineacion entre preguntas y lecciones
**Mitigacion:** contraste sistematico contra los ficheros de leccion del tema.

### Riesgo 3: deriva de estilo entre archivos
**Mitigacion:** guia editorial y segunda pasada de homogeneizacion.

### Riesgo 4: sobredependencia de IA
**Mitigacion:** la decision final siempre es humana y documentada.

## 9. Trazabilidad y auditoria de cambios
Para cada cambio asistido por IA se recomienda registrar:
- fecha,
- archivo modificado,
- descripcion del cambio,
- tipo de asistencia IA (redaccion, preguntas, codigo, revision),
- persona responsable de validacion final.

Plantilla sugerida:

```text
Fecha: YYYY-MM-DD
Archivo: ruta/archivo
Cambio: descripcion breve
Asistencia IA: si/no + tipo
Valida: nombre y rol
```

## 10. Gobernanza y uso responsable
Principios adoptados:
- **Transparencia:** documentar donde se ha usado IA.
- **Supervision humana:** no publicar sin revision.
- **Proporcionalidad:** usar IA donde aporta valor real.
- **Responsabilidad:** autoria y validacion final humanas.

## 11. Reproducibilidad y mantenimiento
Para facilitar continuidad del proyecto:
- mantener este documento actualizado por iteracion,
- conservar historial de cambios en archivos de documentacion,
- evitar introducir preguntas sin mapearlas al contenido del tema,
- revisar periodicamente validez tecnica de ejemplos y nomenclatura.

## 12. Conclusiones
El uso de IA en este proyecto se enmarca como asistencia tecnica y editorial controlada, no como sustitucion del criterio academico.

La calidad final depende de:
- verificacion humana,
- trazabilidad,
- y alineacion estricta con los objetivos formativos.
