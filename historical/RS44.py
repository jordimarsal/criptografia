'''
Created on 2 oct. 2016

@author: Jordi Marsal
'''
from xmllib import space

#########################################################################################
# 
# Global Parameters
#
#########################################################################################

# Constants

# Grid size (num rows and num columns)
NUM_ROWS, NUM_COLUMNS = 24, 25

# Set of values to be used as column numbers
COLUMN_NUMBERS = range(1, 26)

# Set of letters to be used in digraphs
DIGRAPHS_LETTERS = ["a", "b", "c", "d", "e"]

# Set of digraphs made with DIGRAPHS_LETTERS
DIGRAPHS = [l1+l2 for l1 in DIGRAPHS_LETTERS for l2 in DIGRAPHS_LETTERS]

# Values to fill grid cells
GRID_CELLS = [" ", "x"]

# Log level constants
LOG_LEVEL_DEBUG = 2
LOG_LEVEL_WARN = 1
LOG_LEVEL_ERR = 0

# Log level: you can change this value to modify the verbosity of the implementation
LOG_LEVEL = LOG_LEVEL_DEBUG

#########################################################################################
# 
# PUBLIC HELPERS
#
#########################################################################################

import pprint
import random
pp = pprint.PrettyPrinter(width=600)

# Function print_level
# Prints a message if LOG_LEVEL is higher than the specified level
# * Parameter level: message verbosity level
# * Parameter msg: message to print
def print_level(level, msg):
    if level <= LOG_LEVEL:
        print msg

#########################################################################################
# 
# STUDENT HELPERS
#
# YOU CAN CREATE YOUR OWN HELPERS IN THIS SECTION 
# (OPTIONAL)
#

#########################################################################################
# Constants
# 

# Free cells in a row
FREE_CELLS = 10

#########################################################################################
# Functions
# 

####################################################
# Gives a list of random numbers without repetition
# Used: Set positions for empty spaces in a row
# Used: Provides the integer list for columns
# 

def get_cells(fli, NUM, offset):
    cell = random.randrange(0+ offset, NUM+ offset)
    if (cell in fli): 
        fli = get_cells(fli , NUM , offset)
    else:
        fli.append(cell)
    return fli
    
####################################################    
# Produces a list of rows depending of random spaces

def make_k_grid():
    list1=[]
    for y in range(NUM_ROWS):
        fres=[]
        for r in range(FREE_CELLS):
            fres=get_cells(fres, NUM_COLUMNS,0)
        list2=[]
        for x in range(NUM_COLUMNS):
            if (x in fres):
                list2.append(GRID_CELLS[0])
            else:
                list2.append(GRID_CELLS[1])
        list1.append(list2)
    return list1
    
####################################################
# Produces the list of digrafs for columns

def get_k_di_col(): 
    return get_list_digraf(NUM_COLUMNS)
    
####################################################
# Produces the list of digrafs for rows

def get_k_di_row(): 
    return get_list_digraf(NUM_ROWS)
    
####################################################    
# Returns a digrafs'list, large as NUM

def get_list_digraf(NUM):
    dilist=[]
    count=0
    while (count < NUM):
        di = get_digraf()
        if (not di in dilist):
            dilist.append(di)
            count+=1
    # print ("%s: %s %s" % (NUM,count,dilist))
    return dilist

####################################################
# Returns a random digraf

def get_digraf():
    ncell = random.randrange(0, 5)
    cell = DIGRAPHS_LETTERS[ncell]
    ncell = random.randrange(0, 5)
    cell += DIGRAPHS_LETTERS[ncell]
    return cell

####################################################
# Returns a random list of integers for k_columns

def get_k_columns():
    ilist=[]
    for _ in range(NUM_COLUMNS):
        ilist = get_cells(ilist, NUM_COLUMNS,1)
    return ilist
    
####################################################
# Returns a random digraf from a list

def get_digraf_list(lisdi):
    di = lisdi[random.randrange(0, len(lisdi))]
    return di

