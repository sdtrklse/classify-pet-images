# Purpose: Runs all three models to test which provides "best" solution and pipes output from each run into a text file.
# Usage: sh batch-processing/run_models_batch.sh  -- will run program from command line
python check_images.py --dir ../data/pet-images/ --arch alexnet --dogfile ../data/labels/dognames.txt > ../outputs/images-pet-alexnet.txt
python check_images.py --dir ../data/pet-images/ --arch resnet  --dogfile ../data/labels/dognames.txt > ../outputs/images-pet-resnet.txt
python check_images.py --dir ../data/pet-images/ --arch vgg  --dogfile ../data/labels/dognames.txt > ../outputs/images-pet-vgg.txt
