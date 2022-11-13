# author: Piotr Waksmundzki
# script let us in simple and quick way change names of files in indicated folder 
import os

os.chdir(r"C:\Users\Piotr Waksmndzki\Obrazy\photos_01_06_22")
print(os.getcwd())

for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "Pieniny_Mountains_Trip" + str(count).zfill(3)

    new_name = f'{f_name}{f_ext}'

    os.rename(f, new_name)