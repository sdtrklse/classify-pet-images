# The code in this file is provided by Udacity and is not written by me
# 
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh batch-processing/run_models_batch.sh    -- will run program from command line
python check_images.py --dir pet-images/ --arch alexnet --dogfile labels/dognames.txt > outputs/images-pet-alexnet.txt
python check_images.py --dir pet-images/ --arch resnet  --dogfile labels/dognames.txt > outputs/images-pet-resnet.txt
python check_images.py --dir pet-images/ --arch vgg  --dogfile labels/dognames.txt > outputs/images-pet-vgg.txt
