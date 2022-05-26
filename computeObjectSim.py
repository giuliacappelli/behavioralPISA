import argparse
import pandas as pd
import os
import random
from scipy.stats import zscore

"""
Computes the Object Similarity score as designed by Medina (2007),
which works as a behavioral precursor of PISA (my distributional enhancement of Resnik's SPS)
"""

my_parser = argparse.ArgumentParser()

my_parser.add_argument('--verbs',
                       '-v',
                       action='store',
                       default='input/verbs/',
                       help='folder containing a dObj file for each verb of interest')

my_parser.add_argument('--input',
                       '-i',
                       action='store',
                       default='input/judgments.csv',
                       help='file containing space-separated word1 word2 sim_score')

my_parser.add_argument('--kind',
                       '-k',
                       action='store',
                       default='none',
                       help='the kind of input data to be processed: can be either STIMULI or JUDGMENTS')

my_parser.add_argument('--stimuli',
                       '-s',
                       action='store',
                       default='stimuli/',
                       help='output folder for stimuli')

args = my_parser.parse_args()

# create output folders if they do not exist yet

if not os.path.exists(args.stimuli):
    os.makedirs(args.stimuli)


def random_pairs(number_list):
    return [number_list[i] for i in random.sample(range(len(number_list)), 2)]


if args.kind == 'stimuli': # creates stimuli based on the verb-dObj files

	n = 6
	for verb in os.listdir(args.verbs):
		verb_label = verb.strip().split("output_nouns.")[1]
		dobj_list = []
		with open(os.path.join(args.verbs, verb), "r") as file_input, open(args.stimuli+"stimuli.list", "a") as stim_output:
			for line in file_input:
				if len(line)>0:
					dobj = line.strip().split(" ")[0]
					dobj_list.append(dobj)
			pairs = [random_pairs(dobj_list) for i in range(n)]
			for el in pairs:
				print(verb_label, el[0], el[1])
				stim_output.write(verb_label+" "+el[0]+" "+el[1]+"\n")



elif args.kind == 'judgments': # normalizes judgments and computes mean score for each verb

	df_judgs = pd.read_csv(args.input, sep=',')
	df_verbs = pd.read_csv(args.stimuli+"stimuli_eng.list", sep=' ', header=None, names=['verb','word1','word2'])
	df_full = pd.merge(df_verbs, df_judgs, on=['word1','word2'])
	numeric_cols = df_full.select_dtypes('int64').columns
	df_full_zscores = df_full[numeric_cols].apply(zscore) # computes within-subject z-scores
	df_full = df_full.assign(mean=df_full_zscores.mean(axis=1)) # adds mean z-score column
	df_full['judg']=(df_full['mean']-df_full['mean'].min())/(df_full['mean'].max()-df_full['mean'].min()) # normalizes z-scores to 0-1 range
	print(df_full)
	df_small = df_full[["verb", "judg"]] # subsets df_merge to get relevant columns
	df_aggr = df_small.groupby(['verb'],as_index=False).agg(lambda x : x.mean() if x.dtype=='float' else x.head(1))
	print(df_aggr)
	df_aggr.to_csv("simDobj_eng.csv", index=False, index_label=False, header=False, sep=' ')



else:
	print('ERROR: the --kind parameter should be either STIMULI or JUDGMENTS, lower case')
