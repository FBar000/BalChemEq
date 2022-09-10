import itertools
from json.encoder import INFINITY
from re import sub
import mendeleev
# from methods import *
from methods import *
import BCE
from sigFigsClass import *

def getMolarMass(base_substance, target_substance=''):
    """
    Get grams of target_substance per mole of substance_formula. 
    
    target_substance defaults to substance_formula,
    
    Argument:
        base_substance (string): the formual of the chemical substance
        target_substance (string): a subset of the substance formula
    Return:
        const (sfFloat): grams of target_substance per mole of substance_foruma
    """
    # Default to molar mass
    if target_substance == '':
        target_substance = base_substance
    const = 0
    List =  findAtoms(target_substance)
    for atom in List:
        amount_of_atom = count(atom, (base_substance, 1))
        atomic_weight = sfFloat(mendeleev.element(atom).atomic_weight)
        const += sfFloat(amount_of_atom * atomic_weight)
    return const


def massToMoles(substance_formula, mass):
    """
    Returns the moles of the substance.

    Arguments:
        substance_formula (string): A chemical formula (molecular formula)
        mass (sfFloat): The mass (in grams) of the substance
    Returns:
        moles (sfFloat): The moles of the element 
    """
    moles = sfFloat(mass) / getMolarMass(substance_formula)
    return moles


def molesToMass(substance_formula, moles):
    """
    Returns the moles of the substance.

    Arguments:
        substance_formula (string): A chemical formula (molecular formula)
        mass (sfFloat): The moles of the substance
    Returns:
        moles (sfFloat): The moles of the element 
    """
    moles = sfFloat(moles) * getMolarMass(substance_formula)
    return moles


def massToMolarity(substance_formula, mass, volume):
    """
    Get molarity of a solution from the dissolved substance's mass and volume

    Arguments:
        substance_formula (string): Solute formula
        mass (string): Mass of solute
        volume (float): Volume of solvent
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
        base_substance (string): the formual of the chemical substance
        target_substance (string): a subset of the substance formula
    Return:
        (float): percent mass
    """
    mass_part = getMolarMass(base_substance, target_substance)
    mass_whole = getMolarMass(base_substance)
    return mass_part / mass_whole


def massCompToMoleComp(mass_composition):
    """
    Return a dictionary with the moles of each element in a compound of 100g.

    Arg:
        mass_composition (dict): A mapping between elements and their percentage in the compound
    Returns
        mole_comp (dict): a dict with the percent mole composition of each element
    """
    mole_comp = {}
    mole_total = 0
    for key in mass_composition:
        tmp = 100 * mass_composition[key] / getMolarMass(key)
        mole_comp[key] = tmp
        mole_total += tmp
    for key in mass_composition:
        mole_comp[key] /= mole_total
    return mole_comp

def moleRatio(term1, term2, chemicalEquationSolution):
    """
    Compute the ratio of moles of term1 to term2 in the equation whose solution is given.

    (E.g. The ratio of H2 to O2 in "2 H2 + O2 : H2O" is 2 / 1)

    Arg:
        term1 (string): A term in the chemical equation.
        term2 (string): A term in the chemical equation.
        chemicalEquationSolution (dict) A dictionary with the solution to a chemical equation.
    Returns:
        ratio (float): The ratio of term1 to term2 in the reaction described by the solution
    """
    return chemicalEquationSolution[term1] / chemicalEquationSolution[term2]

def productsFromMoles(equation, reactant_amounts):
    """
    Compute the moles of the products produced in a chemical reaction.

    Arguments:
        equation (string): An equation that represents the chemical reaction.
        reactant_amounts (dict): A dictionary with the amount (moles) of each reactant.
    Return 
        product_amounts (dict): A dictionary with the amount (moles) of each product.
    """
    # Solve chemical equation
    coef = BCE.solutionCoefficients(equation)
    # Find limiting reactant
    react_amt = len(reactant_amounts)
    react_terms = list(reactant_amounts.keys())[:react_amt]
    lim_reagent, moles = react_terms[0], reactant_amounts[react_terms[0]]
    for key in react_terms[1:]:
        mole_equivalence = reactant_amounts[key] * moleRatio(lim_reagent, key, coef)
        if mole_equivalence < moles:
            lim_reagent = key
            moles = reactant_amounts[key]
    # Get product keys
    coef = BCE.solutionCoefficients(equation)
    prod_key = list(coef.keys())[react_amt:]
    # Get moles of product
    product_amounts = {}
    for key in prod_key:
        product_amounts[key] = moles * moleRatio(key, lim_reagent, coef)
    return product_amounts
        
def productsFromMass(equation, reactant_amounts):
    """
    Compute the mass of the products produced in a chemical reaction.

    Arguments:
        equation (string): An equation that represents the chemical reaction.
        reactant_amounts (dict): A dictionary with the amount (grams) of each reactant.
    Return 
        product_amounts (dict): A dictionary with the amount (grams) of each product.
    """
    reactant_moles = {}
    for key, value in reactant_amounts.items():
        reactant_moles[key] = massToMoles(key, value)
    solution_moles = productsFromMoles(equation, reactant_moles)
    for key, value in solution_moles.items():
        solution_moles[key] = molesToMass(key, value)
    return solution_moles
    
def reactantsFromMoles(equation, product_amounts):
    """
    Compute the moles of the reactants required for a specific amount of a product.

    Arguments:
        equation (string): An equation that represents the chemical reaction.
        product_amounts (dict): A dictionary with the amount (moles) of a reactant.
    Return 
        reactant_amounts (dict): A dictionary with the amount (moles) of each product.
    """
    # Solve chemical equation
    coef = BCE.solutionCoefficients(equation)
    # Find limiting product
    prod_amt = len(product_amounts)
    prod_terms = list(reversed(list(product_amounts.keys())))[:prod_amt]
    lim_reagent, moles = prod_terms[0], product_amounts[prod_terms[0]]
    for key in prod_terms[1:]:
        mole_equivalence = product_amounts[key] * moleRatio(lim_reagent, key, coef)
        if mole_equivalence < moles:
            lim_reagent = key
            moles = product_amounts[key]
    # Get reactant keys
    coef = BCE.solutionCoefficients(equation)
    prod_key = list(reversed(list(coef.keys())))[prod_amt:]
    # Get moles of product
    reactant_amount = {}
    for key in prod_key:
        reactant_amount[key] = moles * moleRatio(key, lim_reagent, coef)
    return reactant_amount