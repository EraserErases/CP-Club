'''
In this exercise you will create a program that reads a pressure from the user in kilo-
pascals. Once the pressure has been read your program should report the equivalent

pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
'''

pressure_kPa = float(input('Pressure in kilo-pascals: '))

pressure_PSI = pressureKP * 14.22

pressure_mmHg = pressureKP * 7.50062

pressure_atm = pressureatm * 0.0098692327

print(f'{pressure_kPa}kPa = {pressure_PSI}PSI = {pressure_mmHg}mmHg = {pressure_atm}atm')