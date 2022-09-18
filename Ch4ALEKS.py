import BCE
import getMoles 


def findConcentrationFromPrecipitate(equation, sample, mass_obtained):
    """
    Find the molarity (g / L) of a sample given the mass of precipitate formed in a reaction.

    Arguments:
        equation (str): The unbalanced chemical equation
        sample (tuple): A tuple containing the formula of the solute and the volume of solution (L)
        mass_obtained (tuple): A tuple containing the symbol for the precipitate and its mass (g)
    Return:
        molarity (float): The molarity (g / L) of the sample
    """
    target_substance = sample[0]
    sol = BCE.solutionCoefficients(equation)
    target_mass = (
                getMoles.massToMoles(mass_obtained[0], mass_obtained[1]) * 
                sol[target_substance] / sol[mass_obtained[0]] * 
                getMoles.getMolarMass(target_substance)
                )
    molarity = target_mass / sample[1]
    return molarity

def getNeutralizingMass(equation, target, present):
    """
    Find the mass of a base/acid needed to neutralize an acid/base.

    Arguments:
        equation (str): The unbalanced chemical equation for the neutralization reaction.
        target (str): The formula for the acid/base to find.
        present (tuple): A tuple containing the formula and moles of the base/acid present.
    Return:
        y_mass (float): The mass g required to neutralize x.
    
    
    """
    x_eq = present[0]
    x_mol = present[1]
    sol = BCE.solutionCoefficients(equation)
    y_mass = x_mol * sol[target] / sol[x_eq] * getMoles.getMolarMass(target)
    return y_mass

def getTitrantVolume(equation, analyte, titrant):
    """
    Get the volume of a titrant required to neutralize the analyte.

    Arguments:
        equation (str): Unbalanced chemical equation.
        analyte (tuple): Formula and mass (g) of the analyte.
        titrant (tuple): Formula and molarity of the titrant.

    Return:
        titrant_volume (float): The volume of the titrant (L).
    """
    sols = BCE.solutionCoefficients(equation)
    titrant_volume = getMoles.massToMoles(analyte[0],analyte[1]) * sols[titrant[0]] / sols[analyte[0]] * (1 / titrant[1])
    return titrant_volume

if __name__ == '__main__':
    
    eq = "I2"