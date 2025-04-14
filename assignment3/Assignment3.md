### GE2324 Assignment1
LIU Hengche 57854329

#### Q1:
**(a)**:
```
Formula used: d(p, q) = square root of ((q1 - p1)^2 + (q2 - p2)^2)
Euclidean Distance Matrix:
      A     B     C     D     E     F     G     H     I     J
A  0.00  1.70  3.11  6.19  4.03  7.05  5.80  6.53  8.63  6.96
B  1.70  0.00  3.67  4.49  2.47  5.35  5.28  5.60  7.20  6.00
C  3.11  3.67  0.00  7.03  4.51  7.78  3.53  4.84  7.86  5.28
D  6.19  4.49  7.03  0.00  2.52  0.86  6.08  5.12  4.16  5.23
E  4.03  2.47  4.51  2.52  0.00  3.30  4.17  3.81  4.75  4.11
F  7.05  5.35  7.78  0.86  3.30  0.00  6.55  5.42  3.86  5.46
G  5.80  5.28  3.53  6.08  4.17  6.55  0.00  1.62  5.03  1.97
H  6.53  5.60  4.84  5.12  3.81  5.42  1.62  0.00  3.42  0.45
I  8.63  7.20  7.86  4.16  4.75  3.86  5.03  3.42  0.00  3.14
J  6.96  6.00  5.28  5.23  4.11  5.46  1.97  0.45  3.14  0.00
```
**(b)**:
```
Manhattan Distance Matrix:
      A    B     C    D    E    F    G    H     I    J
A   0.0  2.3   4.3  8.5  5.7  9.7  6.0  7.7  11.9  8.3
B   2.3  0.0   5.0  6.2  3.4  7.4  6.7  5.8   9.6  6.0
C   4.3  5.0   0.0  7.6  4.8  8.8  4.7  6.8  11.0  7.4
D   8.5  6.2   7.6  0.0  2.8  1.2  8.1  7.2   4.8  7.4
E   5.7  3.4   4.8  2.8  0.0  4.0  5.9  5.0   6.2  5.2
F   9.7  7.4   8.8  1.2  4.0  0.0  8.3  7.4   5.0  7.6
G   6.0  6.7   4.7  8.1  5.9  8.3  0.0  2.1   6.3  2.7
H   7.7  5.8   6.8  7.2  5.0  7.4  2.1  0.0   4.2  0.6
I  11.9  9.6  11.0  4.8  6.2  5.0  6.3  4.2   0.0  3.6
J   8.3  6.0   7.4  7.4  5.2  7.6  2.7  0.6   3.6  0.0
Formula used: d(p, q) = absolute value of (q1 - p1) + absolute value of (q2 - p2)
```

**(c)**
```
Detailed steps of hierarchical clustering (single - linkage) using Euclidean distance:
Step 1: merged clusters: {H} and {J}, distance: 0.45
Step 2: merged clusters: {D} and {F}, distance: 0.86
Step 3: merged clusters: {G} and {H, J}, distance: 1.62
Step 4: merged clusters: {A} and {B}, distance: 1.70
Step 5: merged clusters: {E} and {A, B}, distance: 2.47
Step 6: merged clusters: {D, F} and {A, B, E}, distance: 2.52
Step 7: merged clusters: {C} and {A, B, D, E, F}, distance: 3.11
Step 8: merged clusters: {I} and {G, H, J}, distance: 3.14
Step 9: merged clusters: {A, B, C, D, E, F} and {G, H, I, J}, distance: 3.53

Detailed steps of hierarchical clustering (single - linkage) using Manhattan distance:
Merge steps:
Step 1: merged clusters: {H} and {J}, distance: 0.60
Step 2: merged clusters: {D} and {F}, distance: 1.20
Step 3: merged clusters: {G} and {H, J}, distance: 2.10
Step 4: merged clusters: {A} and {B}, distance: 2.30
Step 5: merged clusters: {E} and {D, F}, distance: 2.80
Step 6: merged clusters: {A, B} and {D, E, F}, distance: 3.40
Step 7: merged clusters: {I} and {G, H, J}, distance: 3.60
Step 8: merged clusters: {C} and {A, B, D, E, F}, distance: 4.30
Step 9: merged clusters: {G, H, I, J} and {A, B, C, D, E, F}, distance: 4.70
```
![Euclidean hierarchy trees](Euclidean.png)
![Manhattan hierarchy trees](Manhattan.png)

