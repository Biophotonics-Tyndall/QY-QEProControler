import pandas as pd
import matplotlib.pyplot as pl

dataFolder = './data/'

bg = pd.read_csv(f'{dataFolder}dark_background_lab_lights_on.csv')
wl = pd.read_csv(f'{dataFolder}white_light.csv')
lp450 = pd.read_csv(f'{dataFolder}FELH0450.csv')
lp450T = pd.read_csv(f'{dataFolder}felh0450_transmission.csv')
sp500 = pd.read_csv(f'{dataFolder}FESH0500.csv')
sp500T = pd.read_csv(f'{dataFolder}fesh0500_transmission.csv')

# wl['intensities'] -= bg['intensities']
# lp450['intensities'] -= bg['intensities']
# sp500['intensities'] -= bg['intensities']

pl.plot(bg['wavelengths'], bg['intensities'], label='Dark')
pl.plot(wl['wavelengths'], wl['intensities'], label='White Light')
pl.plot(lp450['wavelengths'], lp450['intensities'], label='FELH0450')
pl.plot(sp500['wavelengths'], sp500['intensities'], label='FESH0500')
pl.legend()

pl.show()

pl.plot(lp450['wavelengths'], 100 * lp450['intensities'] / wl['intensities'], label='FELH0450')
pl.plot(lp450T['wavelengths'], lp450T['transmission'], label='FELH0450 from Thorlabs')
pl.legend()

pl.show()

pl.plot(sp500['wavelengths'], 100 * sp500['intensities'] / wl['intensities'], label='FESH0500')
pl.plot(sp500T['wavelengths'], sp500T['transmission'], label='FELH0500 from Thorlabs')

pl.legend()
pl.show()