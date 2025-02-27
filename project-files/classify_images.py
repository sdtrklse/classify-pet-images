import os
from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function. The classifier
    labels are formatted so that they will match the pet image labels.
    The format will include putting the classifier labels in all lower case
    letters and strip the leading and trailing whitespace characters from them.
    For example, the classifier function returns = "Maltese dog, Maltese terrier, Maltese"
    so the classifier label = "maltese dog, maltese terrier, maltese".
    
    Parameters:
        images_dir - The (full) path to the folder of images that are to be
            classified by the classifier function (string)
        results_dic - Results dictionary with "key" as image filename and "value"
            as a list. Where the list will contain the following items:
                index 0 = pet image label (string)
                --- where index 1 and index 2 are added by this function ---
                NEW - index 1 = classifier label (string)
                NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
        model - Indicates which CNN model architecture will be used by the
            classifier function to classify the pet images,
            values must be either: resnet, alexnet, or vgg (string)
    
    Returns:
        None - results_dic is mutable data type so no return needed.
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
