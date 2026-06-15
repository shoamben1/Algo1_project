"""
Final Project – Latin Square Solver

מטרתכם:
לממש אלגוריתם Backtracking שפותר ריבוע לטיני חלקי.

דרישות:
- אם אין פתרון → להחזיר "אין פתרון"
- אם יש פתרון יחיד → להחזיר את הפתרון
- אם יש יותר מפתרון אחד → להחזיר את מספר הפתרונות
- אם יש יותר מ-10 פתרונות → לעצור ולהחזיר "יותר מ-10 פתרונות"

הערה:
אסור להשתמש במשתנים גלובליים.
"""

MAX_SOLUTIONS = 10


def is_valid(board, row, col, num):
    """
    board - הלוח של המספרים
    החזר True אם ניתן להציב num במיקום (row, col)
    לפי חוקי הריבוע הלטיני.
    אחרת החזר False.
    """
    n = len(board)
    #בדיקה בשורה לפי חוקי ריבוע לטיני
    for j in range(n):
        if board[row][j] == num:                                          
            return False
    #בדיקה בעמודה לפי חוקי ריבוע לטיני
    for i in range(n):
        if board[i][col] == num:
            return False
    
    return True
def find_empty(board):
    """
    board - הלוח של המספרים
    מצא תא ריק (שמכיל 0).
    אם נמצא – החזר (row, col)
    אם לא נמצא – החזר None
    """
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return (i , j)
    
    return None

def backtrack(board, count, first_solution):
    """
    board - הלוח של המספרים
    פונקציה רקורסיבית שמנסה להשלים את הלוח.

    count – מספר הפתרונות שנמצאו עד כה
    first_solution – רשימה ריקה שבה ניתן לשמור פתרון ראשון
    """
    if count > MAX_SOLUTIONS:
        return count
    empty_cell = find_empty(board)
    if empty_cell is None:
        count += 1
        if count == 1:
            solution_copy = [row[:] for row in board]
            first_solution.append(solution_copy)
        
        return count
    row, col = empty_cell
    n = len(board)
    for num in range (1,n+1):
        if is_valid(board,row,col,num):
            board[row][col] = num #נסה להציב את המספר
            count = backtrack(board ,count , first_solution)# ביצוע קריאה רקורסיבית
            board[row][col] = 0 #להחזיר את התא למצב ריק כלומר 0 
            if count > MAX_SOLUTIONS:
                return count #עצירה מוקדמת אם יש יותר מ10 פתרונות
            
    return count

def solve_latin_square(board):

    first_solution = []
    count = 0

    count = backtrack(board, count, first_solution)

    if count == 0:
        return "אין פתרון"

    elif count == 1:
        return first_solution[0]

    elif count > MAX_SOLUTIONS:
        return "יותר מ-10 פתרונות"

    else:
        return count

def main():
    examples = [

        # אין פתרון
        [
            [1, 2, 0],
            [2, 1, 0],
            [0, 0, 0]
        ],

        # אין פתרון
        [
            [1, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        # פתרון יחיד
        [
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 3]
        ],

        # יותר מפתרון אחד
        [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],

        # יותר מ10 פתרונות
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    ]

    for board in examples:

        print("Board:")
        for row in board:
            print(row)

        result = solve_latin_square([row[:] for row in board])

        print("Result:", result)
        print("-" * 40)


if __name__ == "__main__":
    main()