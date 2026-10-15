# Modelos 3D opcionales

Si pones aquí estos archivos `.glb`, las páginas los usan en lugar de los personajes hechos a mano:

| Archivo        | Página               | Personaje |
|----------------|----------------------|-----------|
| `rapunzel.glb` | `home/isa.html`      | Rapunzel corriendo en el pasto |
| `eugene.glb`   | `inicio/pedida.html` | Eugene persiguiendo a Maximus |
| `pascal.glb`   | `inicio/pedida.html` | Pascal en las enredaderas |

- El modelo debe mirar hacia +Z y estar de pie (como los de Mixamo / Sketchfab).
- Si trae animaciones, se usa la que se llame "run"/"correr"; si no, "walk"; si no, la primera.
- El tamaño se ajusta solo.
- Los archivos locales solo cargan con un servidor: `python3 -m http.server` en la carpeta del proyecto.
