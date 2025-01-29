import argparse


def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module. If the user fails to provide some or all of the 3 arguments,
    then the default values are used for the missing arguments.

    Command-line arguments:
        1. Image folder as --dir with default value 'pet-images'
        2. CNN model architecture as --arch with default value 'vgg'
        3. Text file with dog names as --dogfile with default value 'dognames.txt'
    
    This function returns these arguments as an ArgumentParser object.
    
    Parameters:
        None - simply using argparse module to create and store command-line arguments
    
    Returns:
        parse_args() - data structure that stores the command-line arguments object
    """

    # Create parser using ArgumentParser
    parser = argparse.ArgumentParser()

    # Create 3 command-line arguments as mentioned above using add_argument()
    # from ArguementParser method
    
    # Argument 1: Image folder
    parser.add_argument(
        '--dir', type=str,
        default='pet-images/',
        help='path to the folder of pet images'
    )
    
    # Argument 2: CNN model architecture
    parser.add_argument(
        '--arch', type=str,
        default='vgg',
        help='the CNN model architecture'
    )

    # Argument 3: Text file with dog names
    parser.add_argument(
        '--dogfile', type=str,
        default='dognames.txt',
        help='text file of names of dog breeds'
    )

    return parser.parse_args()
