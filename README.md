# Trends_Tools
Herramienta de python para generar tendencias en serie no estacionarios

Estas rutinas van dirigidas al calculo de tendencias con diferentes tecnicas descritas en la documentacion cientifica para series no-lineales/no-estacionarias.
Los archivos:

**__toolsTrend.py** : Contiene las rutines para el calculo de tendencias en serie mensuales, mediante las tecnicas de EMD, Lamsal, STL. Thiel Sen, Cooper y Regresion Lineal. 

**Test_Ozone_trend.py** : Contie

**requirements.txt** : Contiene las versiones necesarias para las librerias utilizadas en este modulo.ne un test para las rutines de tendencias calculada sobre la serie historica de Ozone medido en ppbv en la estacion de tololo.

Estas rutinas funciona en base a las siguientes librerias de python:

pandas (https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

numpy (https://numpy.org/install/)

scipy (https://www.scipy.org/install.html)

EMD-signal (https://pyemd.readthedocs.io/en/latest/intro.html)
