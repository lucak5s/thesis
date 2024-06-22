from runtime_comparison.planar_graphic_linear import planar_graphic_linear_comparison
from runtime_comparison.uniform_partition_gammoid_linear import uniform_partition_gammoid_linear_comparison
import csv
import os
import itertools

def round_values(data_dict):
    rounded_dict = {}
    for key, values in data_dict.items():
        rounded_dict[key] = [round(value, 3) for value in values]
    return rounded_dict
  
  
def dict_to_csv(data_dict, filename):
    folder_path = 'results'
    os.makedirs(folder_path, exist_ok=True)
    path = os.path.join(folder_path, filename)
    
    data_dict = round_values(data_dict)
    headers = data_dict.keys()
    rows = itertools.zip_longest(*data_dict.values(), fillvalue=None)

    with open(path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        csvwriter.writerows(rows)


def csv_planar_graphic_linear_comparision(groundset_sizes, density_type, filename):
  runtimes = planar_graphic_linear_comparison(groundset_sizes, density_type=density_type)
  runtimes['ground_set_sizes'] = groundset_sizes
  dict_to_csv(runtimes, filename)


def csv_uniform_partition_gammoid_linear_comparison(groundset_sizes, k_ratio, filename):
  runtimes = uniform_partition_gammoid_linear_comparison(groundset_sizes, k_ratio)
  runtimes['ground_set_sizes'] = groundset_sizes
  runtimes['linear_ground_set_sizes'] = groundset_sizes[:len(runtimes['linear_runtimes'])]
  dict_to_csv(runtimes, filename)


### Planar - Graphic - Linear ###

csv_planar_graphic_linear_comparision([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 150, 190, 240], 'sparse', 'v_e.csv')
csv_planar_graphic_linear_comparision([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 150, 190, 240], 'semi-dense', 'v_2e.csv')
csv_planar_graphic_linear_comparision([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 150, 190, 240], 'dense', 'v_3e.csv')

### Uniform - Partition - Gammoid - Linear ###

csv_uniform_partition_gammoid_linear_comparison([10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 60, 70, 80, 90], 'low-k', 'k_01n.csv')
csv_uniform_partition_gammoid_linear_comparison([10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 60, 70, 80, 90], 'mid-k', 'k_05n.csv')
csv_uniform_partition_gammoid_linear_comparison([10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 60, 70, 80, 90], 'high-k', 'k_09n.csv')