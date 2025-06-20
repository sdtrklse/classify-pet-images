def print_results(
    results_dic, results_stats_dic, model, print_incorrect_dogs=False, print_incorrect_breed=False
):
    """
    Prints the results of the image classification, including statistics and
    incorrect classifications (if requested).
    
    Parameters:
        results_dic (dict): Dictionary with image filenames as keys and a list
            containing pet label and classifier label as values.
        results_stats_dic (dict): Dictionary with a key named "n_images" with the
            number of images, "n_dogs_img" with the number of dog images, and
            "n_notdogs_img" with the number of non-dog images.
        model (str): The CNN model architecture used for classification.
        print_incorrect_dogs (bool): True if incorrect dog classifications should
            be printed, False if not.
        print_incorrect_breed (bool): True if incorrect breed classifications
            should be printed, False if not.
    
    Returns:
        None: This function does not return any value; it prints the results
        directly to the console.
    """
    
    # Print summary results
    print(f"\n=== Results Summary for CNN Model Architecture: {model.upper()} ===\n")
    print(f"{'Number of Images':27}: {results_stats_dic['n_images']:1d}")
    print(f"{'Number of Dog Images':27}: {results_stats_dic['n_dogs_img']:1d}")
    print(f"{'Number of Not a Dog Images':27}: {results_stats_dic['n_notdogs_img']:1d}")
    
    # Print percentages of correct classifications for dogs and breeds
    for key in results_stats_dic:
        if key.startswith("pct"):
            print(f"{key:20}: {results_stats_dic[key]:.1f}")
    
    # Print incorrect classifications of dogs (if requested)
    if (print_incorrect_dogs and ((results_stats_dic["n_correct_dogs"] +
                                   results_stats_dic["n_correct_notdogs"]) !=
                                   results_stats_dic["n_images"])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        
        # Iterate through the results dictionary and print the misclassified dogs
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print(f"Real: {results_dic[key][0]:20}\tClassifier: {results_dic[key][1]:20}")
    
    # Print incorrect classifications of dog breeds (if requested)
    if (print_incorrect_breed and (results_stats_dic["n_correct_dogs"] !=
                                   results_stats_dic["n_correct_breed"])):
        print("\nINCORRECT Dog Breed Assignments:")
        
        # Iterate through the results dictionary and print the misclassified breeds
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print(f"Real: {results_dic[key][0]:20}\tClassifier: {results_dic[key][1]:20}")
