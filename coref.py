import json, spacy, neuralcoref
from flask import Flask, jsonify, request

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)

@app.route('/coref', methods=['POST'])
def coref_resolution():

	text = request.form['text']
	doc = nlp(text)

	coreference_clusters = []

	for cc in doc._.coref_clusters: 

		cchain_obj = {'chain': [], 'main': {
                	'start': cc.main.start_char,
                	'end': cc.main.end_char,
	        	'text': cc.main.text,
		}}

		for m in cc.mentions: 
			_cchain_mention = {
                        	'start': m.start_char,
	                        'end': m.end_char,
        	                'text': m.text
                    	}

			cchain_obj['chain'].append(_cchain_mention)

		coreference_clusters.append(cchain_obj)

	return jsonify({'coref': coreference_clusters})

if __name__ == '__main__': app.run(host='0.0.0.0', port=8150)

