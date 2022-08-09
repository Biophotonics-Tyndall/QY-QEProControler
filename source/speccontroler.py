from seabreeze.spectrometers import Spectrometer
import pandas as pd
import matplotlib.pyplot as pl
from time import sleep

class Controler:
    _integrationTime = 100000 # default integration time

    def __init__(self) -> None:
        self.spec = Spectrometer.from_first_available()
        self.data = pd.DataFrame(columns=['wavelengths', 'intensities'])
        self.integrationTime = 100000 # 0.1s
        print(self.spec)

    @property
    def integrationTime(self):
        intT = self._integrationTime / 1000000
        return f'{intT:.2f} s'

    @integrationTime.setter
    def integrationTime(self, t:int):
        assert (type(t) is int) and (t > 1000), 'integration time must be an integer between 1000 to ....' 
        oldT = self._integrationTime
        self._integrationTime = t
        self.spec.integration_time_micros(self._integrationTime)
        sleep(oldT / 1e6) 

    def acquire(self) -> None:
        """
        Args:
            intTime (int): Integration time in microseconds. 
            Stadard value set to 100000 us equivalent to 0.1s
        """
        sleep(2 * self._integrationTime / 1e6)
        self.data['wavelengths'] = self.spec.wavelengths()
        self.data['intensities'] = self.spec.intensities()

    def plot(self) -> None:
        fig, ax = pl.subplots()
        ax.plot(self.data['wavelengths'], self.data['intensities'])
        fig.show()

    def save(self, filename) -> None:
        self.data.to_csv(f'./data/{filename}.csv')

