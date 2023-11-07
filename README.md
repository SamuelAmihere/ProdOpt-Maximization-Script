# Production Optimization Script

This Python script is designed to optimize the production of two products in a day, using a specific mathematical model. It utilizes mathematical optimization techniques to determine the best production quantities for maximum profitability. 

## Mathematical Formulation

Let's define the variables as follows:

- **x1**: Number of the first product produced in a day.
- **x2**: Number of the second product produced in a day.

The optimization model is as follows:

    max 70x1 + 900x2
    s.t. 3x1 +   5x2 <= 3600 (wood)
          x1 +   2x2 <= 1600 (labor)
        50x1 +  20x2 <= 48000 (machine)

          x1,x2      >= 0.


## Usage

The script can be run with the following command-line options:

```bash
python script_name.py --model [model_name]
    --model: The name of the chosen model.
    --products(prompt): Names of the products to produce, separated by a tab.
```

## Getting Started

To get started with this project, follow the steps below:

    Clone the repository: git clone https://github.com/username/ProdOpt-Maximization-Script.git
    Install the necessary dependencies: pip install -r requirements.txt
    Run the script with the specified options.

## Requirements

    Python 3
    Gurobi (Make sure it is installed and configured properly)

## Contributing

Contributions are always welcome! Please feel free to open an issue or submit a pull request for any changes or enhancements you'd like to make.