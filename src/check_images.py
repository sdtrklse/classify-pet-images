import time

# Import functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


# Main program function
def main():
    """
    Main function that orchestrates the image classification process and calculates runtime.

    This function:
        - Retrieves command-line arguments
        - Generates pet image labels
        - Classifies images using a specified CNN model
        - Adjusts results for dog classification accuracy
        - Calculates and prints statistical results
        - Measures and prints total program runtime
    """

    # Measure total program runtime by collecting start time
    start_time = time.time()

    # Retrieve command-line arguments
    in_arg = get_input_args()

    # Generate pet image labels dictionary
    results = get_pet_labels(in_arg.dir)

    # Classify images and update results dictionary
    classify_images(in_arg.dir, results, in_arg.arch)
    
    # Adjust results dictionary for dog classification
    adjust_results4_isadog(results, in_arg.dogfile)

    # Calculate results statistics
    results_stats = calculates_results_stats(results)

    # Print results and incorrect classifications if requested
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time.time()
    
    # Compute overall runtime in seconds and print it in hh:mm:ss format
    tot_time = end_time - start_time
    hours = int(tot_time / 3600)
    minutes = int((tot_time % 3600) / 60)
    seconds = int((tot_time % 3600) % 60)
    
    print(f"\nTotal Elapsed Runtime: {hours:02}:{minutes:02}:{seconds:02}\n")


# Call to main function to run the program
if __name__ == "__main__":
    main()
