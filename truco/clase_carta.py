"""
Clase Carta para juegos de cartas
"""

class Carta:
    def __init__(self, numero, palo):
        self._numero = numero
        self._palo = palo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        if type(value) != int:
            raise Exception('Solo están permitidos numeros')
        self._numero = value

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, value):
        self._palo = value

    def __str__(self):
        return f'{self.numero} de {self.palo}'

    def __add__(self, otro):
        p1 = self._numero if self._numero < 10 else 0
        p2 = otro.numero if otro.numero < 10 else 0
        # if p1 >= 10:
        #     p1 = 0
        # if p2 >= 10:
        #     p2 = 0

        if self._palo == otro.palo:
            return p1 + p2 + 20
        else:
            return max([p1, p2])

    def envido(self, carta2, carta3):
        p1 = self.palo
        p2 = carta2.palo
        p3 = carta3.palo
        n1 = self.numero if self._numero < 10 else 0
        n2 = carta2.numero if carta2._numero < 10 else 0
        n3 = carta3.numero if carta3._numero < 10 else 0
        # mano = [self, carta2, carta3]

        if p1 == p2 and p1 == p3:
            print('No se juega con flor')
            return 0
        elif p1 == p2:
            return n1 + n2 + 20
        elif p1 == p3:
            return n1 + n3 + 20
        elif p2 == p3:
            return n2 + n3 + 20
        else:
            return max(n1, n2, n3)

            


# Pruebas

carta1 = Carta(7, 'espada')
carta2 = Carta(6, 'espada')
carta3 = Carta(3, 'oro')

carta4 = Carta(12, 'espada')
carta5 = Carta(7, 'espada')
carta6 = Carta(10, 'oro')

carta7 = Carta(5, 'espada')
carta8 = Carta(4, 'espada')
carta9 = Carta(3, 'espada')

assert carta1.envido(carta2, carta3) == 33
assert carta4.envido(carta5, carta6) == 27
assert carta7.envido(carta8, carta9) == 0

print('OK')