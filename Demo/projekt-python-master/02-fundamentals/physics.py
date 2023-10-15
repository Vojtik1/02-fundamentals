'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.6525 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu


def free_fall_time(height):
    """
    Vypočítá dobu volného pádu ze zadané výšky na Zemi.

    :param height: Výška ze které padá objekt (v metrech)
    :return: Doba volného pádu (v sekundách)
    """
    time = (2 * height / EARTH_GRAVITY) ** 0.5
    return time


def moon_free_fall_time(height):
    """
    Vypočítá dobu volného pádu ze zadané výšky na Měsíci.

    :param height: Výška ze které padá objekt (v metrech)
    :return: Doba volného pádu na Měsíci (v sekundách)
    """
    time = (2 * height / MOON_GRAVITY) ** 0.5
    return time


def relativistic_mass(mass, velocity):
    """
    Vypočítá relativistickou hmotnost objektu při dané rychlosti blízké rychlosti světla.

    :param mass: Hmotnost objektu (v kilogramech)
    :param velocity: Rychlost objektu (v metrech za sekundu)
    :return: Relativistická hmotnost objektu (v kilogramech)
    """
    relativistic_mass = mass / ((1 - (velocity ** 2 / SPEED_OF_LIGHT ** 2)) ** 0.5)
    return relativistic_mass


def doppler_effect(frequency, velocity, source_velocity):
    """
    Vypočítá Dopplerův jev pro změnu frekvence vlnění vzhledem k pohybu zdroje a pozorovatele.

    :param frequency: Původní frekvence vlnění (v Hz)
    :param velocity: Rychlost pozorovatele (v metrech za sekundu)
    :param source_velocity: Rychlost zdroje (v metrech za sekundu)
    :return: Nová frekvence vlnění (v Hz)
    """
    observed_frequency = frequency * ((SPEED_OF_SOUND + velocity) / (SPEED_OF_SOUND + source_velocity))
    return observed_frequency



''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''