#!/usr/bin/env python3
"""
Modeling Product manufacturing.
Let
    x1 = number of desksd producedin a day and
    x2 = number of tables produced in a day.

The formulation of this example is
    max Σi,j cixj

    s.t. Σij=0 AiXj = resources
                xj >= 0 for all i,j={0, 1,...n-1}.

"""


from gurobipy import *

def build_model(name:str, prodNames:[str], prices:[], res_consumption:[[]], res_limit:[])->Model:
    """Builds model.

    Args:
        res_consumption[number]: Resources consumed by each product. E.g. [10, 4, 5,...].

        res_limit[number]: Maximum number of various resources available.\n
                            E.g. [500, 140, 300,...].
    """
    products = range(len(prices))
    resources = range(len(res_limit))
    # initialize model
    model = Model(name)
    # Set decision variables
    x = []
    for prod in products:
        x.append(model.addVar(lb = 0,
                        vtype = GRB.CONTINUOUS,
                        name = prodNames[prod]))
    # Set Object Function
    model.setObjective(quicksum(prices[i] * x[i] for i in products),
                       GRB.MAXIMIZE)
    # Set Constraints
    model.addConstrs((quicksum(res_consumption[j][i] * x[i] for i in products)
                       <= res_limit[j] for j in resources), "Resource_limitation")
    
    return (model)

def getSolutions(models:[])->{float:{str:float}}:
    """Solves and returns optimal solution.

    Args:
        model[Model]: The model to optimize\n
                      and find optimal solution.
    """
    # Optimize the model
    solutions = {}
    for model in models:
        model.optimize()
        x = {}
        for var in model.getVars():
            x[var.varName] = var.x
        solutions[model.objVal] = x
    return (solutions)

def print_solutions(prices, resources_consumption,
                    resources_limit, products:[str],
                    model:str)->None:
    """Prints solutions of a model.

        Args:
            prices[]: List of product prices.

            resources_consumption[[]]: nxm array of resources consumed\n
                            by each product n = number of resource type\n
                            m = number of products.
            products: List of products to produce.

            model: Model's name
    """

    if len(products) != len(prices):
        print("You can't model for {:d} product{}".format(len(products),
                '' if len(products) < 2 else 's'))
        print("Based on your data, you must enter {:d} product{}.".format(len(prices),
                '' if len(prices) < 2 else 's'))
        exit(1)
    eg1 = build_model(model,products, prices, resources_consumption, resources_limit)
    modelSolutions = getSolutions([eg1])

    print("\n======================")
    for obj, sol in modelSolutions.items():
        for x, xval in sol.items():
            print('{} = {:.2f}'.format(x, xval))
        print(f'Total Profit = {obj:.2f}')