# Production Optimization Script


This Python script is designed to optimize the production of some products in a day, using a specific mathematical model. It utilizes mathematical optimization techniques to determine the best production quantities for maximum profitability. 

## Mathematical Formulation

Let's define the variables as follows:

- **x1**: Number of the first product produced in a day.
- **x2**: Number of the second product produced in a day.
...

The optimization model is as follows:

    max Σi,j cixj

    s.t. Σij AiXj = resources
                xj >= 0 for all i,j={0, 1,...n-1}.

## Usage

The script can be run with the following command-line options:

bash
```
./script_name.py --model [model_name]

    --model: The name of the chosen model.
    --products(prompt): Names of the products to produce, separated by a tab.
```
windows
```
python script_name.py --model [model_name]

    --model: The name of the chosen model.
    --products(prompt): Names of the products to produce, separated by a tab.
```

## Getting Started

To get started with this project, follow the steps below:

    Clone the repository: git clone https://github.com/SamuelAmihere/ProdOpt-Maximization-Script.git
    Install the necessary dependencies: pip install -r requirements.txt
    Run the script with the specified options.

## Requirements

    Python 3.7.9+
    Gurobi (Make sure it is installed and configured properly)

## Contributing

Contributions are always welcome! Please feel free to open an issue or submit a pull request for any changes or enhancements you'd like to make.