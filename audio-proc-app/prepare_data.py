import librosa
import os
import json

DATASET_PATH = "dataset"
JSON_PATH = "data.json"
SAMPLE_TO_CONSIDER = 22050  # 1 second worth of data/samples


def prepare_dataset(dataset_path, json_path, n_mfcc=13, hop_length=512, n_fft=2048) -> json:
    """
    Using MFCC from librosa
    extracting 13 coefficients
    512 hop_length is the size of the segment in number of frames, customary size for MFCC
    fft is the window for fast forward transform, customary size for MFCC
    """

    # data dict

    pass
