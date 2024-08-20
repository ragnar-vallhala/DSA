#include <bits/stdc++.h>
using namespace std;

bool isSafe(int **board, int row, int col, int n);
bool placeQueen(int **board, int row, int n);
void printBoard(int** board, int n);

int main()
{
    int n = 28;
    int **board = new int*[n];
    for(int i = 0; i < n; i++)
    {
        board[i] = new int[n];
        for(int j = 0; j < n; j++)
        {
            board[i][j] = 0;
        }
    }

    printBoard(board, n);
    placeQueen(board,0,n);
    cout<<"\n\n";
    printBoard(board, n);

    for(int i = 0; i < n; i++)
        delete[] board[i];
    delete[] board;

    return 0;
}

void printBoard(int** board, int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cout << board[i][j] << " ";
        }
        cout << "\n";
    }
}

bool isSafe(int **board, int row, int col, int n)
{
    // Check in the same row
    for(int i = 0; i < col; i++)
    {
        if(board[row][i] == 1)
            return false;
    }
    
    // Check in the same column
    for(int i = 0; i < row; i++)
    {
        if(board[i][col] == 1)
            return false;
    }

    // Check the upper left diagonal
    for(int i = row, j = col; i >= 0 && j >= 0; i--, j--)
    {
        if(board[i][j] == 1)
            return false;
    }

    // Check the upper right diagonal
    for(int i = row, j = col; i >= 0 && j < n; i--, j++)
    {
        if(board[i][j] == 1)
            return false;
    }

    return true;
}

bool placeQueen(int **board, int row, int n)
{
    if(row >= n)
        return true;

    for(int col = 0; col < n; col++)
    {
        if(isSafe(board, row, col, n))
        {
            board[row][col] = 1;
            if(placeQueen(board, row + 1, n))
                return true;
            board[row][col] = 0;
        }
    }
    return false;
}
