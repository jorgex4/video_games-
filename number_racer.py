from random import randint

#***COMANDO PARA EJECUTAR EL JUEGO***: python number_racer.py

#VDefinir numero de jugadores
def validar_jugadores(jugadores):
  while not 2 <= jugadores <= 4:
    jugadores = int(input("Ingrese la cantidad de jugadores (2-4): "))
  return jugadores

#Definir niveles con su respectivo puntaje
def seleccionar_nivel():
  niveles = {
    "1": 20,
    "2": 30,
    "3": 50,
    "4": 100,
  }
  #Validar Niveles 
  while True:
    nivel = input("Seleccione el nivel de tablero (1-4): ")
    if nivel in niveles:
      return niveles[nivel]
    else:
      print("Nivel inválido. Ingrese una opción válida (1-4)")
      
#Lanzar 2 dados del 1 al 6
def lanzar_dados():
  dado1 = randint(1, 6)
  dado2 = randint(1, 6)
  return dado1, dado2

#Condicion para pares consecutivos
def pares_consecutivos(tiradas):
  if len(tiradas) < 3:
    return False
  for i in range(len(tiradas) - 2):
    if tiradas[i] == tiradas[i + 1] == tiradas[i + 2]:
      return True
  return False

def mover_jugador(posicion, tirada):
  return posicion + tirada

def carrera_numerica():
  # Pedir cantidad de jugadores
  jugadores = validar_jugadores(int(input("Ingrese la cantidad de jugadores (2-4): ")))

  # Seleccionar nivel de tablero
  meta = seleccionar_nivel()

  # Inicializar variables
  posiciones = [0] * jugadores
  tiradas_anteriores = [[] for _ in range(jugadores)]
  turno = 0

  # Bucle principal del juego
  while True:
    # Mostrar turno actual
    print(f"\nTurno del jugador {turno + 1}")

    # Lanzar dados y obtener tirada
    dado1, dado2 = lanzar_dados()
    tirada = dado1 + dado2
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Tirada total: {tirada}")

    # Registrar tirada
    tiradas_anteriores[turno].append(tirada)

    # Mover jugador
    posiciones[turno] = mover_jugador(posiciones[turno], tirada)
    print(f"Posición actual: {posiciones[turno]}")

    # Revisar si el jugador ha ganado
    if posiciones[turno] >= meta:
      print(f"\n¡El jugador {turno + 1} ha ganado!")
      break

    # Revisar si hay 3 pares consecutivos
    if pares_consecutivos(tiradas_anteriores[turno]):
      print(f"\n¡El jugador {turno + 1} ha ganado con 3 pares consecutivos!")
      break

    # Cambiar de turno segun el numero de jugadores
    turno = (turno + 1) % jugadores

if __name__ == "__main__":
  carrera_numerica()
