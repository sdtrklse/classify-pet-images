from typing import Dict, List, Union


def print_results(
    results_dic: Dict[str, List[Union[str, int]]],
    results_stats_dic: Dict[str, Union[int, float]],
    model: str,
    print_incorrect_dogs: bool = False,
    print_incorrect_breed: bool = False
) -> None:
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values).

    Parameters:
        results_dic (Dict[str, List[Union[str, int]]]): Dictionary with key
            as image filename and value as a list
                index 0 = pet image label (string)
                index 1 = classifier label (string)
                index 2 = 1/0 (int)  where 1 = match between pet image and
                    classifer labels and 0 = no match between labels
                index 3 = 1/0 (int)  where 1 = pet image "is-a" dog and
                    0 = pet image "is-NOT-a" dog
                index 4 = 1/0 (int)  where 1 = classifier classifies image "as-a" dog and
                    0 = classifier classifies image "as-NOT-a" dog
        results_stats_dic (Dict[str, Union[int, float]]): Dictionary that contains the
            results statistics (either a percentage or a count) where the key is
            the statistic's name (starting with "pct" for percentage or "n" for count)
            and the value is the statistic's value
        model (str): Indicates which CNN model architecture will be used by the
            classifier function to classify the pet images, values must be
            either: resnet, alexnet, or vgg (string)
        print_incorrect_dogs (bool): True prints incorrectly classified dog images and
            False doesn't print anything (default) (bool)
        print_incorrect_breed (bool): True prints incorrectly classified dog breeds and
            False doesn't print anything (default) (bool)

    Returns:
        None - simply printing results
    """

    # Print summary results
    print(f"\n=== Results Summary for CNN Model Architecture: {model.upper()} ===\n")
    print(f"{"Number of Images":27}: {results_stats_dic["n_images"]:1d}")
    print(f"{"Number of Dog Images":27}: {results_stats_dic["n_dogs_img"]:1d}")
    print(f"{"Number of Not a Dog Images":27}: {results_stats_dic["n_notdogs_img"]:1d}")

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
