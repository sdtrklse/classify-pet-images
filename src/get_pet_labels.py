import os


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels from the filenames in the image directory.
    
    Parameters:
        image_dir (str): The directory containing the pet images.
    
    Returns:
        results_dic (dict): A dictionary where the keys are filenames and the values
            are lists containing the pet labels.
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
 