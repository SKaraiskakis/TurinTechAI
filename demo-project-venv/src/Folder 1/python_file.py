# print("savvas")

# def add(a,b):
#     return a+b
# x=add(5,6)
# print(x)

# from evoml_dataset_api.dataset_api import Dataset

#d = Dataset()

# d.get_datasets(source="uci", task="time series", quantity=2)
# df.head(d)
import pkg_resources

package_name = 'evoml-dataset-api'

def is_package_installed(package_name):
    try:
        dist = pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

if is_package_installed(package_name):
    print(f"The package '{package_name}' is installed.")
else:
    print(f"The package '{package_name}' is not installed.")
import ast

def get_imported_packages(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())

    imported_packages = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_packages.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            imported_packages.add(node.module.split('.')[0])

    return imported_packages

file_path = '/home/savvas/demo-project/demo-project-venv/src/python_file.py'
imported_packages = get_imported_packages(file_path)

print("Imported packages:")
for package in imported_packages:
    print(package)


from evoml_dataset_api.dataset_api import Dataset


d = Dataset()

d.get_datasets(task="regression", quantity=2)

data = d.get_dataset(dataset_name="credit-g")