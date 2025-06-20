# The code in this file is provided by Udacity as part of the project.
# It is used to classify pet images using pre-trained models from PyTorch.

import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__


# Fix the `weights` argument in `models` to prevent warning messages
alexnet = models.alexnet(weights="AlexNet_Weights.DEFAULT")
resnet18 = models.resnet18(weights="ResNet18_Weights.DEFAULT")
vgg16 = models.vgg16(weights="VGG16_Weights.DEFAULT")

models = {
    "alexnet": alexnet,
    "resnet": resnet18,
    "vgg": vgg16
}

# Obtain ImageNet labels
with open("../data/labels/imagenet1000-clsid-to-human.txt") as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    """
    Loads an image and applies a model to it. Returns the predicted class as a string.

    Args:
        img_path (str): path to the image
        model_name (str): name of the model to use
    
    Returns:
        str: predicted class
    """

    # Load the image
    img_pil = Image.open(img_path)

    # Define transforms
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Preprocess the image
    img_tensor = preprocess(img_pil)
    
    # Resize the tensor (add dimension for batch)
    img_tensor.unsqueeze_(0)
    
    # Wrap input in variable, wrap input in variable - no longer needed for
    # v0.4 & higher code changed 04/26/2018 by Jennifer S. to handle PyTorch upgrade
    pytorch_ver = __version__.split(".")
    
    # PyTorch versions 0.4 & higher - Variable deprecated so that it returns
    # a tensor. So to address tensor as output (not wrapper) and to mimic the
    # affect of setting volatile = True (because we are using pre-trained models
    # for inference) we can set requires_grad_ to False. Here we just set
    # requires_grad_ to False on our tensor.
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)
    
    # PyTorch versions less than 0.4 - uses Variable because not-deprecated
    else:
        # Apply model to input
        # Wrap input in Variable
        data = Variable(img_tensor, volatile=True)
    
    # Apply model to input
    model = models[model_name]

    # Puts model in evaluation mode
    # Instead of (default) training mode
    model = model.eval()
    
    # Apply data to model - adjusted based upon version to account for
    # Operating on a Tensor for version 0.4 & higher.
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        output = model(img_tensor)
    
    # PyTorch versions less than 0.4
    else:
        # Apply data to model
        output = model(data)
    
    # Return index corresponding to predicted class
    pred_idx = output.data.numpy().argmax()

    return imagenet_classes_dict[pred_idx]
