// Retorna solo usuarios con mayoría de edad
export function filtrarMayores(usuarios) {
    if (!Array.isArray(usuarios)) {
      throw new TypeError("filtrarMayores espera un arreglo de usuarios");
    }
    return usuarios.filter(
      (u) => u && typeof u.edad === "number" && u.edad >= 18
    );
  }
  