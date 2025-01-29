@echo off
REM PURPOSE: Runs all three models to test which provides 'best' solution.
REM          Please note output from each run has been piped into a text file.
REM
REM Usage: run_models_batch.bat  -- will run program from command line on Window OS
@echo on
python check_images.py --dir pet-images/ --arch resnet  --dogfile dognames.txt > resnet-images-pet.txt
python check_images.py --dir pet-images/ --arch alexnet --dogfile dognames.txt > alexnet-images-pet.txt
python check_images.py --dir pet-images/ --arch vgg  --dogfile dognames.txt > vgg-images-pet.txt
