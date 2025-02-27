import os


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    
    The pet labels are formatted so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = "Boston_terrier_02259.jpg" Pet label = "boston terrier")
    
    Parameters:
        image_dir - The (full) path to the folder of images that are to be
            classified by the classifier function (string)
    
    Returns:
        results_dic - Dictionary with "key" as image filename and "value" as a
            list. The list contains for following item:
                index 0 = pet image label (string)
    """
    
    # Get the filenames from the image directory
    # os.listdir() returns a list of all files in a directory
    filename_list = os.listdir(image_dir)

    # Create the results dictionary with the pet labels from the filenames
    # Iterate over the list of filenames and create a dictionary with filename
    # as the key and the pet label as the value
    results_dic = {
        filename: [" ".join(filename.lower().strip().split("_")[:-1])]
        for filename in filename_list
    }

    return results_dic
 