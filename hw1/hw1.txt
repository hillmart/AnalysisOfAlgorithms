CS 325-001, Algorithms, Spring 2023
HW1 - sorting and selection & divide-n-conquer: quicksort, binary search tree (BST), mergesort, number of inversions

Due electronically on flip on Monday 4/10 11:59pm. 
No late submission will be accepted.

Need to submit on flip: report.txt, msort.py, inversions.py and qsort.py.
inversions.py will be automatically graded for correctness (1%).

flip $ /nfs/farm/classes/eecs/spring2023/cs325-001/submit hw1 msort.py
flip $ /nfs/farm/classes/eecs/spring2023/cs325-001/submit hw1 inversions.py
flip $ /nfs/farm/classes/eecs/spring2023/cs325-001/submit hw1 qsort.py
flip $ /nfs/farm/classes/eecs/spring2023/cs325-001/submit hw1 report.txt
OR:
flip $ /nfs/farm/classes/eecs/spring2023/cs325-001/submit hw1 msort.py inversions.py qsort.py report.txt

Note:

0. You need an ENGR account if you don't already have one:
   https://it.engineering.oregonstate.edu/get-engr-account

1. You can ssh to flip machines from your own machine by:
   $ ssh access.engr.oregonstate.edu

   You're *highly* recommended to set up SSH keys to bypass Duo authentication and password:
   https://it.engineering.oregonstate.edu/ssh-keygen

   If you're using Windows, see these instructions on how to SSH:
   https://it.engineering.oregonstate.edu/accessing-unix-server-using-putty-ssh

2. You can add /nfs/farm/classes/eecs/spring2023/cs325-001/ to your $PATH:
   $ export PATH=$PATH:/nfs/farm/classes/eecs/spring2023/cs325-001/
   and add the above command to your ~/.bash_profile,
   so that you don't need to type it every time.

   (alternatively, you can use symbolic links or aliases to avoid typing the long path)

3. You can choose to submit each file separately, or submit them together (see above).

Textbooks for References:
[1] CLRS Ch. 9.2 and Ch. 12

0. Q: What's the best-case, worst-case, and average-case time complexities of quicksort.
   Briefly explain each case. No need to analyze the average-case.

1. Implement mergesort.
   
   >>> mergesort([4, 2, 5, 1, 6, 3])
   [1, 2, 3, 4, 5, 6]   
   
   Filename: msort.py
   
2. [WILL BE GRADED] Calculate the number of inversions in a list.
   Hint: use mergesort and "recursion with a byproduct".

   >>> num_inversions([4, 1, 3, 2])
   4
   >>> num_inversions([2, 4, 1, 3])
   3

   Filename: inversions.py
   Must run in O(nlogn) time, otherwise you will get "Time Limit Exceeded" in the grading system.

3. Buggy Qsort Revisited

   In the slides we showed a buggy version of qsort which is weird in an interesting way:
   it actually returns a binary search tree for the given array, rooted at the pivot:

   >>> from qsort import *
   >>> tree = sort([4,2,6,3,5,7,1,9])
   >>> tree
   [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]

   which encodes a binary search tree:

                      4
                    /   \
                  2       6
                 / \     / \
                1   3   5   7
                             \
                              9
   
   Now on top of that piece of code, add three functions: 
   * sorted(t): returns the sorted order (infix traversal)
   * search(t, x): returns whether x is in t
   * insert(t, x): inserts x into t (in-place) if it is missing, otherwise does nothing.

   >>> sorted(tree)
   [1, 2, 3, 4, 5, 6, 7, 9]
   >>> search(tree, 6)
   True
   >>> search(tree, 6.5)
   False
   >>> insert(tree, 6.5)
   >>> tree
   [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[[], 6.5, []], 7, [[], 9, []]]]]
   >>> insert(tree, 3)
   >>> tree
   [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[[], 6.5, []], 7, [[], 9, []]]]]

   Hint: both search and insert should depend on a helper function _search(tree, x) which 
   returns the subtree (a list) rooted at x when x is found, or the [] where x should 
   be inserted.

   e.g., 
   >>> tree = sort([4,2,6,3,5,7,1,9])        # starting from the initial tree
   >>> _search(tree, 3)
   [[], 3, []]
   >>> _search(tree, 0)
   []
   >>> _search(tree, 6.5)
   []
   >>> _search(tree, 0) is _search(tree, 6.5)
   False
   >>> _search(tree, 0) == _search(tree, 6.5)
   True
   
   Note the last two []'s are different nodes (with different memory addresses): 
   the first one is the left child of 1, while the second one is the left child of 7
   (so that insert is very easy).
   
   Filename: qsort.py
   
   Q: What are the time complexities for the operations implemented?

Debriefing (required!): --------------------------

1. Approximately how many hours did you spend on this assignment?
2. Would you rate it as easy, moderate, or difficult?
3. Did you work on it mostly alone, or mostly with other people?
4. How deeply do you feel you understand the material it covers (0%-100%)? 
5. Any other comments?

This section is intended to help us calibrate the homework assignments. 
Your answers to this section will *not* affect your grade; however, skipping it
will certainly do.
