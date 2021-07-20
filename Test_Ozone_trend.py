#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 00:55:01 2021

@author: cmenares
"""


# Correr para datos
#runfile('/home/cmenares/Documentos/Dicotomo/Laura/ReadingDichotomus.py', wdir='/home/cmenares/Documentos/Dicotomo/Laura')


import pandas as pd
from __toolsTrend import *

df = pd.read_csv('Ozono_dmc_ebas.csv',index_col=0,parse_dates=True) 

def plot_m(pu , pu_m, titulo,color = 'black'):
        
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams['xtick.labelsize'] = 28
    plt.rcParams['ytick.labelsize'] = 28

    pu_m_aux  = pu_m.fillna(pu_m.mean())
    plt.figure(figsize=(27,13))
    ax = plt.subplot(1,1,1)
    
    plt.suptitle(titulo, fontsize=34)
    plt.plot(pu_m.index  , pu_m.values,'-o',color='black',linewidth=3.0,  markersize=2.5, label='Obs')
    
    plt.xlabel('Month',fontsize=28)
    plt.ylabel('O$_{3}$ $ppbv$',fontsize=28)
    plt.legend(loc='upper center',ncol=3,frameon=False, fontsize=24)
    
    plt.fill_between(pu_m.index, pu_m.resample('M').mean() , pu.resample('M').quantile(0.25),facecolor='gray', alpha=0.18) ;    
#    plt.fill_between(pu_m.index, pu_m.resample('M').mean() , pu.resample('M').quantile(0.05),facecolor='gray', alpha=0.18) ;    

    plt.fill_between(pu_m.index, pu.resample('M').mean()   , pu.resample('M').quantile(0.75),facecolor='gray', alpha=0.18) ;    
#    plt.fill_between(pu_m.index, pu.resample('M').mean()   , pu.resample('M').quantile(0.95),facecolor='gray', alpha=0.18) ;    
    
    # quantile(0.75)*(pu.PM25.resample('M').std()/len(pu.PM25.resample('M'))) intervalo de confianza
    plt.tight_layout()

    return

df_d = df.loc['1995':'2015']
df_m = df.resample('M').mean().loc['1995':'2015']


df_m.O3_ppbv[df_m.O3_ppbv<20] = np.nan
df_m = df_m.fillna(df_m.mean()) 

s    = df_m.O3_ppbv.values 
s_df = df_m.O3_ppbv


plot_m(df_d.O3_ppbv , df_m.O3_ppbv , 'Tololo' )

ax = plt.subplot(1,1,1)
plt.plot( s_df.index , linear_trend(s)[0],'-',color='blue',linewidth=2.4, label='Linear Regression')
plt.plot( s_df.index , emd_trend(s)[0],'-',color='r',linewidth=2.4, label='EMD Regression')
plt.plot( s_df.index , lamsal_trend(s)[0],'-',color='darkgray',markersize=2.4, label='Lamsal Regression')
plt.plot( s_df.index , stl_trend(s_df)[0],'-',color='green',markersize=2.4, label='STL LOEES Regression')
plt.plot( s_df.index , TheillSen_trend(s)[0],'-',color='darkorange',markersize=2.4, label='Theil Sen Regression')
plt.plot( s_df.index , cooper_trend(s)[0],'-',color='c',markersize=2.4, label='Cooper Regression')


plt.legend( bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                 borderaxespad=0, frameon=False,fontsize=22,ncol=7)



anchored_text = AnchoredText( "                         " + "${Decadal - Trends}$ " + " \n"  + 
                             "   $Linear$=" + str(round(linear_trend(s)[1]*12*10,1)) + '$ppbv $' +
                             '               $EMD$ = '+  str(round( emd_trend(s)[1]*12*10,1))    + '$ppbv$' +
                             '\n   $Lamsal$ = '+  str(round( lamsal_trend(s)[1]*12*10,1)) + '$ppbv$' +
                             '            $STL$ ='+  str(round( stl_trend(s_df)[1]*12*10,1))  + '$ppbv$' 
                             '\n $ThielSen$ = '+  str(round( TheillSen_trend(s)[1]*12*10,1)) + '$ppbv$' +  '    $Cooper$ = '+  str(round( cooper_trend(s)[1]*12*10,1)) + '$ppbv$' 

                             ,prop=dict(size=20), loc='upper center')
#anchored_text = AnchoredText( "r="+str(round(r,3))+"$\pm$"+ str(round(((1-r**2)/(len(real)-2))**0.5*10,3))+ "\n NPE$_t$=" + str(round(pe,3)),prop=dict(size=12), loc=1)

ax.add_artist(anchored_text)
plt.tight_layout()

plt.savefig('Trends.png',dpi = 300)