from unittest import TestCase
from math import sqrt
import q4.answer as q4
#import q6.answer as q6
import q1.answer as q1
import q3.answer as q3
import q5.answer as q5

from q1.answer import Reading, distance
from q5.answer import create_grid, enumerate_clockwise, Position, Grid, Direction

import pyximport; 
pyximport.install()
from q4.canswer import ireplace


class CythonTests(TestCase):
    def test_no_replace(self):
        a_stirng = "abcd"
        ireplace(a_stirng)
        self.assertEqual(a_stirng, "abcd")

    def test_replace_at_end(self):
        a_stirng = "abcdd"
        ireplace(a_stirng)
        self.assertEqual(a_stirng, "abcd\0")

    def test_replace(self):
        a_stirng = "ab cd"
        ireplace(a_stirng)
        self.assertEqual(a_stirng, "abcd\0")

    def test_replace_consecutive(self):
        a_stirng = "abbcd"
        ireplace(a_stirng)
        self.assertEqual(a_stirng, "abcd\0")
    def test_replace_consecutive_and_spaces(self):
        a_stirng = "ab bcd"
        ireplace(a_stirng)
        self.assertEqual(a_stirng, "abcd\0\0")



#1 2 3
#4 5 6
#7 8 9
#from q6.answer import node
class QFiveTests(TestCase):
    def setUp(self):
        self.sample_grid_string ='1 2 3\n4 5 6\n7 8 9'
        self.grid = Grid()


    def test_initial_direction_is_right(self):
        self.assertEqual(Direction().name, "right")

    def test_next_direction_is_down(self):
        direction = Direction()
        direction.next()
        self.assertEqual(direction.name, "down")

    def test_next_direction_is_circular(self):
        direction = Direction("up")
        direction.next()
        self.assertEqual(direction.name, "right")

    def test_name_links_to_offset(self):
        self.assertEqual(Direction().offset, (1,0))

    def test_apply_offset_from_start(self):
        direction = Direction()
        next_position = Position(0,0).apply_offset(direction.offset)
        self.assertEqual(next_position.x, 1)
        self.assertEqual(next_position.y, 0)

    def test_create_sample_grid(self):
        grid = create_grid(self.sample_grid_string)
        self.assertEqual(grid.get_position(Position(0,0)).value, "1")
        self.assertEqual(grid.get_position(Position(1,0)).value, "2")
        self.assertEqual(grid.get_position(Position(1,1)).value, "5")
        self.assertEqual(grid.get_position(Position(2,2)).value, "9")

    def test_get_position_finds_from_cells(self):
        grid = Grid()
        position_to_find = Position(1,2, 5)
        grid.cells.append( position_to_find )
        self.assertEqual(position_to_find.value, grid.get_position(Position(1,2)).value)

    def test_next_position_right(self):
        grid = create_grid(self.sample_grid_string)
        self.assertEqual(grid.next_position(Position(0,0), Direction("right")) , Position(1,0))

    def test_full_solution(self):
        grid = create_grid(self.sample_grid_string)
        answer_list = [ int(position.value) for position in enumerate_clockwise(grid) ]
        self.assertEqual(answer_list, [1,2,3,6,9,8,7,4,5])


#is this question code word for write a c extension ?
class QFourTests(TestCase):
    def test_removes_spaces(self):
        self.assertEqual(q4.compact("these are some words"), "thesearesomewords")
    def test_removes_dups(self):
        self.assertEqual(q4.compact("fizzbbuzzstuf"), "fizbuzstuf")
    def test_fullcompact(self):
        self.assertEqual(q4.compact("abb cddpddef gh"), "abcdpdefgh")
    def test_fullcompact_double_letter_at_the_end(self):
        self.assertEqual(q4.compact("abb cddpddef fghh"), "abcdpdefgh")


class QOneTests(TestCase):
    def test_full_solution(self):
        self.assertEqual(q1.find([Reading(0,0,5), Reading(6,8,5)]), [(3,4)])

    def test_two_solutions(self):
        positions = q1.find([Reading(-.5,0,1), Reading(.5,0,1)])
        self.assertTrue((0,1.0/2*sqrt(3)) in positions)
        self.assertTrue((0,-1.0/2*sqrt(3)) in positions)

    def test_empty_list(self):
        self.assertEqual(q1.find([Reading(0,0,5), Reading(6,8.1,5)]), [])

    def test_distance(self):
        self.assertEqual(distance(Reading(0,0,0), Reading(3,4,0)), 5)

class QThreeTests(TestCase):
    def test_flatten_chains_two_pointer_sets(self):
        self.assertEqual(len(q3.flatten_chains('7,2,3,4,5,6,-1,0')), 2)

    def test_flatten_chains_three_pointer_sets(self):
        self.assertEqual(len(q3.flatten_chains('7,2,2,4,5,6,-1,0')), 3)

    def test_flatten_chains_cycles(self):
        self.assertEqual(q3.number_cycles(q3.flatten_chains('7,2,3,4,5,6,-1,0')), 1)

    def test_full_solution(self):
        self.assertEqual(q3.number_cycles(q3.flatten_chains('7,2,3,4,5,6,-1,0')), 1)

    def test_full_solution_with_double_tail(self):
        self.assertEqual(q3.number_cycles(q3.flatten_chains('7,2,2,4,5,6,-1,0')), 1)

#class QSixTests(TestCase):
#    def test_node_crooked_tree_has_one_child(self):
#        the_node = node("1","2")
#        self.assertTrue(len(the_node.childern), 1)
#    def test_simplest_tree(self):
#        self.assertEqual(q6.createTree("4"), {"4":None})
#
#    def test_create_simple_tree(self):
#        self.assertEqual(q6.createTree("4,2,5"), node("4", "2", "5"))
#        #self.assertEqual(q6.createTree("4,2,5"), {"4":{"2":None, "5":None}})
#
#    def test_create_multi_level_tree(self):
#        self.assertEqual(q6.createTree("1,5,4,0,3,2,5"),
#            {"1": [
#                {"5":[
#                    "0",
#                    "3"]},
#                {"4":[
#                    "2",
#                    "5"]} ]
#            })
#            #node("1",
#            #    node("5",
#            #        node("0", "3")),
#            #    node("4",
#            #        node("2", "5"))
#            #)
#
#
#    def test_is_sub_tree(self):
#        self.assertTrue(q6.isSubTree("1,5,4,0,3,2,5", "4,2,5"))
#
#    def test_is_multilevel_subtree(self):
#        self.assertTrue(q6.isSubTree("1,5,4,0,3,2,5,0,0,0,0,0,0,0,8", "4,2,5"))
#
#    def test_is_simple_crooked_sub_tree(self):
#        self.assertTrue(q6.isSubTree("4,2,5", "4, 5"))
#
#    def test_is_croocked_sub_tree(self):
#        self.assertTrue(q6.isSubTree("1,5,4,0,3,2,5", "4,5"))
