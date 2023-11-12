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
    dfDetall["DATA_LECTURA"] = pd.to_datetime(dfDetall["DATA_LECTURA"])
    dfFiltrada = dfDetall.query("'ACRÒNIM' == 'TM' & (('DATA_LECTURA' >= '2022-02-01')&('DATA_LECTURA' <= '2022-02-28'))")
    plt.plot(dfFiltrada['DATA_LECTURA'], dfFiltrada['VALORS'])
    plt.show
main()