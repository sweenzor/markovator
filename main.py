import json

from markovate import Markovator

import sys
import random

def create_markovated_tweet(tweets, max_length, unwanted_markovations=[]):
    tweets_texts = map(lambda t: t.strip(), tweets)
    markovator = Markovator()
    markovator.parse_sentences(tweets_texts)
    markovation = markovator.markovate()

    unwanted_markovations.extend(tweets_texts)

    count = 0
    while len(markovation) > max_length or markovation in unwanted_markovations:
        markovation = markovator.markovate()
        count += 1
        if count > 20:
            return None

    return markovation

if __name__ == '__main__':

    with open('roguelazer', 'r') as textfile:
        text = [line for line in textfile.readlines()]

        processed_text = []
        for t in text:
            processed_text.append(t.split('<Roguelazer> ')[-1])

    print create_markovated_tweet(processed_text, 140)
