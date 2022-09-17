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

def getNeutralizingMass(equation, y_eq, x_eq, x_mol):
    sol = BCE.solutionCoefficients(equation)
    y_mass = x_mol * sol[y_eq] / sol[x_eq] * getMoles.getMolarMass(y_eq)
    return y_mass


if __name__ == '__main__':

    equation = 'NiCl2 + Ag(NO3) : AgCl + Ni(NO3)2'
    sample = ('AgNO3', 0.25)
    mass_obtained = ('AgCl', 0.0081)

    BCE.writeBCESteps(equation)
    print(findConcentrationFromPrecipitate(equation, sample, mass_obtained))