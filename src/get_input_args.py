import argparse


def get_input_args():
    """
    Retrieves and parses the 3 command-line arguments provided by the user when they run the program.
    This function uses the argparse module to create and return an ArgumentParser object with the specified arguments.

    Command-line arguments:
        1. --dir: The path to the folder of pet images (default: "../data/pet-images/")
        2. --arch: The CNN model architecture to use (default: "vgg")
        3. --dogfile: The text file containing the names of dog breeds (default: "../data/labels/dognames.txt")
    
    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
    """
    
    # Create parser using ArgumentParser
    parser = argparse.ArgumentParser()

    # Argument 1: Image folder as --dir with default value "../data/pet-images/"
    parser.add_argument(
        "--dir", type=str,
        default="../data/pet-images/",
        help="path to the folder of pet images"
    )
    
    # Argument 2: CNN model architecture as --arch with default value "vgg"
    parser.add_argument(
        "--arch", type=str,
        default="vgg",
        help="the CNN model architecture"
    )
    
    # Argument 3: Text file with dog names as --dogfile with default value "../data/labels/dognames.txt"
    parser.add_argument(
        "--dogfile", type=str,
        default="../data/labels/dognames.txt",
        help="text file of names of dog breeds"
    )
    
    return parser.parse_args()