####################################################
# Fills the grid
def getFilledGrid(row, col, grid, txt):
    c=0
    while (c<len(txt)):
        s=grid[row][col]
        # print(str(c)+": "+str(row)+","+str(col)+" "+txt[c]+" g:"+s)
        if(s is ' '):
            grid[row][col]=txt[c]
            c+=1
            col+=1
        else:
            col+=1
        if (col>=NUM_COLUMNS):
            col=0
            row +=1
        if (row>=NUM_ROWS):
            row=0
    return grid
    
def gr(col, row):
    li2=[]
    li1=[]
    c=0
    for _ in range(col):
        c+=1
        li2.append(c) 
    for _ in range (row):
        li1.append(li2)
    return li1

####################################################             ###############
# CIFRADO
def getCyphTxt(grid, column_numbers, start_r, num_chars):
    cytxt=""
    c = 0
    # print("*idx:"+str(start_r))
    # print("*col:"+str(start_r))
    while (c < num_chars):
        for y in range(len(grid)):
            char=grid[y][start_r]
            if ((char is not ' ') & (char is not 'x')):
                # print(char)
                cytxt += char
                c+=1
        start_r= getNextCol(start_r, column_numbers)
        
    return cytxt

def getNextCol(colu, column_numbers):
    idx = getIdxfromCol(colu, column_numbers)
    idx += 1 
    if (idx > NUM_COLUMNS): idx=1
    colu = getColfromIdx(idx, column_numbers)
    # print("col:"+str(colu)+" idx:"+str(idx))
    return colu

def getColfromIdx(idx, column_numbers):
    col=0
    for index, item in enumerate(column_numbers): #
        if (item==idx): col = index
    return col

def getIdxfromCol(colu, column_numbers):
    idx=0
    for index, item in enumerate(column_numbers): #
        if (index==colu): idx = item
    return idx

#########################################################################################

# EXERCISE 1.1: Implement RS44 key generation
#
# Function UOC_RS44_GenerateKeys.
# Create a random RS44 key
# 
# * Returns: a 5 item list with the generated key in the following format:
# [grid, column_digraphs, row_digraphs, column_numbers, start_cell, start_column]
#

def UOC_RS44_GenerateKeys():
        
    # [["." for x in range(NUM_COLUMNS)] for y in range(NUM_ROWS)] 
    # [".." for x in range(NUM_COLUMNS)]
    # [".." for x in range(NUM_ROWS)]
    # [COLUMN_NUMBERS for x in range(NUM_COLUMNS)]
    
    
    #### IMPLEMENTATION GOES HERE ####
    
    k_grid = make_k_grid()
    k_digraph_columns = get_k_di_col() 
    k_digraph_rows = get_k_di_row()
    k_columns = get_k_columns() 
    
    k_write=[]
    k_write.append(get_digraf_list(k_digraph_rows))
    k_write.append(get_digraf_list(k_digraph_columns))
    
    k_read = get_digraf_list(k_digraph_columns)
    
    key = [k_grid, k_digraph_columns, k_digraph_rows, k_columns, k_write, k_read]
        
    ##################################
    
    return key

# EXERCISE 1.2: Implement RS44 enciphering
#
# Function UOC_RS44_Cipher.
# Cipher a message with RS44
# * Parameter key: a RS44 key (as generated by the UOC_RS44_GenerateKeys function)
# * Parameter plaintext: an uppercase string with the message to encrypt
# * Returns: an uppercase string with the ciphered message
# 

def UOC_RS44_Cipher(key, plaintext):
    
    #### IMPLEMENTATION GOES HERE ####
    ciphertext=""
    thetext = drainSpaces(plaintext)
    if (isApprovedLenght(thetext)):
        thetext = mayus(thetext)
        [grid, column_digraphs, row_digraphs, column_numbers, start_cell, start_column] = key
        
        pp.pprint(column_digraphs)
        pp.pprint(row_digraphs)
        pp.pprint(column_numbers)
        pp.pprint(start_cell)
        pp.pprint(start_column)
        
        start_row = getHitList(start_cell[0], row_digraphs)
        start_col = getHitList(start_cell[1], column_digraphs)
        
        grid = getFilledGrid(start_row, start_col, grid, thetext)
        
        start_read = getHitList(start_column, column_digraphs)
                   
        ciphertext = getCyphTxt(grid, column_numbers, start_read, len(thetext))
    
    ##################################
        
        print("Text to cypher: #%s#" % thetext)
        print("Cyphered Text:  #%s#" % ciphertext)
    else:
        print("massa llarg, limit:%s" % (NUM_ROWS * FREE_CELLS))
        
    return ciphertext

