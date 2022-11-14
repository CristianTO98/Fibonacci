import argparse

parser = argparse.ArgumentParser(
                    prog = 'Fibonacci',
                    description = 'Devuelve el resultado de ejecutar la función de fibonacci con argumento de entrada')

parser.add_argument('nth',type = int, help = "The n-term of the ....")           # positional argument



args = parser.parse_args()

print(args.nth)

