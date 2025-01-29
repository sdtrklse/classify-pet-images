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
    # Measures total program runtime by collecting start time
    start_time = time.time()

    # This function retrieves 3 command-line arguments as input from the user
    # running the program from a terminal window.
    in_arg = get_input_args()

    # This function creates the results dictionary that contains the results.
    results = get_pet_labels(in_arg.dir)

    # This function creates classifier labels with classifier function, compares labels,
    # and adds these results to the results dictionary.
    classify_images(in_arg.dir, results, in_arg.arch)
    
    # This function adjusts the results dictionary to determine if classifier correctly
    # classified images as 'a dog' or 'not a dog'. This demonstrates if
    # model can correctly classify dog images as dogs (regardless of breed).
    adjust_results4_isadog(results, in_arg.dogfile)

    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts and percentages).
    results_stats = calculates_results_stats(results)

    # This function prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested).
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Measure total program runtime by collecting end time
    end_time = time.time()

    # Computes overall runtime in seconds and prints it in hh:mm:ss format
    tot_time = end_time - start_time

    hours = int(tot_time / 3600)
    minutes = int((tot_time % 3600) / 60)
    seconds = int((tot_time % 3600) % 60)

    print(f"\nTotal Elapsed Runtime: {hours:02}:{minutes:02}:{seconds:02}\n")


# Call to main function to run the program
if __name__ == "__main__":
    main()
