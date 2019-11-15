# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_groupBy(unittest.TestCase):
    def test_splits_the_list_into_groups_according_to_the_grouping_function(self):
        grade = lambda score: \
            'F' if score < 65 \
            else 'D' if score < 70 \
            else 'C' if score < 80 \
            else 'B' if score < 90 \
            else 'A'
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
        self.assertEqual(R.groupBy(byGrade, students), {
            'A': [{'name': 'Dianne', 'score': 99}, {'name': 'Gillian', 'score': 91}],
            'B': [{'name': 'Abby', 'score': 84}, {'name': 'Chris', 'score': 89}, {'name': 'Irene', 'score': 85}],
            'C': [{'name': 'Brad', 'score': 73}, {'name': 'Hannah', 'score': 78}],
            'D': [{'name': 'Fred', 'score': 67}, {'name': 'Jack', 'score': 69}],
            'F': [{'name': 'Eddy', 'score': 58}]
        })
    
    def test_returns_an_empty_object_if_given_an_empty_array(self):
        eq(self, R.groupBy(R.prop('x'), []), {})

    # def test_dispatches_on_transformer_objects_in_list_position(self):
    #     byType = R.prop('type')
    #     xf = {
    #         '@@transducer/init': lambda :{ {} },
    #         '@@transducer/result': lambda x:{ x },
    #         '@@transducer/step': R.mergeRight
    #     }
    #     eq(self, _isTransformer(R.groupBy(byType, xf)), True)


if __name__ == '__main__':
    unittest.main()
