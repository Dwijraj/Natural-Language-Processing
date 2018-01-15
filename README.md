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

#Using Bag of Words Model
	
	<table>
		<td>
			<tr>
				Encoder
			</tr>
			<tr>
				CountVectorizer
			</tr>	
		</td>
		<td>
			<tr>
				Max Features
			</tr>
			<tr>
				1500
			</tr>	
		</td>
		<td>
			<tr>
				Classifier
			</tr>
			<tr>
				SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
					decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
					max_iter=-1, probability=False, random_state=None, shrinking=True,
					tol=0.001, verbose=False)
			</tr>	
		</td>
		<td>
			<tr>
				Training Accuracy with Stemming
			</tr>
			<tr>
				88.91666666666667
			</tr>	
		</td>
		<td>
			<tr>
				Testing Accuracy with Stemming
			</tr>
			<tr>
				0.81375
			</tr>	
		</td>
		<td>
			<tr>
				Training Accuracy without Stemming
			</tr>
			<tr>
				88
			</tr>	
		</td>
		<td>
			<tr>
				Testing Accuracy without Stemming
			</tr>
			<tr>
				80.375
			</tr>	
		</td>
	
	</table>
	