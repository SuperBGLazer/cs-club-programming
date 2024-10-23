
# Programming Challenges

Each person must fork this GitHub repo and create a folder in repo with their name. All the challenges must be stored in it. You are allowed to use any programming language that you want. When you are done with you challenges, create a pull request and merge it in with the main GitHub repo.

## Bad Grades Challenges (10-50)
In class we must make perfect program that are simple and easy to understand. For these challenges, we are doing the opposite of it. Points will be awarded based on how bad it looks or how inefficient it runs. Make sure to use bad programming practices.

1. **Complicated Hello World** (10-50)
   - Write a program that shows the message "Happy birthday Trenton" in the most complicated way possible. Do not just print it directly to the console.

2. **Add two numbers** (10-50)
   - Write a program that adds to number together that are from the user. Don't just add numbers together using `a + b = c`.

3. **List program** (10-50)
   - Write a program that allows users to add items to a list and display it back to the user.

4. **Average** (10-50)
   - Write a program that calculates the average of a list of numbers.

## Easy Challenges (10-20 points)

1. **Reverse and Replace** (10 pts)
   - Write a function that takes a string, reverses it, and replaces every vowel with its uppercase version.
   - Example: `"apple"` → `"ELppA"`

2. **Sum of Two Lists** (10 pts)
   - Write a program that takes two lists of integers of the same length and returns a list where each element is the sum of the corresponding elements from the input lists.
   - Example: `[1, 2, 3]` and `[4, 5, 6]` → `[5, 7, 9]`

3. **Odd Index Filter** (10 pts)
   - Write a function that takes a list and returns a new list containing only the elements at odd indices.
   - Example: `[10, 20, 30, 40, 50]` → `[20, 40]`

4. **String Pattern Generator** (10 pts)
   - Given an integer `n`, generate a string of alternating `'X'` and `'O'` characters of length `n`.
   - Example: `n=5` → `"XOXOX"`

5. **Count Digits and Letters** (15 pts)
   - Write a function that counts the number of digits and letters in a given string and returns the result as a tuple.
   - Example: `"abc123"` → `(3, 3)`

6. **Every Third Character** (15 pts)
   - Write a function that returns every third character from a given string, starting with the first character.
   - Example: `"abcdefghij"` → `"adgj"`

7. **Element Frequency Counter** (15 pts)
   - Write a program that takes a list of integers and returns a dictionary with each element and its frequency.
   - Example: `[1, 2, 2, 3, 1, 1]` → `{1: 3, 2: 2, 3: 1}`

8. **Multiply Digits** (15 pts)
   - Write a function that multiplies all the digits of an integer.
   - Example: `1234` → `24` (1 * 2 * 3 * 4)

9. **Rotate a List** (15 pts)
   - Write a function that rotates a list by `n` positions to the left.
   - Example: `[1, 2, 3, 4, 5]`, `n=2` → `[3, 4, 5, 1, 2]`

10. **Sum of Even Numbers** (15 pts)
   - Write a function that returns the sum of all even numbers in a given list of integers.
   - Example: `[1, 2, 3, 4, 5]` → `6`

11. **Nested List Flattening** (15 pts)
   - Write a function that flattens a list of lists into a single list.
   - Example: `[[1, 2], [3, 4]]` → `[1, 2, 3, 4]`

12. **Reverse Words in a Sentence** (20 pts)
   - Write a function that reverses the order of words in a sentence but keeps the letters in each word in the same order.
   - Example: `"Hello world"` → `"world Hello"`

13. **Unique Letters Only** (20 pts)
   - Write a program that removes all duplicate letters from a string, keeping only the first occurrence of each letter.
   - Example: `"programming"` → `"progamin"`

14. **Find Missing Number in List** (20 pts)
   - Given a list of integers from `1` to `n` where one number is missing, write a function that finds the missing number.
   - Example: `[1, 2, 4, 5]` → `3`

15. **Palindrome Checker** (20 pts)
   - Write a function that checks if a given string is a palindrome, ignoring spaces and punctuation.
   - Example: `"A man, a plan, a canal, Panama"` → `True`

16. **Longest Word in Sentence** (20 pts)
   - Write a function that finds the longest word in a sentence.
   - Example: `"The quick brown fox"` → `"quick"`

17. **List Without Min and Max** (20 pts)
   - Write a function that removes the smallest and largest values from a list of integers.
   - Example: `[4, 1, 6, 3, 5]` → `[4, 3, 5]`

18. **Sum of Divisors** (20 pts)
   - Write a function that returns the sum of all divisors of a given number.
   - Example: `12` → `28` (1 + 2 + 3 + 4 + 6 + 12)

19. **Second Largest Number** (20 pts)
   - Write a function that returns the second-largest number in a list of integers.
   - Example: `[3, 5, 1, 2, 4]` → `4`

20. **Rearrange List in Zigzag Order** (20 pts)
   - Write a function that rearranges the elements of a list so that the first element is less than the second, the second is greater than the third, and so on (zigzag order).
   - Example: `[4, 3, 7, 8, 6]` → `[3, 7, 4, 8, 6]`



## Medium Challenges (25-40 points)

21. **Prime Number Sieve** (25 pts)
   - Implement the Sieve of Eratosthenes to find all prime numbers up to a given number `n`.
   - Example: `n=10` → `[2, 3, 5, 7]`

22. **Matrix Transposition** (25 pts)
   - Write a function that transposes a 2D matrix (i.e., converts rows into columns and vice versa).
   - Example: `[[1, 2], [3, 4]]` → `[[1, 3], [2, 4]]`

