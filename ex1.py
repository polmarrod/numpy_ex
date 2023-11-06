import pandas as pd
import matplotlib as plt
import numpy as nd

def main ():
    dfEstacions = pd.read_csv('2020_MeteoCat_Estacions.csv')
    dfDetall = pd.read_csv('2022_MeteoCat_Detall_Estacions.csv')
    dfDades = pd.read_csv('MeteoCat_Metadades.csv')
    nyEstacions = dfEstacions.to_numpy()
    nyDetall = dfDetall.to_numpy()
    nyDades = dfDades.to_numpy()
    filtro_acronimo = (nyEstacions[:, 19] == "TM")
    nyEstacionsFiltered = nyEstacions[filtro_acronimo]
main()