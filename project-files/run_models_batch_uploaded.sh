# PURPOSE: Runs all three models to test which provides 'best' solution on the uploaded images.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch_uploaded.sh    -- will run program from command line
python check_images.py --dir uploaded-images/ --arch resnet  --dogfile dognames.txt > resnet-images-uploaded.txt
python check_images.py --dir uploaded-images/ --arch alexnet --dogfile dognames.txt > alexnet-images-uploaded.txt
python check_images.py --dir uploaded-images/ --arch vgg  --dogfile dognames.txt > vgg-images-uploaded.txt
