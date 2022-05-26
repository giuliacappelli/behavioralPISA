# Behavioral PISA: A (behavioral) measure of Preference In Selection of Arguments to model verb argument recoverability

This script serves two purposes (explained below):
1. creating stimuli for a behavioral experiment
2. computing the Behavioral PISA scores based on the results of the aforementioned experiment

## Getting started

The script should run on Python 3.0+ and does not have to be installed. Runs fine on Python 3.10.4 in Ubuntu 22.04.

### Prerequisites

You need the following packages to make the script work:

    argparse>=1.1
    pandas>=1.3.5
    numpy>=1.21.5
    os
    random
    scipy>=1.8.0
    
To install these packages in Python 3, make sure you have installed pip3 and run:    
    
    pip3 install <package>
    
## Running the script

Make sure you have the script and the input file within the same folder before starting.

### Parameters

You may pass several optional parameters to the script:

    --verbs, -v:    folder containing a space-separated file for each verb of interest, each containing a list of direct objects (defaults to input/verbs/)
    --input, -i:    file containing space-separated similarity judgments in the form "word1 word2 sim_score" (defaults to input/judgments.csv)
    --kind, -k:     the kind of input data to be processed: can be either STIMULI or JUDGMENTS
    --stimuli, -s:  output folder for the experimental stimuli
    
To access the list of parameters in your terminal, run:    
    
    python3 computeObjectSim.py -h
    
### Creating stimuli for the behavioral experiment

Doing so will require two parameters: `--kind` (set to `stimuli`) and `--verbs`.

For each verb, you will have a space-separated, header-less file in the `--verbs` folder containing a direct object per line (together with additional, optional information). For instance, the file for the verb 'to eat' would look like this, if you had both its objects and their frequencies in a corpus:

| | | |
|-|-|-|
| pizza | 180
| hamburger | 150
| hat | 10

The script will read these files, extract 6 pairs of objects for each verb, and print a single output file shaped like this:

| | | |
|-|-|-|
| verb_1 | dObj_1 | dObj_5
| verb_1 | dObj_6 | dObj_31
| verb_1 | dObj_6 | dObj_2
| verb_2 | dObj_1 | dObj_2

You can easily use this output file as stimuli in your Behavioral PISA experiment by removing the verb column and, for instance, importing the resulting file into your experimental platform of choice (e.g. PsychoPy, to upload on Pavlovia).

### Computing Behavioral PISA scores

Doing so will require two parameters: `--kind` (set to `judgments`) and `--input`.

Given an input file containing space-separated similarity judgments in the form "word1 word2 sim_score", the script preprocesses raw judgment data following Kim et al. (2019), i.e. it computes the within-subject z-scores for the judgments, then averages these scores to obtain the mean judgment for each pair of objects in the stimuli list, then normalizes the mean judgments to fall between 0 and 1.

The output of this section of the script is a csv file containing a verb and its Behavioral PISA score per line.

## License

This project is licensed under the MIT License. May it provide optimal data for all your experimental needs :mortar_board:

## References
* Cappelli, Giulia; Lenci, Alessandro (2020). "A measure of Preference In Selection of Arguments to model verb argument recoverability", Proceedings of the Ninth Joint Conference on Lexical and Computational Semantics, Barcelona, Spain (Online), Association for Computational Linguistics, pp. 131-136. [ACL Anthology](https://www.aclweb.org/anthology/2020.starsem-1.14/)
* Kim, Najoung; Rawlins, Kyle; Smolensky, Paul (2019). "The complement-adjunct distinction as gradient blends: the case of English prepositional phrases", [lingbuzz/004723](https://ling.auf.net/lingbuzz/004723)

To cite my computational paper which inspired Behavioral PISA:
```
@inproceedings{cappelli-lenci-2020-pisa,
    title = "{PISA}: A measure of Preference In Selection of Arguments to model verb argument recoverability",
    author = "Cappelli, Giulia  and
      Lenci, Alessandro",
    booktitle = "Proceedings of the Ninth Joint Conference on Lexical and Computational Semantics",
    month = dec,
    year = "2020",
    address = "Barcelona, Spain (Online)",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.starsem-1.14",
    pages = "131--136",
    abstract = "Our paper offers a computational model of the semantic recoverability of verb arguments, tested in particular on direct objects and Instruments. Our fully distributional model is intended to improve on older taxonomy-based models, which require a lexicon in addition to the training corpus. We computed the selectional preferences of 99 transitive verbs and 173 Instrument verbs as the mean value of the pairwise cosines between their arguments (a weighted mean between all the arguments, or an unweighted mean with the topmost k arguments). Results show that our model can predict the recoverability of objects and Instruments, providing a similar result to that of taxonomy-based models but at a much cheaper computational cost.",
}
```

## Acknowledgments
Many thanks to 
* @ellepannitto, my Python fairy
* @najoungkim, for sharing references that ultimately led to my PhD project
* the Stack Overflow community, for the many code snippets that saved me from frustration

