# %%

import math
import random

# %%
# sqrt é a raiz quadrada de um numero, importando da biblioteca math
math.sqrt(49)

# %%
# retorna valor de pi importando da biblioteca math
math.pi

# %%
# retorna o numeral e
math.e

# %%
# uso recomendado
from math import pi, e

print(pi)
print(e)

# %%

# importando tudo da biblioteca, não recomendado, pode subscrever funções de outras libs
from math import *

sqrt(49)

# %%

# importando math com alias, sendo um apelido para ela
import math as mt

print(mt.sqrt(67))
