from __future__ import unicode_literals
import pytest

from spacy.strings import StringStore
from spacy.matcher import *
from spacy.attrs import ORTH
from spacy.tokens.doc import Doc
from spacy.vocab import Vocab


@pytest.fixture
def matcher(EN):
    specs = []
    for string in ['JavaScript', 'Google Now', 'Java']:
        spec = []
        for orth_ in string.split():
            spec.append([(ORTH, EN.vocab.strings[orth_])])
        specs.append((spec, EN.vocab.strings['product']))
    return Matcher(specs)


def test_compile(matcher):
    assert matcher.n_patterns == 3

def test_no_match(matcher, EN):
    tokens = EN('I like cheese')
    assert matcher(tokens) == []


def test_match_start(matcher, EN):
    tokens = EN('JavaScript is good')
    assert matcher(tokens) == [(EN.vocab.strings['product'], 0, 1)]


def test_match_end(matcher, EN):
    tokens = EN('I like Java')
    assert matcher(tokens) == [(EN.vocab.strings['product'], 2, 3)]


def test_match_middle(matcher, EN):
    tokens = EN('I like Google Now best')
    assert matcher(tokens) == [(EN.vocab.strings['product'], 2, 4)]


def test_match_multi(matcher, EN):
    tokens = EN('I like Google Now and Java best')
    assert matcher(tokens) == [(EN.vocab.strings['product'], 2, 4),
                               (EN.vocab.strings['product'], 5, 6)]

def test_dummy():
    pass