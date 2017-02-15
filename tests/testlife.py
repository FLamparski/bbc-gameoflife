from gameoflife.Life import Life
import unittest

class testLife(unittest.TestCase):
	def test_no_interaction(self):
		emptyState = [
				[0,0,0],
				[0,0,0],
				[0,0,0]  ]
		testLife = Life()
		self.assertEqual(emptyState, testLife.evolve(emptyState))

	def test_underpopulation(self):
		s0 = [
			[0, 0, 0],
			[0, 1, 0],
			[0, 0, 0]
		]
		target = [
			[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]
		]
		testLife = Life()
		self.assertEqual(target, testLife.evolve(s0))

	def test_overpopulation(self):
		s0 = [
			[0, 1, 1],
			[1, 1, 1],
			[0, 0, 0]
		]
		target = [
			[0, 0, 1],
			[0, 0, 1],
			[1, 1, 0]
		]
		testLife = Life()
		self.assertEqual(target, testLife.evolve(s0))

	def test_survival(self):
		s0 = [
			[0, 1, 1],
			[0, 1, 1],
			[0, 0, 0]
		]
		target = [
			[0, 1, 1],
			[0, 1, 1],
			[0, 0, 0]
		]
		testLife = Life()
		self.assertEqual(target, testLife.evolve(s0))

	def test_create(self):
		s0 = [
			[0, 0, 1],
			[1, 0, 1],
			[0, 0, 0]
		]
		target = [
			[1, 1, 0],
			[1, 1, 0],
			[0, 0, 0]
		]
		testLife = Life()
		self.assertEqual(target, testLife.evolve(s0))


	def test_spinner(self):
		sA = [
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 1, 1, 1, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0]
		]
		sB = [
			[0, 0, 0, 0, 0],
			[0, 0, 1, 0, 0],
			[0, 0, 1, 0, 0],
			[0, 0, 1, 0, 0],
			[0, 0, 0, 0, 0]
		]
		testLife = Life()
		self.assertEqual(sB, testLife.evolve(sA))
		self.assertEqual(sA, testLife.evolve(sB))

	def test_glider(self):
		# Test based on this sequence:
		# https://camo.githubusercontent.com/f865db6a304d36aa7fef6c060729a2d635cd5c14/687474703a2f2f7777772d726f68616e2e736473752e6564752f7e72636172726574652f7465616368696e672f4d2d3539365f706174742f696d616765732f676c696465722e676966
		# The glider is a cell arrangement which keeps going indefinitely.
		t0 = [
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 1, 0, 0],
			[0, 1, 0, 1, 0, 0],
			[0, 0, 1, 1, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0]
		]
		t1 = [
			[0, 0, 0, 0, 0, 0],
			[0, 0, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0],
			[0, 0, 1, 1, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0]
		]
		t2 = [
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 1, 0, 0],
			[0, 0, 0, 0, 1, 0],
			[0, 0, 1, 1, 1, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0]
		]
		t3 = [
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 1, 0, 1, 0],
			[0, 0, 0, 1, 1, 0],
			[0, 0, 0, 1, 0, 0],
			[0, 0, 0, 0, 0, 0]
		]
		t4 = [
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0],
			[0, 0, 1, 0, 1, 0],
			[0, 0, 0, 1, 1, 0],
			[0, 0, 0, 0, 0, 0]
		]
		testLife = Life()
		self.assertEqual(t1, testLife.evolve(t0))
		self.assertEqual(t2, testLife.evolve(t1))
		self.assertEqual(t3, testLife.evolve(t2))
		self.assertEqual(t4, testLife.evolve(t3))
