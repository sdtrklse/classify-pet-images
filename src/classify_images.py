import os
from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Classifies pet images using a pre-trained classifier and updates the results dictionary.
    
    Parameters:
        images_dir (str): Directory containing pet images.
        results_dic (dict): Dictionary containing image filenames and their labels.
        model (str): Pre-trained model to use for classification.
    
    Returns:
        None: The results_dic is updated in place with classifier labels and match status.
    """
    
    # Get the classifier labels for each image
    classifier_labels = [
        classifier(os.path.join(images_dir, filename), model).lower().strip()
        for filename in results_dic.keys()
    ]
    
    # Compare the classifier labels to the pet image labels
    for filename, results, classifier_label in zip(results_dic.keys(), results_dic.values(), classifier_labels):
        results_dic[filename].extend(
            [classifier_label, 1 if results[0] in classifier_label else 0]
        )
