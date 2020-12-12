********************************************************************************
******************************* CODING INSTRUCTIONS ****************************
********************************************************************************

Python files are written for Python 3.7. If you prefer to use Python 2.7, replace the
calls to "input" in utils.py with calls to "raw_input".

The steps that you should take to solve this problem set are as follows:

1) First, read through the problem set in Homework_2.pdf.  Solve the asymptotic
ordering problems and the recurrence relation problems, and place the answers
in the file Homework_2_Submission.tex according to the instructions given above.

2) Read through the four algorithms in the file algorithms.py.

3) Try to understand how each of the four algorithms works.  To improve your
understanding of the algorithms, we have provided a visualizer in the file
visualizer.html.  To run the visualizer on a particular matrix, enter the
matrix into the file problem.py, then run the Python script main.py, and
then open the file visualizer.html in a browser.  (Chrome is the
only browser guaranteed to work with the visualizer, but other modern browsers
are also likely to work.)

4) Analyze the runtime of each of the four algorithms.  You may find it useful
to look at the comments of some of the functions in peak.py and trace.py, in
which the runtimes are given.

5) Try to figure out which algorithms are correct.  You can try to do this by
running the algorithms on random matrices (generated using the Python script
generate.py), but keep in mind that random matrices have a large number of
peaks, and do not usually have a very interesting peak structure.  You may
have better luck examining the algorithms in detail, and constructing
counterexamples by hand.

6) Fill out the multiple-choice answers concerning correctness and runtime.

7) Construct one counterexample (a matrix where the algorithm returns an
incorrect answer) for each incorrect algorithm.

8) Figure out which of the correct algorithms is most efficient in terms
of asymptotic runtime, and write a proof of correctness for it.

9) Place ALL of your answers in the file Homework_2_Submission.tex, or write them
in a different application, and submit the problem set through Canvas. The submission
should be made as an image (pdf or png)

********************************************************************************
******************************** DIRECTORY CONTENTS ****************************
********************************************************************************

Homwork_2.pdf

    The file containing the assignment. 

Homework_2_Submission.tex

    The file that you should fill in with your responses if you choose to
    Write your solution in LaTeX.  Your answers should be entered in the 
    locations indicated, and you should not change anything outside of those
    locations. 

Homework_2_Critique.tex

    This is the file where you will fill in your critique of your own proof,
    (if you do your critique in LaTeX). 1 week after the assignment is due
    and the solutions have been released.  You should then copy and paste your
    proof into the designated location, and then provide a critique of your own
    proof afterwards.  The critique will be due 1 week after the rest of the
    assignment is due.

macros.tex

    This file contains definitions used in the other tex files; it must be
    in the same directory as the other tex files in order for pdflatex to
    work. You should not edit it, and are not responsible for its contents.

algorithms.py

    The Python file containing the four algorithms algorithm1, algorithm2,
    algorithm3, and algorithm4.  This is the file that you should spend most of
    your time looking at, to examine the four algorithms for correctness and
    efficiency.  You may assume that any bugs that might occur will occur in
    this file --- there is no need to examine any other files for correctness.

generate.py

    This Python file can be run to generate a random matrix.  With no
    arguments (such as when running the file in IDLE), the code generates a
    random matrix of size 10 x 10, with numbers between 0 and 200, and prompts
    the user for a place to save the result.  It also takes the following
    command-line arguments:

        python generate.py [<filename> [<rows> <columns> [<maximum>]]]

    The first command-line argument, <filename>, specifies the output file.
    The next two command-line arguments, <rows> and <columns>, must both be
    specified for either one to be read.  The fourth and final command-line
    argument, <maximum>, specifies the maximum number that can be generated
    in any cell of the matrix.

main.py

    When this Python file is run, it loads a peak problem from a file that
    the user specifies, and does the following:

        (1) Tests all four algorithms on the desired peak problem, and
            outputs the results.

        (2) Generates a record of the execution of all four algorithms, and
            outputs both the peak problem and the execution traces to the file
            trace.jsonp.  These traces can be examined by displaying the file
            visualizer.html in a browser.

    When run with no arguments (such as when run in IDLE), main.py prompts
    the user for a file name to read the matrix from, defaulting to problem.py.
    It also takes a single optional argument (the filename to read the matrix
    from):

        python main.py [<filename>]

peak.py

    This file contains the code for constructing a PeakProblem object, and a
    number of methods that can be called on such a problem.  These methods are
    used by the algorithms in algorithms.py.  Each of these functions has been
    labeled with its worst-case runtime, to simplify your analysis of the
    four algorithms.

problem.py

    Thie file contains a template for entering in a matrix.  This is also the
    default name for files read by main.py and written by generate.py.  The
    counterexamples that you submit should look like this, but instead of the
    matrix we have given you, you should find a matrix that causes at least one
    of the four algorithms to fail.

trace.py

    This file contains the code for recording information about the sequence of
    steps performed by an algorithm.  Just like peak.py, it has been annotated
    with runtimes to make it easier to analyze the four algorithms.

utils.py

    This file contains some methods used for getting file names from the user.
    None of the functions in this file are used by any of the algorithms, so
    you are not responsible for reading and understanding this code.

trace.jsonp

    This file contains an object representing the history of the execution of
    the four algorithms.  You need not read it yourself --- it will be written
    by main.py, and read by visualizer.html. Initially, it is blank; each time
    you run main.py, this file will be rewritten.

visualizer.html

    An HTML visualizer for the algorithm traces generated by main.py.  The
    visualizer is a tool for improving your understanding of how the algorithms
    work.  The included legend explains what each of the symbols mean.

********************************************************************************
****************************** COMPATIBILITY ***********************************
********************************************************************************

This code has been verified to work with Python 3.7.  It will work with Python 2.7
with one minor change: replace "input" with "raw_input" in utils.py.
