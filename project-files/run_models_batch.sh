# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch.sh    -- will run program from command line
python check_images.py --dir pet-images/ --arch resnet  --dogfile dognames.txt > resnet-images-pet.txt
python check_images.py --dir pet-images/ --arch alexnet --dogfile dognames.txt > alexnet-images-pet.txt
python check_images.py --dir pet-images/ --arch vgg  --dogfile dognames.txt > vgg-images-pet.txt
