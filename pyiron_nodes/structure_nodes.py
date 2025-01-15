from pyiron_workflow import as_function_node, as_macro_node, as_dataclass_node
from typing import Optional

@as_function_node
def CreateStructure(pr, element:str, bravais_lattice: Optional[str], a: Optional[float|int], c: Optional[float|int] = None, cubic:bool = False):
    """
    pr: pyiron_atomistics project
    bravais_lattice: e.g., "bcc" or "fcc" or "hcp"
    a: lattice constant in Angstrom
    c: height of hexagonal prism in Angstrom
    cubic: returns conventional unit cell instead of primitive for cubic structures (not to be used for non-cubic)
    """

    from pyiron_atomistics import Project
    
    pr = pr
    if bravais_lattice != 'hcp' and c == None:
        structure = pr.create.structure.bulk(element, crystalstructure=bravais_lattice, cubic=cubic, a=a)
    elif bravais_lattice == 'hcp' and c == None:
        structure = pr.create.structure.bulk(element, crystalstructure=bravais_lattice, cubic=cubic, a=a)
    else:
        structure = pr.create.structure.bulk(element, crystalstructure=bravais_lattice, cubic=cubic, a=a, c=c)
    
    return structure

@as_function_node("repeated_structure")
def RepeatStructure(structure, repetition_x: int, repetition_y: int, repetition_z: int):
    """
    structure: ase object from pyiron_atomistics
    """

    return structure.repeat([repetition_x, repetition_y, repetition_z])

@as_function_node("view")
def VisualizeStructure(structure):
    """
    structure: ase object from pyiron_atomistics
    """
    
    return structure.plot3d()

@as_function_node("vacancy_structure")
def CreateVacancies(structure, indices: Optional[str|list[int]] = '0'):
    """
    indices: list of atoms to be removed, can be a list of integers (indices) or a string with spaces between indices e.g., '0 4 8'
    structure: ase object from pyiron_atomistics
    """

    if isinstance(indices, str):
        indices = [int(i) for i in indices.split()]
        
    del structure[indices]
    
    return structure

@as_function_node("substitute_structure")
def SubstituteAtoms(structure, substitute_species: str, subsitute_magmom:Optional[int|float], indices: Optional[str|list[int]] = '0'):
    """
    indices: list of atoms to be removed, can be a list of integers (indices) or a string with spaces between indices e.g., '0 4 8'
    structure: ase object from pyiron_atomistics
    """

    if isinstance(indices, str):
        indices = [int(i) for i in indices.split()]
        
    for i in indices:
        structure[i] = substitute_species
        structure[i].magmom = subsitute_magmom
    
    return structure
