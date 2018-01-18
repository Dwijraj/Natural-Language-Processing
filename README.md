# Natural-Language-Processing
Natural Language Processing, or NLP for short, is broadly defined as the automatic manipulation of natural language, like speech and text, by software.

Problems of NLP:-
Word Representation and Meaning.

Text Classification.

Language Modeling.

Machine Translation.

Speech Recognition.

and more

This repository contains a guide of how NLP problems are to be dealt with.

# Using Bag of Words Model

			|       Observation         |
			|---------------------------|
			| Encoder | CountVectorizer |
			|---------|-----------------|
			| Max Features | 1500		|
			| Classifier   |	SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',max_iter=-1, probability=False, random_state=None, shrinking=True,tol=0.001, verbose=False)	|
			| Testing with stemming | 81.375 |
			| Training with Stemming  | 88.916 |
			| Training without Stemming| 88|
			| Testing without stemming|	80.375
 	