# Trends_Tools
Herramientas de python para calcular tendencias de series de tiempo no estacionarias

Desarrollado por Camilo Menares, Enero de 2021
Revisado por Laura Gallardo (lgallard at u.uchile.cl)

Estas rutinas van dirigidas al cálculo de tendencias con diferentes métodos descritos en la literatura científica para series no-lineales/no-estacionarias.

Los archivos:

**__toolsTrend.py** : Contiene las rutinas para el cálculo de tendencias en series de tiempo mensuales mediante los métodos:

1) EMD, Empirical Mode Decomposition. Ref. Huang & Wu, 2008 (doi:10.1029/2007RG000228); Wu & Huang, 2009 (doi:10.1142/S1793536909000047)
2) Lamsal, Descomposición en armónicos, lineal y ruido. Ref. Lamsal et al, 2015 (doi:10.1016/j.atmosenv.2015.03.055)
3) STL, Seasonal Trend decomposition based on Loess. Ref. Cleveland et al, 1990, Journal of Oficial Statistics 6, 3-73 (http://www.nniiem.ru/file/news/2016/stl-statistical-model.pdf)
4) Thiel-Sen, . Ref. Sen, 1960 (https://doi.org/10.1177/0008068319600101)
5) Cooper, Tropospheric Ozone Assessment Report (TOAR) method:  locally weighted regression (or lowess, or loess smoother). Ref. Cooper et al. 2020 (https://doi.org/10.1525/elementa.420); Cleveland, 1979 (https://doi.org/10.1080/01621459.1979.10481038); Cleveland & Devlin, 1988 (https://doi.org/10.1080/01621459.1988.10478639)
6) Regresión Lineal. Basado en https://scikit-learn.org/stable/modules/linear_model.html, Ordinary Least Squares

---------------------------
**Test_Ozone_trend.py** : Esta rutina permite aplicar los métodos antes indicados a una serie mensual de observaciones de ozono registradas en Tololo (30S, 70W, 2200 m snm). Los datos están razón de mezcla molar (ppbv). Dichos datos fueron obtenidos desde: http://ebas.nilu.no/Pages/DataSetList.aspx?key=8E72FB7960CB456A90B1191ED9FED899

--------------------------
**requirements.txt** : Establece las versiones de librerías python utilizadas necesarias para _toolsTrend.py.

Estas rutinas funcionan sobre las siguientes librerías de python:
1) pandas (https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
2) numpy (https://numpy.org/install/)
3) scipy (https://www.scipy.org/install.html)
4) EMD-signal (https://pyemd.readthedocs.io/en/latest/intro.html)
--------------------------

## Test
La rutina Test_Ozone_trend.py devuelve la siguiente imagen:

![Trends](https://user-images.githubusercontent.com/69597135/126395011-95095516-031d-4ef6-94ad-4ab1f4d2048f.png)

Donde son indicada en diferentes cololres las regresiones calculadas por el modulo, y en color negro las observacion de Ozono realizada en Tololo.
