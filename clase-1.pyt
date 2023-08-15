def calcular_monto_final(ahorros, tasa_interes, años):
    monto_final = ahorros * (1 + tasa_interes / 100) ** años
    return monto_final

def main():
    try:
        ahorros = float(input("Ingresa el monto de tus ahorros: "))
        tasa_interes = float(input("Ingresa la tasa de interés anual (%): "))
        años = int(input("Ingresa el número de años: "))
        
        monto_final = calcular_monto_final(ahorros, tasa_interes, años)
        
        print("Después de {} años, tus ahorros de ${:.2f} crecerán a ${:.2f} con una tasa de interés del {}%.".format(años, ahorros, monto_final, tasa_interes))
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()