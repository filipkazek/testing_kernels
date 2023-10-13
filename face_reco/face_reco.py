import spiceypy
import datetime
import math
spiceypy.furnsh(r"C:\Users\filip\Desktop\face_reco\_kernels\lsk\naif0012.tls")
spiceypy.furnsh(r"C:\Users\filip\Desktop\face_reco\_kernels\spk\de432s.bsp")
spiceypy.furnsh(r"C:\Users\filip\Desktop\face_reco\_kernels\pck\gm_de431.tpc")
today = datetime.datetime.today()
today=today.strftime('%Y-%m-%dT00:00:00')

et_today=spiceypy.utc2et(today)
earth_wrt_sun, earth_sun_lt = spiceypy.spkgeo(targ=399,  et=et_today, ref='ECLIPJ2000', obs=10)
print('State vector of earth:',  earth_wrt_sun)  

dist = math.sqrt(earth_wrt_sun[0]**2+earth_wrt_sun[1]**2+earth_wrt_sun[2]**2)
distAU=spiceypy.convrt(dist,'km','AU')
print("Distance from sun to earth in AU: ", distAU)

orbit_speed= math.sqrt(earth_wrt_sun[3]**2 + earth_wrt_sun[4]**2 + earth_wrt_sun[5]**2)
print("Orbital speed: ", orbit_speed)


    



