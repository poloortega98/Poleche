
factor_milla_km=1.60934
factor_km_milla=1/factor_milla_km

print("Si quieres convertir millas a kilometros, escribe \"gelatina\" \nSi quieres convertir kilometros a millas, escribe \"chorlito\"")
valor_a_convertir = input("8==D  ")

if valor_a_convertir == "gelatina":
    entrada = input("Introduce el valor en millas: ").replace(",", ".")
    millas = float(entrada)
    km = millas * factor_milla_km
    decimales= int(input("¿Cuantos decimales quieres carnal?   "))

    formato=f"{{:.{decimales}f}}"
    km_formateado = formato.format(km)

    print(f"Aqui tiene su valor convertido estimadisimo usuario: {millas} millas son {km_formateado} kilometros")
    
elif valor_a_convertir == "chorlito":
    entrada = input("Introduce el valor en kilometros: ").replace(",", ".")
    km = float(entrada)
    millas = km * factor_km_milla
    decimales= int(input("¿Cuantos decimales quieres carnal?   "))

    formato=f"{{:.{decimales}f}}"
    millas_formateadas = formato.format(millas)

    print(f"Aqui tiene su valor convertido amigo usuario: {millas_formateadas} millas")

else:
    print("DIJE QUE ESCRIBIERAS GELATINA O CHORLITO, NO QUE ME HICIERAS UN ENSALADILLA DE FRUTAS, MALDITO CRETINO")

volver_a_jugar = input("¿Quieres volver a convertir algo señorite usuarie? (si/no)")
while volver_a_jugar == "si":
    print("Si quieres convertir millas a kilometros, escribe \"gelatina\" \nSi quieres convertir kilometros a millas, escribe \"chorlito\"")
    valor_a_convertir = input("8==D  ")

    if valor_a_convertir == "gelatina":
        entrada = input("Introduce el valor en millas: ").replace(",", ".")
        millas = float(entrada)
        km = millas * factor_milla_km
        decimales= int(input("¿Cuantos decimales quieres carnal?   "))

        formato=f"{{:.{decimales}f}}"
        km_formateado = formato.format(km)

        print(f"Aqui tiene su valor convertido estimadisimo usuario: {millas} millas son {km_formateado} kilometros")
        
    elif valor_a_convertir == "chorlito":
        entrada = input("Introduce el valor en kilometros: ").replace(",", ".")
        km = float(entrada)
        millas = km * factor_km_milla
        decimales= int(input("¿Cuantos decimales quieres carnal?   "))

        formato=f"{{:.{decimales}f}}"
        millas_formateadas = formato.format(millas)

        print(f"Aqui tiene su valor convertido amigo usuario: {millas_formateadas} millas")

    else:
        print("DIJE QUE ESCRIBIERAS GELATINA O CHORLITO, NO QUE ME HICIERAS UN ENSALADILLA DE FRUTAS, MALDITO CRETINO")

    volver_a_jugar = input("¿Quieres volver a convertir algo señorite usuarie? (si/no)")

print("Que bueno porque llevo convirtiendo malditas unidades de distancia desde mi natalicio y estoy a una conversion mas de volverme chango")