#### Q2:
**(a)**
```
Step 1: Count support for single itemsets
Single itemset counts: {'A': 4, 'B': 4, 'C': 3, 'E': 3, 'D': 2}
Frequent single itemsets (min support = 2): {'A': 4, 'B': 4, 'C': 3, 'E': 3, 'D': 2}

Step 2: Generate candidate itemsets of size 2
Candidate itemsets of size 2: {('A', 'E'), ('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('B', 'D'), ('D', 'E'), ('A', 'C'), ('B', 'E'), ('A', 'D')}
Candidate counts: {('A', 'E'): 3, ('A', 'B'): 2, ('B', 'C'): 3, ('C', 'D'): 1, ('C', 'E'): 0, ('B', 'D'): 1, ('D', 'E'): 1, ('A', 'C'): 1, ('B', 'E'): 1, ('A', 'D'): 1}
Frequent candidate itemsets (min support = 2): {('A', 'E'): 3, ('A', 'B'): 2, ('B', 'C'): 3}

Step 3: Generate candidate itemsets of size 3
Candidate itemsets of size 3: {(('A', 'B'), ('A', 'E'), ('B', 'C'))}
Candidate counts: {(('A', 'B'), ('A', 'E'), ('B', 'C')): 0}
Frequent candidate itemsets (min support = 2): {}

Frequent Itemsets (min support = 2):
{'A'}
{'B'}
{'C'}
{'E'}
{'D'}
{'A', 'E'}
{'B', 'A'}
{'B', 'C'}
```

**(b)**
- Results:
```
Summary of Association Rules (min support = 0.3333333333333333, min confidence = 0.6):
Found 4 rules:
Rule: {'A'} -> {'E'}, Support: 0.50, Confidence: 0.75
Rule: {'E'} -> {'A'}, Support: 0.50, Confidence: 1.00
Rule: {'B'} -> {'C'}, Support: 0.50, Confidence: 0.75
Rule: {'C'} -> {'B'}, Support: 0.50, Confidence: 1.00
```
- Steps:
```
Single Itemsets and their Support:
Item: A, Support: 0.67
Item: B, Support: 0.67
Item: C, Support: 0.50
Item: E, Support: 0.50
Item: D, Support: 0.33

Generating Association Rules:

Examining itemset: {'A'}

Examining itemset: {'B'}

Examining itemset: {'C'}

Examining itemset: {'E'}

Examining itemset: {'D'}

Examining itemset: {'D', 'B'}
  Antecedent: frozenset({'D'}), Consequent: frozenset({'B'})
  Support(A ∪ B): 0.17, Support(A): 0.33, Confidence: 0.50
  Antecedent: frozenset({'B'}), Consequent: frozenset({'D'})
  Support(A ∪ B): 0.17, Support(A): 0.67, Confidence: 0.25

Examining itemset: {'A', 'E'}
  Antecedent: frozenset({'A'}), Consequent: frozenset({'E'})
  Support(A ∪ B): 0.50, Support(A): 0.67, Confidence: 0.75
  Rule passed: frozenset({'A'}) -> frozenset({'E'}), Support: 0.50, Confidence: 0.75
  Antecedent: frozenset({'E'}), Consequent: frozenset({'A'})
  Support(A ∪ B): 0.50, Support(A): 0.50, Confidence: 1.00
  Rule passed: frozenset({'E'}) -> frozenset({'A'}), Support: 0.50, Confidence: 1.00

Examining itemset: {'B', 'C'}
  Antecedent: frozenset({'B'}), Consequent: frozenset({'C'})
  Support(A ∪ B): 0.50, Support(A): 0.67, Confidence: 0.75
  Rule passed: frozenset({'B'}) -> frozenset({'C'}), Support: 0.50, Confidence: 0.75
  Antecedent: frozenset({'C'}), Consequent: frozenset({'B'})
  Support(A ∪ B): 0.50, Support(A): 0.50, Confidence: 1.00
  Rule passed: frozenset({'C'}) -> frozenset({'B'}), Support: 0.50, Confidence: 1.00

Examining itemset: {'B', 'A'}
  Antecedent: frozenset({'B'}), Consequent: frozenset({'A'})
  Support(A ∪ B): 0.33, Support(A): 0.67, Confidence: 0.50
  Antecedent: frozenset({'A'}), Consequent: frozenset({'B'})
  Support(A ∪ B): 0.33, Support(A): 0.67, Confidence: 0.50

Examining itemset: {'D', 'E'}
  Antecedent: frozenset({'D'}), Consequent: frozenset({'E'})
  Support(A ∪ B): 0.17, Support(A): 0.33, Confidence: 0.50
  Antecedent: frozenset({'E'}), Consequent: frozenset({'D'})
  Support(A ∪ B): 0.17, Support(A): 0.50, Confidence: 0.33

Examining itemset: {'D', 'A'}
  Antecedent: frozenset({'D'}), Consequent: frozenset({'A'})
  Support(A ∪ B): 0.17, Support(A): 0.33, Confidence: 0.50
  Antecedent: frozenset({'A'}), Consequent: frozenset({'D'})
  Support(A ∪ B): 0.17, Support(A): 0.67, Confidence: 0.25

Examining itemset: {'A', 'C'}
  Antecedent: frozenset({'A'}), Consequent: frozenset({'C'})
  Support(A ∪ B): 0.17, Support(A): 0.67, Confidence: 0.25
  Antecedent: frozenset({'C'}), Consequent: frozenset({'A'})
  Support(A ∪ B): 0.17, Support(A): 0.50, Confidence: 0.33

Examining itemset: {'D', 'C'}
  Antecedent: frozenset({'D'}), Consequent: frozenset({'C'})
  Support(A ∪ B): 0.17, Support(A): 0.33, Confidence: 0.50
  Antecedent: frozenset({'C'}), Consequent: frozenset({'D'})
  Support(A ∪ B): 0.17, Support(A): 0.50, Confidence: 0.33

Examining itemset: {'B', 'E'}
  Antecedent: frozenset({'B'}), Consequent: frozenset({'E'})
  Support(A ∪ B): 0.17, Support(A): 0.67, Confidence: 0.25
  Antecedent: frozenset({'E'}), Consequent: frozenset({'B'})
  Support(A ∪ B): 0.17, Support(A): 0.50, Confidence: 0.33

```

