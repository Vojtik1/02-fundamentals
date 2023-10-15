import physics

vyska = 25
hmotnost = 50
rychlost = 3
frekvence = 90
zdroj = 8
print("doba volného pádu ze zadané výšky na Zemi:",(physics.free_fall_time(vyska)))
print("doba volného pádu ze zadané výšky na Měsíci:",(physics.moon_free_fall_time(vyska)))
print("relativistická hmotnost objektu při dané rychlosti blízké rychlosti světla:",(physics.relativistic_mass(hmotnost,rychlost)))
print("Dopplerův jev pro změnu frekvence vlnění vzhledem k pohybu zdroje a pozorovatele:",(physics.doppler_effect(frekvence,rychlost,zdroj)))
