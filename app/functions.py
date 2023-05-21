from DSSATTools import (
    Crop, SoilProfile, WeatherData, WeatherStation,
    Management, DSSAT
)
import pandas as pd
from datetime import datetime, timedelta
import numpy as np


def dssat_computing(inp):
    # Random weather data
    endtime = datetime.strptime(inp['plant_date'], '%Y-%m-%d') + timedelta(days=10*365)
    endtime_str = endtime.strftime('%Y-%m-%d')
    starttime = datetime.strptime(inp['plant_date'], '%Y-%m-%d') - timedelta(days=1)
    starttime_str = endtime.strftime('%Y-%m-%d')
    DATES = pd.date_range(starttime, endtime_str)
    N = len(DATES)

    df = pd.DataFrame(
        {
        'tn': np.random.gamma(10, 1, N),
        'rad': np.random.gamma(10, 1.5, N),
        'prec': [0.0]* N,
        'rh': 100 * np.random.beta(1.5, 1.15, N),
        },
        index=DATES,
    )
    df['TMAX'] = df.tn + np.random.gamma(5., .5, N)

    # Create a WeatherData instance
    WTH_DATA = WeatherData(
        df,
        variables={
            'tn': 'TMIN', 'TMAX': 'TMAX',
            'prec': 'RAIN', 'rad': 'SRAD',
            'rh': 'RHUM'
        }
    )

    WTH_DATA['TMAX'][inp['plant_date']] = inp['tmax']
    WTH_DATA['TMIN'][inp['plant_date']] = inp['tmin']
    WTH_DATA['RAIN'][inp['plant_date']] = inp['rain']
    WTH_DATA['SRAD'][inp['plant_date']] = inp['srad']
    WTH_DATA['RHUM'][inp['plant_date']] = inp['rhum']

    # Create a WheaterStation instance
    wth = WeatherStation(
        WTH_DATA, 
        {'ELEV': 33, 'LAT': 0, 'LON': 0, 'INSI': 'dpoes'}
    )

    # Soil instance from default soil profile
    soil = SoilProfile(default_class=inp['soil'])

    # Crop
    crop = Crop(inp['plant'])
    # Check how the cultivar looks like
    cul = 'IB00'
    for i in range(1, 100):
        if i < 10:
            cult = cul + '0' + str(i)
        else:
            cult = cul + str(i)
        
        try:
            crop.cultivar[cult]
            break
        except:
            pass

    # Management instance
    man = Management(
        cultivar=cult,
        planting_date=DATES[1],
    )

    # Modify harvest to Automatic
    man.simulation_controls['HARVS'] = 'A'

    dssat = DSSAT()
    dssat.setup()
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )

    # Save the output
    output1 = dssat.output['PlantGro']
    
    oup = {
        'DAP': output1['DAP'][inp['harvest_date']],
        'GSTD': output1['GSTD'][inp['harvest_date']],
        'LAID': output1['LAID'][inp['harvest_date']],
        'SWAD': output1['SWAD'][inp['harvest_date']],
        'LWAD': output1['LWAD'][inp['harvest_date']],
        'GWAD': output1['GWAD'][inp['harvest_date']],
        'GAD': output1['G#AD'][inp['harvest_date']],
        'GWGD': output1['GWGD'][inp['harvest_date']],
        'HIAD': output1['HIAD'][inp['harvest_date']],
        'CWAD': output1['CWAD'][inp['harvest_date']],
    }

    dssat.close()

    return oup
