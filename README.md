# Corpus for Spain Languages using Data Augmentation

To contribute to the [ELE strategic agenda](https://european-language-equality.eu/), we create a dataset for building an extensive speech dataset with transcriptions of languages spoken in Spain using audio data augmentation (ADA) techniques. In particular, for languages: **Catalan**, **Galician**, **Asturian** and **Euskera**. 

The complete report is [here](http://report).
We provide the datasets generated in this report, which include both the audio files and metadata (including transcriptions) for your convenience and further use.

We hope to encourage the speech technology community to generate more and larger datasets in other EU languages.



## Corpus 

The dataset is distributed as follows:


| File                               | # audio | hrs   | Size  | Description          |
|------------------------------------|---------|-------|-------|--------------------------------|
| [catalan_audios_original.zip](http://XX)  | 12,231  | 56.7  | XX GB | Original audios of catalan and metadata. |
| [galician_audios_original.zip](http://XX) | 22,304  | 62.5  | XX GB | Original audios of galician and metadata.|
| [euskera_audios_original.zip](http://XX)  | 12,231  | 37.6  | XX GB | Original audios of euskera and metadata. |
| [asturian_audios_original.zip](http://XX) |  8,459  | 25.6  | XX GB | Original audios of asturian and metadata.|
| **TOTAL**                              | **63,271**  | **182.5** |                           |

Additionaly, we provide the [noises](http://noises.zip) (XX GB) used in ADA and [examples of files with ADA applied](http://ada.zip) (XX GB).

Note: The metadata files and source code makes reference to the audio files based on the 
these struct:

```bash
audios/original/*  # for original audios 
audio/ada/*        # for audios with ADA applied
```

So, it is important that you store the audio files in accordance with the previous structure to ensure that they are easily accessible and properly aligned with the corresponding metadata.


## Usage

To use this dataset, simply download it following each reference. The transcriptions and metadata can also be used to analyze and annotate the speech data. It could be useful to balance characteristics such as gender and age range. 


## Data Augmentation Techniques

We used the following ADA techniques:

* **Background noise**: This technique involves adding random background noise to the speech signal to simulate real-world environments.

* **Time stretching**: This technique involves changing the duration of the speech signal to increase its variability.

* **Gaussean noise**: This technique simulates the effects of background noise in real-world environments. 

The parameteres used are in the [report](http://report).



## Citation
If you use the datasets for any purpose, please cite the original source of the dataset as well as this repository.



```bib
@Misc{ele2-da,
	author =	{Jose Herrera and Moises Barrios},
	title =		{{Generation of a Large Speech Corpus for Spain Languages using Data Augmentation}},
	year =		2023,
	url =		{XXXX},
	note =		{Project deliverable; EU project European Language Equality (ELE); Grant Agreement no.~LC-01884166 – 101075356 ELE2},
}
```


## Contact
If you have any questions or comments about this repository, please feel free to contact us at XXXXXX. 