23. **String Compression** (25 pts)
   - Write a function that compresses a string by replacing repeated characters with the character followed by the count of repetitions.
   - Example: `"aaabbcc"` → `"a3b2c2"`

24. **Fibonacci Sequence with Memoization** (25 pts)
   - Write a function that generates the `n`th Fibonacci number using memoization.
   - Example: `n=7` → `13`

25. **Check if a List is Monotonic** (25 pts)
   - Write a function to check if a list of integers is either strictly increasing or strictly decreasing.
   - Example: `[1, 2, 3, 4]` → `True`, `[4, 3, 2, 1]` → `True`

26. **Balanced Parentheses Checker** (30 pts)
   - Write a function that checks if a string of parentheses is balanced (e.g., `()` is balanced, but `((` is not).
   - Example: `"(()())"` → `True`

27. **Find Longest Substring Without Repeating Characters** (30 pts)
   - Write a function that finds the longest substring without repeating characters in a given string.
   - Example: `"abcabcbb"` → `"abc"`

28. **Binary Search Implementation** (30 pts)
   - Write a function that implements binary search to find the index of a target element in a sorted list of integers.
   - Example: `[1, 2, 3, 4, 5]`, `target=3` → `2`

29. **Find All Subsets of a Set** (30 pts)
   - Write a function that generates all subsets of a given set of integers.
   - Example: `{1, 2, 3}` → `{ {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} }`

30. **LCS (Longest Common Subsequence)** (30 pts)
   - Write a function that finds the longest common subsequence between two strings.
   - Example: `"abcde"` and `"ace"` → `"ace"`

31. **Clock Angle Calculator** (30 pts)
   - Write a program that calculates the angle between the hour and minute hands of an analog clock at a given time.
   - Example: `3:30` → `75 degrees`

32. **Decimal to Binary Converter** (30 pts)
   - Write a function that converts a decimal number to its binary representation.
   - Example: `10` → `"1010"`

33. **Merge Overlapping Intervals** (35 pts)
   - Write a function that merges overlapping intervals in a list of intervals.
   - Example: `[(1, 3), (2, 6), (8, 10)]` → `[(1, 6), (8, 10)]`

34. **Unique Triplets Summing to Zero** (35 pts)
   - Given a list of integers, find all unique triplets that sum up to zero.
   - Example: `[-1, 0, 1, 2, -1, -4]` → `[(-1, 0, 1), (-1, -1, 2)]`

35. **Rotate Matrix 90 Degrees** (35 pts)
   - Write a function that rotates a given square matrix by 90 degrees clockwise.
   - Example: `[[1, 2], [3, 4]]` → `[[3, 1], [4, 2]]`

36. **Longest Palindromic Substring** (35 pts)
   - Write a function that finds the longest palindromic substring in a given string.
   - Example: `"babad"` → `"bab"`

37. **Pascal's Triangle Generator** (35 pts)
   - Write a function that generates the first `n` rows of Pascal's Triangle.
   - Example: `n=5` → `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`

38. **Check if Binary Tree is Balanced** (40 pts)
   - Write a function that checks if a binary tree is height-balanced (i.e., the height of two subtrees of any node never differ by more than one).
   - Example: Binary tree input.

39. **Word Ladder** (40 pts)
   - Write a function that finds the shortest transformation sequence from a start word to an end word by changing only one letter at a time. Each transformed word must be a valid word in a given dictionary.
   - Example: `"hit"` to `"cog"`, dictionary = `["hot", "dot", "dog", "lot", "log", "cog"]` → `["hit", "hot", "dot", "dog", "cog"]`

40. **Sudoku Validator** (40 pts)
   - Write a function that checks if a completed Sudoku puzzle is valid.
   - Example: 9x9 grid input.



## Hard Challenges (45-50 points)

41. **N-Queens Problem** (45 pts)
   - Write a program that solves the N-Queens problem by placing N queens on an NxN chessboard such that no two queens attack each other.
   - Example: `n=4` → Solutions for 4x4 board.

42. **Tic-Tac-Toe AI** (45 pts)
   - Write a program that implements a Tic-Tac-Toe game and includes an AI that uses the minimax algorithm to play optimally.
   - Example: Playable game.

43. **Knight's Tour Problem** (45 pts)
   - Write a program that solves the Knight's Tour problem, where a knight must visit every square on a chessboard exactly once.
   - Example: 8x8 chessboard.

44. **Max Flow in a Network** (45 pts)
   - Write a function that calculates the maximum flow in a flow network using the Ford-Fulkerson algorithm.
   - Example: Network graph input.

45. **Regex Engine** (50 pts)
   - Write a simplified regex engine that supports `*` (zero or more), `.` (any character), and literal characters.
   - Example: `"a*b"` matches `"aaab"` and `"b"`.

46. **LRU Cache** (50 pts)
   - Implement an LRU (Least Recently Used) Cache with operations to insert, access, and evict items based on usage frequency.
   - Example: Cache input.

47. **Conway's Game of Life** (50 pts)
   - Write a program that simulates Conway's Game of Life on an infinite grid.
   - Example: Grid state input.

48. **Word Search Solver** (50 pts)
   - Write a function that solves a word search puzzle, finding all the words from a list in the puzzle grid.
   - Example: 2D grid input.

49. **Traveling Salesman Problem (TSP)** (50 pts)
   - Write a program that solves the Traveling Salesman Problem using a heuristic approach (e.g., greedy, simulated annealing).
   - Example: Graph input.

50. **Build a Compiler** (50 pts)
   - Write a simplified compiler that parses and evaluates expressions (e.g., arithmetic operations) in a custom language.
   - Example: Basic language input, evaluates mathematical expressions.

