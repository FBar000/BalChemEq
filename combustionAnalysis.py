from unicodedata import decimal
from getMoles import *
from methods import *
import numpy as np
import sigFigCounter as sfc


def moles(atom, term, t_mass): 
    """
    Get the moles of an atom in a compound of a given mass.

    Arguments:
        atom (string) The symbol of the atom to be counted.
        term (string) The formula for the compound to count from.
        t_mass (float) The mass of the compound to count from.
    Return:
        moles_of_atom (float) The moles of the atom present in the compound.
    """
    return t_mass / getMolarMass(term) * count(atom, (term, 1))

def check(raw_number): 
    """
    Returns true if float is within 10^-3 of an integer. False otherwise.

    Arguments: 
        raw_number (dnarray type=float) An array of floating point number.
    """
    return np.all(abs(raw_number.round() - raw_number) < 0.001)


# A dictionary with {cmpd: mass}; "X" is unknown compound
unknown_compound_mass = 1.50
product_information = {"CO2": 4.72,
                        "H2O": 1.93}

# A dictionary of the present atoms
atoms = findAtoms("".join(product_information.keys()))
atoms.remove("O")
print(atoms)

# A dict with {atom: moles}
info = {}
for atm in atoms:
    tmp = 0
    for term, mass in product_information.items():
        tmp_2 = moles(atm, term, mass)
        tmp += np.round(tmp_2, decimals=sfc.find_sigfigs(mass))
    info[atm] = tmp

print(info)
# Find Moles Oxygen
tmp = 0
for atom, mole in info.items():
    tmp += np.round(mole * getMolarMass(atom), decimals=sfc.find_sigfigs(mole))
print(f"tmp: {tmp}")
print(f"sigfigs: {sfc.find_sigfigs(mole)}")
info["O"] = (unknown_compound_mass - tmp) / getMolarMass("O")
print(info)

info_vector = np.fromiter([unknown_compound_mass] + list(info.values()), dtype=float)
info_vector = info_vector / np.amin(info_vector)
print(info_vector)

while not check(info_vector):
    info_vector += info_vector

print(info_vector)