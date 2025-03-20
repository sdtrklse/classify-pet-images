@echo off
REM PURPOSE: Runs all three models to test which provides 'best' solution on the uploaded images.
REM          Please note output from each run has been piped into a text file.
REM
REM Usage: batch-processing\run_models_batch_uploaded.bat  -- will run program from command line on Window OS
@echo on
python check_images.py --dir ../data/uploaded-images/ --arch alexnet --dogfile ../data/labels/dognames.txt > ../outputs/images-uploaded-alexnet.txt
python check_images.py --dir ../data/uploaded-images/ --arch resnet  --dogfile ../data/labels/dognames.txt > ../outputs/images-uploaded-resnet.txt
python check_images.py --dir ../data/uploaded-images/ --arch vgg  --dogfile ../data/labels/dognames.txt > ../outputs/images-uploaded-vgg.txt
