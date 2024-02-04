# Introducción a Git y GitHub

## Tabla de Contenidos

1. [¿Qué es Git?][#seccion1]
2. [¿Por qué necesitamos Git?](#seccion2)
3. [¿Cómo funciona Git?](#seccion3)
4. [Configuración básica de Git](#seccion4)
5. [Conceptos básicos de Git](#seccion5)
6. [Comandos básicos de Git](#seccion6)
7. [¿Qué es GitHub?](#seccion7)
8. [¿Cómo funciona GitHub?](#seccion8)
9. [Creando una cuenta en GitHub](#seccion9)
10. [Creando un nuevo repositorio en GitHub](#seccion10)
11. [Clonando un repositorio de GitHub](#seccion11)
12. [Subiendo cambios a GitHub](#seccion12)
13. [GitHub Desktop](#seccion13)
14. [Referencias y recursos adicionales](#seccion14)

<a name="seccion1"></a>
## 1. ¿Qué es Git?

Git es un sistema de control de versiones distribuido gratuito y de código abierto diseñado para manejar todo, desde proyectos pequeños hasta muy grandes, con velocidad y eficiencia. Es fácil de aprender y tiene un rendimiento diminuto con operaciones de tipo lightning-fast. 

Git se creó por primera vez en 2005 por Linus Torvalds, el creador del sistema operativo Linux, con el objetivo de rastrear los cambios en el código fuente durante el desarrollo de software. Desde entonces, se ha convertido en el sistema de control de versiones más popular entre los desarrolladores.

<a name="seccion2"></a>
## 2. ¿Por qué necesitamos Git?

El desarrollo de software implica mucho más que simplemente escribir código. Implica el seguimiento de los cambios, la colaboración con otros desarrolladores, el pruebas de diferentes características y, a veces, el deshacer cambios que resultan ser una mala idea. Git nos ayuda con todas estas tareas y muchas más.

Git también es muy útil para los científicos de datos y los analistas de datos. Permite el seguimiento de los cambios en los conjuntos de datos, los modelos de aprendizaje automático, los notebooks de Jupyter, etc. Esto facilita enormemente la experimentación y la colaboración.

<a name="seccion3"></a>
## 3. ¿Cómo funciona Git?

Git rastrea y registra los cambios en los archivos en un directorio llamado repositorio. Cada vez que realizamos un cambio y lo registramos en Git, Git crea una instantánea del nuestros archivos y almacena una referencia a esa instantánea. Si los archivos no han cambiado, Git no almacena el archivo de nuevo, solo un enlace al archivo idéntico anterior que ya tiene almacenado.

<a name="seccion4"></a>
## 4. Configuración básica de Git

Antes de comenzar a usar Git, debes configurar tu nombre y dirección de correo electrónico. Git usa esta información para asociar commits con un identificador.

Abre una terminal y ejecuta los siguientes comandos:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@ejemplo.com"
```

<a name="seccion5"></a>
## 5. Conceptos básicos de Git

Antes de profundizar en los comandos de Git, aqui te dejo algunos conceptos básicos que debes conocer:

- **Repositorio**: Un repositorio es un contenedor para un proyecto que se está rastreando con Git. Contiene todos los archivos del proyecto, así como el historial completo de cambios.
- **Commit**: Un commit es una instantánea de nuestros archivos. Es esencialmente una "versión guardada" de nuestro código.
- **Branch**: Un branch es una versión paralela de un repositorio. Se utiliza para trabajar en diferentes versiones de un proyecto simultaneamente.
- **Staging Area**: El Staging Area es un lugar donde podemos agrupar nuestros cambios en archivos en preparación para un commit.

<a name="seccion6"></a>
## 6. Comandos básicos de Git

A continuación se presentan algunos de los comandos básicos que utilizaremos con más frecuencia al trabajar con Git. Si deseas una referencia más completa, consulta la [documentación oficial de Git](https://git-scm.com/doc).

- `git clone <url>`: Clona un repositorio de Git desde la URL especificada.
- `git pull`: Actualiza los cambios del repositorio en remoto en tu repositorio local.

- `git init`: Inicia un nuevo repositorio de Git.
- `git status`: Muestra el estado del repositorio actual.
- `git add <archivo>`: Agrega un archivo al staging area.
- `git commit -m "<mensaje>"`: Crea un nuevo commit con un mensaje descriptivo.
- `git push`: Sube los cambios al repositorio en remoto.
- `git log`: Muestra el historial de commits.
- `git branch <nombre>`: Crea un nuevo branch.
- `git checkout <nombre>`: Cambia al branch especificado.
- `git merge <nombre>`: Fusiona el branch especificado con el branch actual.


[Esquema](/img/git_schema.PNG)

<a name="seccion7"></a>
## 7. ¿Qué es GitHub?

GitHub es un servicio de alojamiento en la nube para repositorios de Git. Permite a los desarrolladores almacenar repositorios de Git de manera remota y ofrece muchas características que facilitan la colaboración en proyectos de código abierto y privados. GitHub proporciona una interfaz de usuario basada en web, así como integración con la línea de comandos de Git.

<a name="seccion8"></a>
## 8. ¿Cómo funciona GitHub?

Cuando trabajas con un repositorio de Git en tu máquina local (tu computadora), se llama repositorio local. Puedes subir este repositorio a GitHub, lo que te permite almacenarlo de manera remota. Este repositorio remoto en GitHub puede ser accesado y descargado por otros desarrolladores. Puede servir como una copia de seguridad de tu trabajo en caso de que algo le suceda a tu máquina local, y permite a otros colaborar en tu proyecto.

<a name="seccion9"></a>
## 9. Creando una cuenta en GitHub

Antes de poder utilizar GitHub, necesitas crear una cuenta. Aquí te dejo los pasos para hacerlo:

1. Ve a [GitHub](https://github.com/).
2. Haz clic en el botón verde "Sign up for GitHub".
3. Rellena el formulario de registro.
4. Verifica tu dirección de correo electrónico.

<a name="seccion10"></a>
## 10. Creando un nuevo repositorio en GitHub

Una vez que tienes una cuenta en GitHub, puedes crear repositorios para almacenar tus proyectos. Aquí te dejo los pasos para hacerlo:

1. Inicia sesión en GitHub.
2. Selecciona "New repository".
3. Rellena el nombre de tu repositorio, añade una descripción (opcional), elige si quieres que sea público o privado, y si quieres inicializarlo con un README.
4. Haz clic en "Create repository".

<a name="seccion11"></a>
## 11. Clonando un repositorio de GitHub

Para trabajar en un proyecto almacenado en GitHub, necesitas clonar el repositorio. Esto descargará una copia del repositorio en tu máquina local.

```bash
git clone <URL del repositorio>
```

<a name="seccion12"></a>
## 12. Subiendo cambios a GitHub

Cuando hayas hecho algunos cambios en tu repositorio local y quieras subirlos a GitHub, necesitarás añadir tus cambios (add), crear la instánea (commit) y subir esos cambios (push). Esto subirá tus cambios al repositorio remoto en GitHub.

```bash
git add .
git commit -m "mensaje"
git push 
```

En donde `<branch>` es el nombre del branch que quieres subir. Si estás trabajando en el branch principal, el comando sería `git push origin main`.

<a name="seccion13"></a>
## 13. GitHub Desktop

[GitHub Desktop](https://desktop.github.com/) permite simplificar la mayoría de estas tareas mediate una sencilla aplicación en tu escritorio.


<a name="seccion14"></a>
## 14. Referencias y recursos adicionales

- [Documentación oficial de Git](https://git-scm.com/doc)
- [Guía de GitHub para principiantes](https://guides.github.com/activities/hello-world/)
- [Tutorial interactivo de Git](https://learngitbranching.js.org/)

Espero que esta introducción te haya ayudado a entender qué es Git y GitHub y por qué son herramientas tan importantes para el desarrollo de software y la ciencia de datos. ¡Ahora estás listo para empezar a utilizar Git y GitHub en tus propios proyectos!

[#seccion1]: #seccion1