def mayus(text):
    text= text.upper()
    return text

def isApprovedLenght(text):
    ret = False
    if (len(text)<=(NUM_ROWS * FREE_CELLS)):ret=True
    return ret

def drainSpaces(text):
    l=text.split(' ')
    text=""
    for i in range(len(l)):
        text += l[i] 
    return text
    
def getHitList(digraf, list_digraphs):
    for index, item in enumerate(list_digraphs):
        if (item==digraf): 
            sr = index
            break
    return sr



# EXERCISE 1.3: Implement RS44 deciphering
#
# Function UOC_RS44_Decipher.
# Decipher a message with RS44
# * Parameter key: a RS44 key (as generated by the UOC_RS44_GenerateKeys function)
# * Parameter ciphertext: an uppercase string with the message to decrypt
# * Returns: an uppercase string with the deciphered message
# 

def UOC_RS44_Decipher(key, ciphertext):
    
    plaintext = ""
    
    #### IMPLEMENTATION GOES HERE ####
    if (isApprovedLength(ciphertext)):
        [grid, column_digraphs, row_digraphs, column_numbers, start_cell, start_column] = key
        
        start_row = getHitList(start_cell[0], row_digraphs)
        start_col = getHitList(start_cell[1], column_digraphs)
    
        path_ci = getPathGrid(start_row, start_col, grid, len(ciphertext))
        
        start_read = getHitList(start_column, column_digraphs)
        
        path_ci = getPopulatedCiph(ciphertext,start_read, path_ci, column_numbers)
        
        for loc in path_ci:
            plaintext += loc.char
    else:
        print("Error: excessive lenght of text")
        
    ##################################
    
    return plaintext

####################################################
# User data type to save each char in the path
# Parameter row: saves the row
# Parameter col: saves the column
# Parameter char: saves the char

class locate:
    def __init__(self, row, col, char):
        self.row=row
        self.col=col 
        self.char=char 
    
####################################################
# Gets the path of cipher through the grid
# Parameter row: initial row to start
# Parameter col: initial column to start
# Parameter grid: the grid
# Parameter length: length of ciphered text
# Returns: the path of 'locate' user data type

def getPathGrid(row, col, grid, length):
    c=0
    _path = []
    while (c<length):
        s=grid[row][col]
        if(s is GRID_CELLS[0]):
            a = locate(row, col, GRID_CELLS[0])
            _path.append(a)
            c+=1
            col+=1
        else:
            col+=1
        if (col>=NUM_COLUMNS):
            col=0
            row +=1
        if (row>=NUM_ROWS):
            row=0
    return _path

####################################################
# Fills the path through the grid with ciphered text
# Parameter _ciphered: the ciphered text
# Parameter _read: initial column to start read
# Parameter _path: the path of locate user data type
# Parameter _column_numbers: the column_numbers
# Returns: the path filled

def getPopulatedCiph( _ciphered, _read, _path, _column_numbers): 
    le, c = len(_path),0
    col = _read 
    while (c<le):
        for row in range(NUM_ROWS):
            if(in_path(_path, row, col)):
                _path=putPath(row,col,_path, _ciphered[c])
                c += 1 
        col = getNextCol(col, _column_numbers)
    return _path

####################################################
# Puts a char on a specific 'locate'
# Parameter row: row to put
# Parameter col: column to put
# Parameter pat: the path
# Parameter letta: the char to put
# Returns: the path filled

def putPath(row, col, pat, letta):
    for loc in pat:
        if ((loc.row==row) & (loc.col==col)): loc.char=letta
    return pat

####################################################
# Validate if a 'locate' exists in the path
# Parameter r: row to validate
# Parameter c: column to validate
# Parameter pat: the path
# Returns: boolean

def in_path(pat, r, c):
    ret = False
    for loc in pat:
        if ((loc.row==r) & (loc.col==c)): ret = True
    return ret

####################################################
# The length of text must be fitted in a key
# Parameter text: text to measure
# Returns: boolean if is ok

