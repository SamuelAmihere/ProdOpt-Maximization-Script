#!/usr/bin/env python3
"""Script to perform optimization of production of\n
    some products in a day.

Modeling and Application.\n
Let
    x1 = number of first product produced in a day and\n
    x2 = number of second product produced in a day.

The formulation of this example is\n
    max 70x1 + 900x2\n
    s.t. 3x1 +   5x2 <= 3600 (wood)\n
          x1 +   2x2 <= 1600 (labor)\n
        50x1 +  20x2 <= 48000 (machine)\n

          x1,x2      >= 0.
"""

import click
from models.gurobi.products_model import (print_solutions)
from utils.data import load_json_data


@click.command()
@click.option('--products', prompt="products (separated by tab)",
              help='names of products to produce')
@click.option('--model', default='eg1',
              help='names of modele')
@click.option('--data_src', default='products.json',
              help='Source of data')
def consoleApp(products:str, model:str, data_src)->None:
    """Finds optimal solutions for products.
    
        Args:
            products: Products obtained from the command prompt.

            model: Model name entered as an option at the terminal.
    """
    # -----------------Data-------------------------
    data = load_json_data(data_src)
    
    if data == None:
        print("No data for the model!")
        exit(1)
    products = [i.strip() for i in products.strip().split(" ")]
    data['products'] = products
    data['model'] = model
    
    # ----------------Model---------------------------
    print_solutions(**data)

if __name__ == '__main__':
    
    consoleApp()
