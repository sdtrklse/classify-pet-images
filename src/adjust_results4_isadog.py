from typing import Dict, List, Union


def adjust_results4_isadog(
    results_dic: Dict[str, List[Union[str, int]]], 
    dogfile: str
) -> None:
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images "as a dog" or "not a dog" especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    
    Parameters:
        results_dic (Dict[str, List[Union[str, int]]]): Dictionary with "key" as image
            filename and "value" as a list. Where the list will contain the following items:
                index 0 = pet image label (string)
                index 1 = classifier label (string)
                index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 and index 4 are added by this function -----
                NEW - index 3 = 1/0 (int)  where 1 = pet image "is-a" dog and 
                    0 = pet image "is-NOT-a" dog
                NEW - index 4 = 1/0 (int)  where 1 = classifier classifies image
                    "as-a" dog and 0 = classifier classifies image "as-NOT-a" dog
        dogfile (str): A text file that contains names of all dogs from the classifier
            function and dog names from the pet image files. This file has
            one dog name per line dog names are all in lowercase with
            spaces separating the distinct words of the dog name. Dog names
            from the classifier function can be a string of dog names separated
            by commas when a particular breed of dog has multiple dog names
            associated with that breed (ex. maltese dog, maltese terrier,
            maltese) (string - indicates text file's filename).
    
    Returns:
        None - results_dic is mutable data type so no return needed.
    """
    
    # Create a dictionary to store all dog names
    dognames_dic: Dict[str, int] = dict()

    # Read dog names from dogfile and store them in a dictionary
    with open(dogfile) as f:
        
        for line in f:
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
