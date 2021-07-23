theBoard = {
    'top-left': ' ',
    'top-mid': ' ',
    'top-right': ' ',
    'mid-left': ' ',
    'mid-mid': ' ',
    'mid-right': ' ',
    'bottom-left': ' ',
    'bottom-mid': ' ',
    'bottom-right': ' '
}


def displayBoard(board):
    print(board['top-left'] + ' | ' + board['top-mid'] + ' | ' + board['top-right'])
    print('---------')
    print(board['mid-left'] + ' | ' + board['mid-mid'] + ' | ' + board['mid-right'])
    print('---------')
    print(board['bottom-left'] + ' | ' + board['bottom-mid'] + ' | ' + board['bottom-right'])


displayBoard(theBoard)
theBoard['mid-mid'] = 'X'
displayBoard(theBoard)