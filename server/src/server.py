#! /usr/bin/python

def warn(*args, **kwargs):
    pass #the trick to switch off deprecation warnings
import warnings
warnings.warn = warn

import numpy as np
import azimuth.model_comparison

def predict(seq, aa_cut=None, percent_peptide=None, model=None, model_file=None, pam_audit=False, length_audit=False, learn_options_override=None):
    """
    Args:
        seq: numpy array of 30 nt sequences.
        aa_cut: numpy array of amino acid cut positions (optional).
        percent_peptide: numpy array of percent peptide (optional).
        model: model instance to use for prediction (optional).
        model_file: file name of pickled model to use for prediction (optional).
        pam_audit: check PAM of each sequence.
        length_audit: check length of each sequence.
        learn_options_override: a dictionary indicating which learn_options to override (optional).
    Returns: a numpy array of predictions.
    """
    if type(seq).__module__ != np.__name__:
        seq = np.array(seq)

    if type(aa_cut).__module__ != np.__name__:
        if aa_cut:
            aa_cut = np.array(aa_cut)
        else:
            aa_cut = None

    if type(percent_peptide).__module__ != np.__name__:
        if aa_cut:
            percent_peptide = np.array(percent_peptide)
        else:
            percent_peptide = None
    predictions = azimuth.model_comparison.predict(seq, aa_cut, percent_peptide, model, model_file, pam_audit, length_audit, learn_options_override)
    result = [ (seq[i], prediction) for i, prediction in enumerate(predictions)]
    return result


from flask import Flask
from flask import request
from flask.json import jsonify

app = Flask(__name__)

@app.route('/')
def info():
    sequence = request.args.get('sequence')
    if(sequence):
        seqs = np.array([sequence])
        result = predict(seqs, model_file="models/V3_model_full.pickle")
        return jsonify({'scores': result})
    else:
        return 'Please, provide a sequence! host:port?sequence=<your sequence>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)
