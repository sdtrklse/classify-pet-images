@echo off
REM Purpose: Runs all three models to test which provides "best" solution and pipes output from each run into a text file.
REM Usage: batch-processing\run_models_batch.bat  -- will run program from command line on Window OS
@echo on
python check_images.py --dir ../data/pet-images/ --arch alexnet --dogfile ../data/labels/dognames.txt > ../outputs/images-pet-alexnet.txt
python check_images.py --dir ../data/pet-images/ --arch resnet  --dogfile ../data/labels/dognames.txt > ../outputs/images-pet-resnet.txt
python check_images.py --dir ../data/pet-images/ --arch vgg  --dogfile ../data/labels/dognames.txt > ../outputs/images-pet-vgg.txt
