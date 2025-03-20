from typing import Dict, List, Union

def calculates_results_stats(
    results_dic: Dict[str, List[Union[str, int]]]
) -> Dict[str, Union[int, float]]:
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the "best" model for classifying images.

    Parameters:
        results_dic (Dict[str, List[Union[str, int]]]): Dictionary with key as image
            filename and value as a list
                index 0 = pet image label (string)
                index 1 = classifier label (string)
                index 2 = 1/0 (int)  where 1 = match between pet image and
                        classifer labels and 0 = no match between labels
                index 3 = 1/0 (int)  where 1 = pet image "is-a" dog and
                        0 = pet image "is-NOT-a" dog
                index 4 = 1/0 (int)  where 1 = classifier classifies image
                        "as-a" dog and 0 = classifier classifies image
                        "as-NOT-a" dog
    
    Returns:
        Dict[str, Union[int, float]]: Dictionary that contains the results statistics (either
            a percentage or a count) where the key is the statistic's name (starting
            with "pct" for percentage or "n" for count) and the value is the
            statistic's value.
    """

    results_stats_dic = dict()

    # Number of images classified
    results_stats_dic["n_images"] = len(results_dic)

    # Number of matches between pet image and classifier labels
    results_stats_dic["n_match"] = 0

    # Number of dog images classified
    results_stats_dic["n_dogs_img"] = 0
    
    # Number of correct dog classifications
    results_stats_dic["n_correct_dogs"] = 0
    
    # Number of non-dog images classified
    results_stats_dic["n_notdogs_img"] = 0
    
    # Number of correct non-dog classifications
    results_stats_dic["n_correct_notdogs"] = 0
    
    # Number of correct breed classifications
    results_stats_dic["n_correct_breed"] = 0
    
    # Iterate through the results dictionary and count the number of match, dogs, non-dogs,
    # correct dogs, and correct breeds
    for key in results_dic:
        
        # Number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic["n_dogs_img"] += 1
            # Number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic["n_correct_dogs"] += 1
        
        # Number of non-dog images
        if results_dic[key][3] == 0:
            results_stats_dic["n_notdogs_img"] += 1
            # Number of correct non-dog classifications
            if results_dic[key][4] == 0:
                results_stats_dic["n_correct_notdogs"] += 1
        
        # Number of correct breed classifications
        if results_dic[key][2] == 1 and results_dic[key][3] == 1:
            results_stats_dic["n_correct_breed"] += 1

        # (OPTIONAL) Number of label matches
        if results_dic[key][2] == 1:
            results_stats_dic["n_match"] += 1

    # (Objective 1-a) Calculate the percentage of correctly classified dogs images
    results_stats_dic["pct_correct_dogs"] = results_stats_dic["n_correct_dogs"] / results_stats_dic["n_dogs_img"] * 100
    
    # (Objective 1-b) Calculate the percentage of correctly classified non-dogs images
    if results_stats_dic["n_notdogs_img"] > 0:
        results_stats_dic["pct_correct_notdogs"] = results_stats_dic["n_correct_notdogs"] / results_stats_dic["n_notdogs_img"] * 100
    else:
        results_stats_dic["pct_correct_notdogs"] = 0
    
    # (Objective 2) Calculate the percentage of correctly classified dog breed images
    results_stats_dic["pct_correct_breed"] = results_stats_dic["n_correct_breed"] / results_stats_dic["n_dogs_img"] * 100

    # (OPTIONAL) Calculate the percentage of correctly matched images (regardless if they are a dog)
    results_stats_dic["pct_match"] = results_stats_dic["n_match"] / results_stats_dic["n_images"] * 100

    return results_stats_dic
