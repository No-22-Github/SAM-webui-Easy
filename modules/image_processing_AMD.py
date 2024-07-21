import os
import numpy as np
import cv2
import torch
import torch_directml
import sys
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
from modules.mask_utils import MaskUtils



def init_sam_model(sam_checkpoint="./models/sam_vit_h_4b8939.pth", model_type="default", use_directml=True):
        print("加载模型中...")

        if use_directml:
            device = torch_directml.device()
        else:
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
        
        if use_directml:
            sam = sam.to(device)
        else:
            sam = sam.to(device=device)
        
        sam.to(dtype=torch.float32)

        sam_predictor = SamPredictor(sam)
        mask_utils = MaskUtils(sam_predictor)
        
        print("使用设备:", "DirectML" if use_directml else device)
        print("仅对DirectML设备初步支持，如有bug请等待更新")

        return mask_utils


def process_image(image_path, mask_utils:MaskUtils, input_point, input_label, save_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return mask_utils.show_best_mask(image, input_point, input_label, save_path=save_path)