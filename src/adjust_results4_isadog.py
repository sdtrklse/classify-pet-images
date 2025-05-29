def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to include information about whether
    the pet image and classifier label are of a dog.
    
    Parameters:
        results_dic (dict): Dictionary with image filenames as keys and a list
            containing pet label and classifier label as values.
        dogfile (str): Path to the file containing dog names, one per line.
    
    Returns:
        None: The function modifies the results_dic in place.
    """
    
    # Create a dictionary to store all dog names
    dognames_dic = dict()
    
    # Read dog names from dogfile and store them in a dictionary
    with open(dogfile) as file:
        
        for line in file:
            dogname = line.rstrip()
            
            # Check for duplicate dog names in the file
            if dogname in dognames_dic:
                print(f"Warning: Duplicate dog name '{dogname}' found in {dogfile}")
            else:
                dognames_dic[dogname] = 1
    
    # Add is-a-dog information to the results dictionary
    for filename, results in zip(results_dic.keys(), results_dic.values()):
        pet_label, classifier_label = results[0], results[1]
        results_dic[filename].extend(
            [
                1 if pet_label in dognames_dic else 0,
                1 if classifier_label in dognames_dic else 0
            ]
        )
