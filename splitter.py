# -*- coding: utf-8 -*-

import click
import json
import random


@click.command()
@click.argument('in_file', type=click.File())
@click.argument('out_file', type=click.File(mode='w'))
@click.option('--seed', default=0)
@click.option('--dev-size', default=0.1)
@click.option('--test-size', default=0.2)
@click.option('-v', '--version', default='0.0.1')
def main(in_file, out_file, seed, dev_size, test_size, version):
    dataset = json.load(in_file)

    doc_names = sorted(list(set([o['iitbDocName'] for o in dataset['annotations']])))

    dev_size = int(dev_size * len(doc_names))
    test_size = int(test_size * len(doc_names))

    random.seed(0)
    random.shuffle(doc_names)

    (dev_names, train_names) = (doc_names[:dev_size], doc_names[dev_size:])
    (test_names, train_names) = (train_names[:test_size], train_names[test_size:])

    dataset['documents'] = []
    for name in train_names:
        dataset['documents'].append(dict(iitbDocName=name, fold='train'))
    for name in dev_names:
        dataset['documents'].append(dict(iitbDocName=name, fold='dev'))
    for name in test_names:
        dataset['documents'].append(dict(iitbDocName=name, fold='test'))

    dataset['version'] = version
    json.dump(dataset, out_file, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()
