"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Xiaoze Sun.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # done: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')
    #test1
    expected = 0.13416
    answer = sum_cosines(3)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)
    # test2
    expected = 1.54030
    answer = sum_cosines(1)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)
    # test3
    expected = -0.23581
    answer = sum_cosines(5)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

def sum_cosines(n):
    total = 0
    num=n+1
    for k in range(num):
        total = total + math.cos(k)

    return total
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # ------------------------------------------------------------------
    # done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # done: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')
    # test1
    expected = 11.854408
    answer = sum_square_roots(5)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)
    # test2
    expected = 15.31850
    answer = sum_square_roots(6)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)
    # test3
    expected = 19.06016
    answer = sum_square_roots(7)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

def sum_square_roots(n):
    total = 0
    i = 0
    k=0
    while i <= n:
        total=total+math.sqrt(k)
        i=i+1
        k=k+2
    return total
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # ------------------------------------------------------------------
    # done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
