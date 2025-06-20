# Questions Regarding Uploaded Image Classification

**Question 1:** Did the three model architectures classify the breed of dog in `Dog_01.jpg` to be the same breed? If not, report the differences in the classifications.

**Answer:** No, the three model architectures did not classify the breed of dog (*Dachshund*) in `Dog_01.jpg` to be the same breed. Here are the differences in the classifications:

- AlexNet: doberman, doberman pinscher
- VGG: black-and-tan coonhound
- ResNet: black-and-tan coonhound

**Question 2:** Did each of the three model architectures classify the breed of dog in `Dog_01.jpg` to be the same breed of dog as that model architecture classified `Dog_02.jpg`? If not, report the differences in the classifications.

**Answer:** No, each of the three model architectures did not classify the breed of dog in `Dog_01.jpg` to be the same breed of dog as that model architecture classified `Dog_02.jpg`. Here are the differences in the classifications:

- AlexNet
    - Dog_01.jpg: doberman, doberman pinscher
    - Dog_02.jpg: miniature pinscher
- VGG
    - Dog_01.jpg: black-and-tan coonhound
    - Dog_02.jpg: doberman, doberman pinscher
- ResNet
    - Dog_01.jpg: black-and-tan coonhound
    - Dog_02.jpg: muzzle

**Question 3:** Did the three model architectures correctly classify `Animal_Name_01.jpg` and `Object_Name_01.jpg` to not be dogs? If not, report the misclassifications.

**Answer:** Yes, the three model architectures correctly classified `Animal_Name_01.jpg` and `Object_Name_01.jpg` to not be dogs. Here are the classifications:

- AlexNet
    - `Coffee_mug_01.jpg`: coffee mug (correctly classified as not a dog)
    - `Polar_bear_01.jpg`: ice bear, polar bear, ursus maritimus, thalarctos maritimus (correctly classified as not a dog)
- VGG
    - `Coffee_mug_01.jpg`: coffee mug (correctly classified as not a dog)
    - `Polar_bear_01.jpg`: ice bear, polar bear, ursus maritimus, thalarctos maritimus (correctly classified as not a dog)
- ResNet
    - `Coffee_mug_01.jpg`: coffee mug (correctly classified as not a dog)
    - `Polar_bear_01.jpg`: ice bear, polar bear, ursus maritimus, thalarctos maritimus (correctly classified as not a dog)

**Question 4:** Based upon your answers for questions 1-3 above, select the model architecture that you feel did the best at classifying the four uploaded images. Describe why you selected that model architecture as the best on uploaded image classification.

**Answer:** Based on the answers for questions 1-3, the *VGG* model architecture did the best at classifying the four uploaded images.

Here is the reasoning:

- VGG correctly classified both non-dog images (`Coffee_mug_01.jpg` and `Polar_bear_01.jpg`) as not dogs.
- VGG had consistent classifications for `Dog_01.jpg` and `Dog_02.jpg`, identifying them both as specific dog breeds, even though the breeds were not correct.
- Compared to ResNet, which misclassified `Dog_02.jpg` as "muzzle" (not a breed), VGG provided more plausible dog breed classifications.

Overall, VGG demonstrated better performance in terms of correctly identifying non-dog images and providing reasonable dog breed classifications. Although I have tried couple of different breeds of `Dog_01_.jpg` and `Dog_02.jpg` images, the results may vary slightly depending on the breed of the dog in the image.
