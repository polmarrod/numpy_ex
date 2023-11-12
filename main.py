import pandas as pd
import matplotlib.pyplot as plt
import numpy as nd



def main ():
    # ' EX 1'
    dfEstacions = pd.read_csv('2020_MeteoCat_Estacions.csv')
    dfDetall = pd.read_csv('2022_MeteoCat_Detall_Estacions.csv')
    dfDades = pd.read_csv('MeteoCat_Metadades.csv')
    dfDetall["DATA_LECTURA"] = pd.to_datetime(dfDetall["DATA_LECTURA"])
    # ' Final EX1'
    # ' Ex2'
    nyEstacions = dfEstacions.to_numpy()
    nyDetall = dfDetall.to_numpy()
    nyDades = dfDades.to_numpy()
    # ' Final Ex2'
    # ' Ex3'
    font1 = {'family':'serif','color':'blue','size':20}
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
    # 'Final ex3'
    # 'Ex 4'
    dfDetall['MES'] = dfDetall['DATA_LECTURA'].dt.month
    dfDetall['DAY'] = dfDetall['DATA_LECTURA'].dt.day
    dfFebrero = dfDetall[(dfDetall['MES'] == 2) & (dfDetall['ACRÒNIM'] == 'TM')]
    # print(dfFebrero) para pruebas
    valDia = dfFebrero.groupby(['MES', 'DAY'])['VALOR'].median().reset_index()
    # print(valDia) para mas pruebas xd
    plt.hist(valDia['VALOR'], bins=range(0, 26, 1))
    plt.title('Histograma de Temperatura per a Febrer de 2022')
    plt.xlabel('Temperatura')
    plt.ylabel('Dias')
    plt.show()
    mean_temp = valDia['VALOR']
    std_temp = valDia['VALOR'].std()
    predicted_temps = nd.random.normal(loc=mean_temp, scale=std_temp, size=28)
    predicted_temps = nd.round(predicted_temps).astype(int)
    # print(predicted_temps)  mas pruebas jejeje
    'Final EX 4'
    'Ex 5'
    dfDetall['MES'] = dfDetall['DATA_LECTURA'].dt.month
    dfDetall['DAY'] = dfDetall['DATA_LECTURA'].dt.day
    dfFebreroLluvia = dfDetall[(dfDetall['MES'] == 2) & (dfDetall['ACRÒNIM'] == 'PPT')]
    print(dfFebreroLluvia)
    valDia = dfFebreroLluvia.groupby(['MES', 'DAY'])['VALOR'].mean().reset_index()
    media_lluvia = valDia['VALOR'].mean()
    desviacion_lluvia = valDia['VALOR'].std()
    dfFebreroLluvia['VALOR'] = nd.random.normal(loc=media_lluvia, scale=desviacion_lluvia, size=len(dfFebreroLluvia))
    dfFebreroLluvia['VALOR'] = dfFebreroLluvia['VALOR'].clip(lower=0)
    dfFebreroLluvia['Lluvia'] = dfFebreroLluvia['VALOR'] > 1
    proporcion_lluvia = dfFebreroLluvia['Lluvia'].value_counts(normalize=True)
    plt.figure(figsize=(8, 8))
    plt.pie(proporcion_lluvia, labels=proporcion_lluvia.index,)
    plt.title('Proporción de días con lluvia febrero23')
    plt.show()
    dfFebreroLluvia['Lluvia'].value_counts().plot(kind='bar')
    plt.title('Días con lluvia y sin lluvia en febrero de 2023')
    plt.xlabel('Lluvia')
    plt.ylabel('Número de días')
    plt.xticks([0, 1], ['Sin lluvia', 'Con lluvia'], rotation=0)
    plt.show()
    'Final ex 5'
main()