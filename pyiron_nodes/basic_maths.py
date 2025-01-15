from pyiron_workflow import as_function_node, as_macro_node, as_dataclass_node
from typing import Optional

@as_function_node("sum")
def Addition(variable1:Optional[int|float], variable2:Optional[int|float]) -> int|float:
    sum_ = variable1 + variable2
    return sum_

@as_function_node("difference")
def Subtraction(variable1, variable2:Optional[int|float]) -> int|float:
    diff = variable1 - variable2
    return diff

@as_function_node("product")
def Multiplication(variable1, variable2:Optional[int|float]) -> int|float:
    prod = variable1 * variable2
    return prod

@as_function_node("quotient")
def Division(variable1, variable2:Optional[int|float]) -> int|float:
    qnt = variable1 / variable2
    return qnt

@as_function_node("result")
def EquationNode(equation: str, a:Optional[int|float] = 0, b:Optional[int|float] = 0, c:Optional[int|float] = 0, d:Optional[int|float] = 0, e:Optional[int|float] = 0, f:Optional[int|float] = 0) -> int|float:
    """
    Equation: enter an equation with up to 6 variables, can include numpy (as np)
    a,b,c,d,e,f: the variables in the equation
    """

    import numpy as np

    result = eval(equation)
    
    return result