**(c)**
- Results
```
Final Interests of the Rules:
Rule: frozenset({'A'}) -> frozenset({'E'}), Interest: 0.25
Rule: frozenset({'E'}) -> frozenset({'A'}), Interest: 0.33
Rule: frozenset({'B'}) -> frozenset({'C'}), Interest: 0.25
Rule: frozenset({'C'}) -> frozenset({'B'}), Interest: 0.33
```
- Steps
```
A -> E: conf = 0.75, E expec = 0.50, so interest = | conf - expec | = 0.25
E -> A: conf = 1.00, A expec = 0.67, so interest = | conf - expec | = 0.33
B -> C: conf = 0.75, C expec = 0.50, so interest = | conf - expec | = 0.25
C -> B: conf = 1.00, B expec = 0.67, so interest = | conf - expec | = 0.33
```

#### Q3
**(a)**
- Results:
```
Document 1: {'mat and looks', 'on the mat', 'the mat and', 'and looks very', 'sits on the', 'the cat sits', 'looks very calm', 'cat sits on'}
Document 2: {'dog plays nearby', 'on the mat', 'sits calmly on', 'the dog plays', 'calmly on the', 'the cat sits', 'while the dog', 'mat while the', 'cat sits calmly', 'the mat while'}
Document 3: {'the cat watches', 'the grass the', 'on the grass', 'cat watches quietly', 'plays joyfully as', 'dog plays joyfully', 'grass the dog', 'as the cat', 'joyfully as the', 'the dog plays'}
```