def isApprovedLength(text):
    ret=False
    if(len(text)<= NUM_ROWS * FREE_CELLS):ret=True
    return ret


###
### TEST ###
###

key =  [[['x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' '], 
         ['x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x'], 
         ['x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x'], 
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], 
         [' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', 'x', ' ', ' '], 
         [' ', ' ', ' ', 'x', ' ', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x'], 
         ['x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' '], 
         ['x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' '], 
         ['x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' '], 
         ['x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', ' ', 'x', ' '], 
         [' ', 'x', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x', ' ', ' ', 'x'], 
         ['x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x'], 
         [' ', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' '], 
         ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', ' ', 'x', 'x'], 
         [' ', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', ' '], 
         ['x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' '], 
         [' ', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', 'x'], 
         ['x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', ' ', 'x', 'x', ' '], 
         ['x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', ' ', 'x', 'x'], 
         [' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' '], 
         ['x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x'], 
         ['x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x', 'x', ' ', 'x', ' ', 'x'], 
         ['x', 'x', ' ', ' ', 'x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ', ' ', 'x', 'x'], 
         ['x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ']], 
        ['ac', 'ea', 'aa', 'be', 'bd', 'ce', 'de', 'ca', 'ec', 'ae', 'bb', 'eb', 'ee', 'cc', 'cd', 'bc', 'ab', 'da', 'cb', 'dd', 'dc', 'ad', 'ba', 'db', 'ed'], 
        ['be', 'da', 'dc', 'cb', 'aa', 'bb', 'ca', 'ec', 'ae', 'ab', 'eb', 'ad', 'dd', 'db', 'ba', 'cc', 'de', 'bc', 'ed', 'ce', 'cd', 'ac', 'ea', 'bd'], 
        [24, 20, 13, 15, 17, 7, 11, 10, 9, 22, 12, 16, 18, 25, 3, 4, 14, 8, 19, 6, 21, 5, 2, 23, 1], 
        ['bd', 'ed'], 
        'ac']


plaintext = "CRYPTOGRAPHY IS A TOOL TO PROTECT INFORMATION"

cyphertx = UOC_RS44_Cipher(key, plaintext)


def test_case_13(name, exp_plaintext, key, ciphered):
    plain = UOC_RS44_Decipher(key, ciphered)
    print "Test", name + ":", plain == exp_plaintext


exp_plaintext =  "ISTHEPRACTIVEANDSTUDYOFTECHNIQUESFORSECURECOMMUNICATION"
key =  [[['x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' '], ['x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x'], ['x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], [' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', 'x', ' ', ' '], [' ', ' ', ' ', 'x', ' ', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' '], ['x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' '], ['x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' '], ['x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', ' ', 'x', ' '], [' ', 'x', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x', ' ', ' ', 'x'], ['x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x'], [' ', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' '], ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', ' ', 'x', 'x'], [' ', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', ' '], ['x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' '], [' ', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', 'x'], ['x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', ' ', 'x', 'x', ' '], ['x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', ' ', 'x', 'x'], [' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' '], ['x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x', 'x', ' ', 'x', ' ', 'x'], ['x', 'x', ' ', ' ', 'x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ', ' ', 'x', 'x'], ['x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ']], ['ac', 'ea', 'aa', 'be', 'bd', 'ce', 'de', 'ca', 'ec', 'ae', 'bb', 'eb', 'ee', 'cc', 'cd', 'bc', 'ab', 'da', 'cb', 'dd', 'dc', 'ad', 'ba', 'db', 'ed'], ['be', 'da', 'dc', 'cb', 'aa', 'bb', 'ca', 'ec', 'ae', 'ab', 'eb', 'ad', 'dd', 'db', 'ba', 'cc', 'de', 'bc', 'ed', 'ce', 'cd', 'ac', 'ea', 'bd'], [24, 20, 13, 15, 17, 7, 11, 10, 9, 22, 12, 16, 18, 25, 3, 4, 14, 8, 19, 6, 21, 5, 2, 23, 1], ['bd', 'ed'], 'ac']
ciphered =  "EETNMIAIQURUYIDAESADCHTNESFORSFOCPETRONTMCUNVOSIIEHCTUC"
test_case_13("13.2", exp_plaintext, key, ciphered)

