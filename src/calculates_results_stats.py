def calculates_results_stats(results_dic):
    """
    Calculates statistics from the results dictionary, including the number of images,
    matches, dog images, correct dog classifications, non-dog images, correct non-dog
    classifications, and correct breed classifications.

    Parameters:
        results_dic (dict): Dictionary with image filenames as keys and a list
            containing pet label, classifier label, is-a-dog, and other information.
    
    Returns:
        dict: A dictionary containing the calculated statistics.
    """

    # Initialize the results statistics dictionary
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
    
    # Iterate through the results dictionary
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
