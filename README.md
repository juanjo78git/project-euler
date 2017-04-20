# PROJECT EULER

Mis soluciones a los ejercicios planteados en [projecteuler.net], programados
en [Python].

Cuando tengo tiempo, intento resolver algunos ejercicios, nunca miro
soluciones, y aplico la filosofía del proyecto: "*...there is a fine line
between researching ideas and using the answer you found on another
website...*" intentando siempre tener una idea propia, o una intuición
y luego explorar a partir de ese primer punto.
Nunca buscar la solución directa.

## Los inicios

Era 2008 y en la empresa donde trabajaba nos dejaron mucho tiempo para
formarnos libremente en diferentes tecnologías o lenguajes. Di con
[projecteuler.net] y empecé a programar con Python. Aunque el repositorio nació
en 2012 las primeras soluciones datan de ese primer año.

## Perfil en Project Euler

![profile]

## Cómo instalar el repositorio

Se requiere:

 * Python3

Se instala:

```Shell
git clone https://github.com/penicolas/project-euler.git
cd project-euler
$ pip install -e .  # para desarrollo
# O
$ pip install .
# Sin instalar
$ python -m projecteuler.projecteuler
```

# Cómo ejecutar los problemas

Fácil, ahora que está todo pasado a un ejecutable unitario:

```
usage: projecteuler [-h] -p PROBLEM [-b] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -p PROBLEM, --problem PROBLEM
                        Problem from projecteuler.net
  -b, --batch-mode      Batch mode
  -v, --version         show program's version number and exit
```

Ejemplo:

```Shell
$ projecteuler -p 1
1;233168;0:00:00
# Ejemplo modo batch
$ projecteuler -p 26 -b
26;983;0:00:00.410004
27;-59231;0:00:09.025092
28;669171001;0:00:00
29;9183;0:00:00.930009
30;443839;0:00:05.681058
31;73682;0:00:14.262147
32;45228;0:00:00.510005
...
```

## Cómo está organizado el repositorio

En las carpetas `projecteuler\problems` se encuentran las soluciones a los
problemas ya resueltos. Por otra parte, tengo empezados algunos otros, que se
encuentran marcados como XXXX_draft, no funcionan y a veces únicamente son
ideas vagas.


## Tiempos

Para ver en detalle los tiempos de cada uno de los problemas:

 * [Tiempos]

Algunos son desastrosos...


## Una librería sencilla: mymaths.py 

En `mymaths.py` incluyo algunas funciones típicas que estoy usando mucho:

**funciones**
- `ispalindrome(n)`
- `isprime(n)`
- `ispythagoreantriplet(a, b, c)`
- `numdivs(n)`

**generadores**
- `factorial(x)`
- `fibonacci()`
- `prime()`
- `trianglenumber()`

Etc.

## Repositorio antiguo

Anteriormente el repositorio estaba en [Bitbucket] como privado, ya que no
quería que nadie hiciera trampas, eso fue en [2012]. Hoy en día hay
suficientes repositorios en GitHub con las soluciones que no tiene sentido no
publicar mi repositorio.

## Licencia

Todo el código bajo la [licencia MIT][license]

[projecteuler.net]:https://projecteuler.net
[Python]:https://www.python.org
[Bitbucket]:https://bitbucket.org
[profile]:https://projecteuler.net/profile/pnicolas.png
[license]:LICENSE
[Tiempos]:TIME.md
[2012]:https://github.com/penicolas/project-euler/commit/bdd064ab688d16a17ec19976ced31fcf0b9fb38a
