# **Audio Data Augmentation**

## **Transformations**

All the transformations used have been extracted from [audiomentations library](https://iver56.github.io/audiomentations/). Specifically, the transformations used are:

- **AddBackgroundNoise**: This technique involves adding random background noise to the speech signal to simulate real-world environments.
- **AddGaussianNoise**: This technique simulates the effects of background noise in real-world environments. 
- **TanhDistortion**: This technique applied a distortion in the speech. 
- **TimeStretch**: This technique involves changing the duration of the speech signal to increase its variability.


## **Usage example**

In order to apply data augmentation to a set of audios, the following command should be execute from the Linux terminal. Two arguments are needed: the first one corresponds to the audios metadata and the second one corresponds to the number of augmentations per file.

```bash
python da.py <audios_metadata> <num_DA_per_file>
```

Once the command is executed, the audios begin to be processed. First, a random background noise is added to the original audio. After that, a random transformation is applied. Finally, the augmented audios and a metadata file are generated.

Note: It is necesary to have an `ADA` folder where all the augmented audios will be saved.

## **References**

[Common Voice Datasets in Spanish](https://commonvoice.mozilla.org/es/datasets)

[Audiomentations library](https://iver56.github.io/audiomentations/)