- Steps:
```
Processing Document 1...
Normalized Text: 'the cat sits on the mat and looks very calm'
3-Shingles: {'mat and looks', 'on the mat', 'the mat and', 'and looks very', 'sits on the', 'the cat sits', 'looks very calm', 'cat sits on'}

Processing Document 2...
Normalized Text: 'the cat sits calmly on the mat while the dog plays nearby'
3-Shingles: {'dog plays nearby', 'on the mat', 'sits calmly on', 'the dog plays', 'calmly on the', 'the cat sits', 'while the dog', 'mat while the', 'cat sits calmly', 'the mat while'}

Processing Document 3...
Normalized Text: 'on the grass the dog plays joyfully as the cat watches quietly'
3-Shingles: {'the cat watches', 'the grass the', 'on the grass', 'cat watches quietly', 'plays joyfully as', 'dog plays joyfully', 'grass the dog', 'as the cat', 'joyfully as the', 'the dog plays'}

Final 3-Shingle Results:
Document 1: {'mat and looks', 'on the mat', 'the mat and', 'and looks very', 'sits on the', 'the cat sits', 'looks very calm', 'cat sits on'}
Document 2: {'dog plays nearby', 'on the mat', 'sits calmly on', 'the dog plays', 'calmly on the', 'the cat sits', 'while the dog', 'mat while the', 'cat sits calmly', 'the mat while'}
Document 3: {'the cat watches', 'the grass the', 'on the grass', 'cat watches quietly', 'plays joyfully as', 'dog plays joyfully', 'grass the dog', 'as the cat', 'joyfully as the', 'the dog plays'}
```

**(b)**
- Results
```
Jaccard Similarity Matrix:
Similarity between Document 1 and Document 2: 0.1250
Similarity between Document 1 and Document 3: 0.0000
Similarity between Document 2 and Document 3: 0.0526

Final Jaccard Similarity Matrix:
[0, 0.125, 0.0]
[0.125, 0, 0.05263157894736842]
[0.0, 0.05263157894736842, 0]
```
- Steps
```
Unique Shingles Across All Documents:
{'cat watches quietly', 'on the mat', 'the mat and', 'and looks very', 'sits on the', 'dog plays joyfully', 'calmly on the', 'looks very calm', 'grass the dog', 'joyfully as the', 'cat sits on', 'mat while the', 'the dog plays', 'the mat while', 'dog plays nearby', 'mat and looks', 'the cat watches', 'the grass the', 'on the grass', 'sits calmly on', 'the cat sits', 'as the cat', 'while the dog', 'cat sits calmly', 'plays joyfully as'}

Shingle Matrix (Rows: Shingles, Columns: Documents):
cat watches quietly: [0, 0, 1]
on the mat: [1, 1, 0]
the mat and: [1, 0, 0]
and looks very: [1, 0, 0]
sits on the: [1, 0, 0]
dog plays joyfully: [0, 0, 1]
calmly on the: [0, 1, 0]
looks very calm: [1, 0, 0]
grass the dog: [0, 0, 1]
joyfully as the: [0, 0, 1]
cat sits on: [1, 0, 0]
mat while the: [0, 1, 0]
the dog plays: [0, 1, 1]
the mat while: [0, 1, 0]
dog plays nearby: [0, 1, 0]
mat and looks: [1, 0, 0]
the cat watches: [0, 0, 1]
the grass the: [0, 0, 1]
on the grass: [0, 0, 1]
sits calmly on: [0, 1, 0]
the cat sits: [1, 1, 0]
as the cat: [0, 0, 1]
while the dog: [0, 1, 0]
cat sits calmly: [0, 1, 0]
plays joyfully as: [0, 0, 1]
```

**(c)**
- Results:
```
Signature Matrix:
3 1 1 2
1 1 3 3
2 3 1 1
2 1 1 1 

Jaccard Similarity
                    1-2     1-3     1-4     2-3     2-4     3-4
sim(ci, cj)         0.167   0.4     0.33    0       0.4     0.4
sim(sigi, sigj)     0.25    0.25    0.5     0       0.25    0.75

The Minhashing is a good approximation in this case. sim(ci, cj) has strong correlation with sim(sigi, sigj), which proves that the approximation is ideal. It captures the minimum hash values of sets, effectively summarizing their contents while preserving the relative uniqueness of elements. 
```
- Steps:
```
After hash1: 3 1 2 2
After hash2: 1 1 3 1
After hash3: 1 3 1 1
After hash4: 2 3 1 1
```

