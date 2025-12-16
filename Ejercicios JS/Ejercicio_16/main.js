import usuarios from "./datos.js";
import { filtrarMayores } from "./filtros.js";

const mayores = filtrarMayores(usuarios);
console.log("Usuarios mayores de 18 años:");
console.table(mayores);
