@echo off
REM PURPOSE: Runs all three models to test which provides 'best' solution on the uploaded images.
REM          Please note output from each run has been piped into a text file.
REM
REM Usage: run_models_batch_uploaded.bat  -- will run program from command line on Window OS
@echo on
python check_images.py --dir uploaded-images/ --arch resnet  --dogfile dognames.txt > resnet-images-uploaded.txt
python check_images.py --dir uploaded-images/ --arch alexnet --dogfile dognames.txt > alexnet-images-uploaded.txt
python check_images.py --dir uploaded-images/ --arch vgg  --dogfile dognames.txt > vgg-images-uploaded.txt
