# project euler

Mis soluciones a los ejercicios planteados en [projecteuler.net], programados
en [Python].

Cuando tengo tiempo, intento resolver algunos ejercicios, nunca miro
soluciones, y aplico la filosofía del proyecto: "...there is a fine line
between researching ideas and using the answer you found on another website..."
intentando siempre tener una idea propia, o una intuición e intentar encontrar
soluciones posibles. Nunca buscar la solución directa.

## Perfil en Project Euler

![profile]

## Cómo está organizado el repositorio

En las carpetas `solutions_XXXX-XXXX` se encuentran las soluciones a los
problemas ya resueltos, tengo algunas lagunas, ejercicios que tengo resueltos
y no tengo el código fuente.

Por otra parte, tengo empezados algunos otros, que se encuentran en el
directorio `drafts_0001-9999`, no funcionan y a veces únicamente son ideas
vagas.

## Una librería sencilla: mymaths.py 

En `lib/mymaths.py` incluyo algunas funciones típicas que estoy usando mucho:

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

Para poder hacer uso de las funciones:

```python
lib_path = os.path.abspath('../../lib')
sys.path.append(lib_path)

import mymaths
```

## Repositorio antiguo

Anteriormente el repositorio estaba en [Bitbucket] como privado, ya que no
quería que nadie hiciera trampas, eso fue hace casi 4 años. Hoy en día hay
suficientes repositorios en GitHub con las soluciones que no tiene sentido no
publicar ya mi repositorio.

## Licencia

Todo el código bajo la [licencia MIT][license]

[projecteuler.net]:https://projecteuler.net
[Python]:https://www.python.org
[Bitbucket]:https://bitbucket.org
[profile]:https://projecteuler.net/profile/pnicolas.png
[license]:LICENSE
