# Corpus for Spain Languages using Audio Data Augmentation (ADA)

To contribute to the [ELE strategic agenda](https://european-language-equality.eu/), we create a dataset for building an extensive speech dataset with transcriptions of languages spoken in Spain using audio data augmentation (ADA) techniques. In particular, for languages: **Catalan**, **Galician**, **Asturian** and **Euskera**. 

The complete report is [here (PENDING)](https://github.com/Pangeamt/ele2-ada). 

We provide the datasets generated in this report, which include the audio files and metadata (including transcriptions) for your convenience and further use.

We hope to encourage the speech technology community to generate more and larger datasets in other EU languages.



## Corpus 

The dataset is distributed as follows:


| File                               | # audio | hrs   | Size  | Description          |
|------------------------------------|---------|-------|-------|------------------------------------|
| [catalan_dataset.zip](https://s3.eu-west-1.amazonaws.com/com.pangeanic.voice.projects/ele2-ada/catalan_dataset.zip) | 20,277  | 56.7  | 11.0 GB | Audio files in the Catalan language and metadata. |
| [galician_dataset.zip](https://s3.eu-west-1.amazonaws.com/com.pangeanic.voice.projects/ele2-ada/galician_dataset.zip) | 22,304  | 62.5  | 8.0 GB | Audio files in the Galician language and metadata.|
| [euskera_dataset.zip](https://s3.eu-west-1.amazonaws.com/com.pangeanic.voice.projects/ele2-ada/euskera_dataset.zip)  | 12,231  | 37.6  | 6.0 GB | Audio files in the Euskera language and metadata. |
| [asturian_dataset.zip](https://s3.eu-west-1.amazonaws.com/com.pangeanic.voice.projects/ele2-ada/asturian_dataset.zip) |  8,459  | 25.6  | 3.7 GB | Audio files in the Asturian language and metadata.|
| **TOTAL**                              | **63,271**  | **182.4** |                           |

We provide the [noises](https://s3.eu-west-1.amazonaws.com/com.pangeanic.voice.projects/ele2-ada/noises.zip) (28 MB) applied in ADA, and also all previous files in [one zip file](https://s3.eu-west-1.amazonaws.com/com.pangeanic.voice.projects/ele2-ada/all.zip) (29 GB). 

## Example of ADA

An example of [ADA applied to asturian](https://s3.eu-west-1.amazonaws.com/com.pangeanic.voice.projects/ele2-ada/ast_ADA.zip) (133 GB) is available to download. 
The `ADA/` folder contains 169,162 audio files, which is 20 times the original dataset of the asturian language.

However, given the file is too large, we provide **in this repository** a tiny example using the asturian language. The file `ast_metada_tiny.json` is the metadata of two audio files in asturian that are in `ast/` folder, and `ast_ADA_metada_tiny.json` is the metadata of the augmented files that are in `ADA/`. 


## Usage

To use this dataset, simply download it following each reference. The transcriptions and metadata can also be used to analyze and annotate the speech data. It could be useful to balance characteristics such as gender and age range. 


## Audio Data Augmentation

The source code of ADA and documentation are [here](https://github.com/Pangeamt/ele2-ada/tree/main/da_techniques). 


## Citation
If you use the datasets for any purpose, please cite the original source of the dataset as well as this repository.



```bib
@Misc{ele2-da,
	author = {Jose Herrera and Moises Barrios},
	title =	{{Generation of a Large Speech Corpus for Spain Languages using Data Augmentation}},
	year =	2023,
	url =	{PENDING},
	note =	{Project deliverable; EU project European Language Equality (ELE); Grant Agreement no.~LC-01884166 – 101075356 ELE2},
}
```


## Contact
If you have any questions or comments about this repository, please feel free to contact us at [support@pangeanic.com](mail:support@pangeanic.com).