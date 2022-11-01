
from functools import reduce

def main():
    elementosImpares = filter(lambda x: x % 2 != 0, [1,2,3,4,5,6,7,8,9,10])
    sumaElementos = reduce(lambda x, y : x + y, elementosImpares)
    print(sumaElementos)

if __name__ == "__main__":
    main()