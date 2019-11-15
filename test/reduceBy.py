# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

byType = R.prop('type')
sumValues = lambda acc, obj: acc + obj['val']

sumInput = [
    {'type': 'A', 'val': 10},
    {'type': 'B', 'val': 20},
    {'type': 'A', 'val': 30},
    {'type': 'A', 'val': 40},
    {'type': 'C', 'val': 50},
    {'type': 'B', 'val': 60}
]

class Test_reduceBy(unittest.TestCase):
    def test_splits_the_list_into_groups_according_to_the_grouping_function(self):
        grade = lambda score: \
            (
                'F' if score < 65
                else 'D' if score < 70
                else 'C' if score < 80
                else 'B' if score < 90
                else 'A'
            )
        students = [
            {'name': 'Abby', 'score': 84},
            {'name': 'Brad', 'score': 73},
            {'name': 'Chris', 'score': 89},
            {'name': 'Dianne', 'score': 99},
            {'name': 'Eddy', 'score': 58},
            {'name': 'Fred', 'score': 67},
            {'name': 'Gillian', 'score': 91},
            {'name': 'Hannah', 'score': 78},
            {'name': 'Irene', 'score': 85},
            {'name': 'Jack', 'score': 69}
        ]
        byGrade = lambda student: grade(student['score'] or 0)
        collectNames = lambda acc, student: acc.append(student['name']) or acc
        self.assertEqual(R.reduceBy(collectNames, [], byGrade, students), {
            'A': ['Dianne', 'Gillian'],
            'B': ['Abby', 'Chris', 'Irene'],
            'C': ['Brad', 'Hannah'],
            'D': ['Fred', 'Jack'],
            'F': ['Eddy']
        })
    
    def test_splits_the_list_into_mutation_free_groups(self):
        grade = lambda score: \
            (
                'F' if score < 65
                else 'D' if score < 70
                else 'C' if score < 80
                else 'B' if score < 90
                else 'A'
            )
        students = [
            {'name': 'Abby', 'score': 84},
            {'name': 'Brad', 'score': 73},
            {'name': 'Chris', 'score': 89},
            {'name': 'Dianne', 'score': 99},
            {'name': 'Eddy', 'score': 58},
            {'name': 'Fred', 'score': 67},
            {'name': 'Gillian', 'score': 91},
            {'name': 'Hannah', 'score': 78},
            {'name': 'Irene', 'score': 85},
            {'name': 'Jack', 'score': 69}
        ]
        byGrade = lambda student: grade(student['score'] or 0)
        collectNames = lambda acc, student: acc.append(student['name']) or acc
        self.assertEqual(R.reduceBy(collectNames, [], byGrade, students), {
            'A': ['Dianne', 'Gillian'],
            'B': ['Abby', 'Chris', 'Irene'],
            'C': ['Brad', 'Hannah'],
            'D': ['Fred', 'Jack'],
            'F': ['Eddy']
        })
    
    def test_returns_an_empty_object_if_given_an_empty_array(self):
        eq(self, R.reduceBy(sumValues, 0, byType, []), {})

    # def test_can_act_as_a_transducer(self):
    #     reduceToSumsBy = R.reduceBy(sumValues, 0)
    #     sumByType = reduceToSumsBy(byType)
    #     eq(self, R.into(
    #         {},
    #         R.compose(sumByType, R.map(R.adjust(1, R.multiply(10)))),
    #         sumInput
    #     ), {'A': 800, 'B': 800, 'C': 500})


if __name__ == '__main__':
    unittest.main()
