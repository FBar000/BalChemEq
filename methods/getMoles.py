
from re import sub
import mendeleev
# from methods import *
from constructSystemMatrix import *


def getMolarMass(base_substance, target_substance=''):
    """
    Get grams of target_substance per mole of substance_formula. 
    
    target_substance defaults to substance_formula,
    
    Argument:
        base_substance (string) the formual of the chemical substance
        target_substance (string) a subset of the substance formula
    Return:
        const (float) grams of target_substance per mole of substance_foruma
    """
    # Default to molar mass
    if target_substance == '':
        target_substance = base_substance
    const = 0
    L =  findAtoms(target_substance)
    for a in L:
        print(a)
        print(count(a, (base_substance, 1)))
        # print(count(a, (base_substance, 1)) * mendeleev.element(a).atomic_weight)
        const += count(a, (base_substance, 1)) * mendeleev.element(a).atomic_weight
    return const


def massToMoles(substance_formula, mass):
    """
    Returns the moles of the substance.

    Arguments:
        substance_formula (string) A chemical formula (molecular formula)
        mass (float) The mass (in grams) of the substance
    Returns:
        moles (float) The moles of the element 
    """
    const =  getMolarMass(substance_formula)
    moles = mass / const
    return moles


def molesToMass(substance_formula, moles):
    """
    Returns the moles of the substance.

    Arguments:
        substance_formula (string) A chemical formula (molecular formula)
        mass (float) The moles of the substance
    Returns:
        moles (float) The moles of the element 
    """
    const = getMolarMass(substance_formula)
    moles = moles * const
    return moles


def massToMolarity(substance_formula, mass, volume):
    """
    Get molarity of a solution from the dissolved substance's mass and volume

    Arguments:
        substance_formula (string) Solute
        mass (string) Mass of solute
        volume (float) Volume of solvent
    """
    return massToMoles(substance_formula, mass) / volume

def molarityToMass(substance_formula, moles, volume):
    """
    Inverse of massToMolarity
    """
    return volume * molesToMass(substance_formula, moles)


def percentMass(base_substance, target_substance):
    """
    Percent mass target_substance of base_substance

    Argument:
        base_substance (string) the formual of the chemical substance
        target_substance (string) a subset of the substance formula
    Return:
        (float) percent mass
    """
    mass_part = getMolarMass(base_substance, target_substance)
    mass_whole = getMolarMass(base_substance)
    return mass_part / mass_whole


def massCompToMoleComp(mass_composition):
    """
    Return a dictionary with the moles of each element in a compound of 100g.

    Arg:
        mass_composition (dict) A mapping between elements and their percentage in the compound
    """
    mole_comp = {}
    for key in mass_composition:
        mole_comp[key] = 100 * mass_composition[key] / getMolarMass(key)
    return mole_comp

if __name__ == '__main__':

    print(getMolarMass("C2H3Cl"))
    # print(7 / 2 * 35.00 / getMolarMass("C2H3Cl"))