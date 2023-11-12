import pandas as pd
import matplotlib.pyplot as plt
import numpy as nd

def main ():
    ' EX 1'
    dfEstacions = pd.read_csv('2020_MeteoCat_Estacions.csv')
    dfDetall = pd.read_csv('2022_MeteoCat_Detall_Estacions.csv')
    dfDades = pd.read_csv('MeteoCat_Metadades.csv')
    ' Final EX1'
    ' Ex2'
    nyEstacions = dfEstacions.to_numpy()
    nyDetall = dfDetall.to_numpy()
    nyDades = dfDades.to_numpy()
    ' Final Ex2'
    ' Ex3'
    font1 = {'family':'serif','color':'blue','size':20}
    dfDetall["DATA_LECTURA"] = pd.to_datetime(dfDetall["DATA_LECTURA"])
    dfFiltrada = dfDetall.query("ACRÒNIM == 'TM' & ((DATA_LECTURA >= '2022-02-01')&(DATA_LECTURA <= '2022-02-28'))")
    estacions = dfFiltrada['CODI_ESTACIO'].unique()
    for estacion in estacions:
        dfEstacion = dfFiltrada.query("CODI_ESTACIO == '"+ estacion +"'")
        dfEstacion['DAY'] = dfEstacion['DATA_LECTURA'].dt.day
        plt.plot(dfEstacion['DAY'], dfEstacion['VALOR'], label = estacion)
        
    plt.ylabel("Temperatua ºC")
    plt.xlabel("Dias de febrero")
    plt.title("Temperatura de febrer", fontdict = font1)
    plt.legend()
    plt.show()
    for index,  estacion in enumerate( estacions):
        dfEstacion = dfFiltrada.query("CODI_ESTACIO == '"+ estacion +"'")
        plt.subplot(1,estacions.size, index+1)
        plt.title(estacion)
        dfEstacion['DAY'] = dfEstacion['DATA_LECTURA'].dt.day
        plt.plot(dfEstacion['DAY'], dfEstacion['VALOR'])
    plt.show()
    'Final ex3'
main()