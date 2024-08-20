"""Testing the birthday_book.py program.  Tests written by Mark Smucker and Hannah Yeates."""
from birthday_book import main
from io import StringIO
import sys
import os

def run_input_output(capsys, monkeypatch, name):
    with open(f"tests-input/test-{name}.txt", "r") as infile:
        user_input = infile.read()
    with open(f"tests-expected-output/test-{name}.out.txt", "r") as infile:
        expected_output = infile.read()
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    main()
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test_echo_on_off(capsys, monkeypatch):
    """Make sure echo on/off works."""
    run_input_output(capsys, monkeypatch, "echo-on-off")

def test_add(capsys, monkeypatch):
    """Your program should add Madonna Ciccone and Natalie Hershlag 
    to the birthday book, then it should output the list of items in the 
    birthday book."""
    run_input_output(capsys, monkeypatch, "add")

def test_add_wrongargs(capsys, monkeypatch):
    """Your program should add Madonna Ciccone, and report an error when 
    adding Natalie. Your list should only contain Madonna Ciccone. """
    run_input_output(capsys, monkeypatch, "add-wrongargs")

def test_adding(capsys, monkeypatch):
    run_input_output(capsys, monkeypatch, "adding")

def test_bad_format(capsys, monkeypatch):
    """Your program should indicate that the input is invalid, 
    and should prompt the user for a new input."""
    run_input_output(capsys, monkeypatch, "bad-format")

def test_delete_0(capsys, monkeypatch):
    """Your program should report that this is an invalid input. Your birthday 
    book should start counting at one."""
    run_input_output(capsys, monkeypatch, "delete-0")

def test_delete_bounds(capsys, monkeypatch):
    """Your program should report that this is an invalid input. 
    There is only one element in the list."""
    run_input_output(capsys, monkeypatch, "delete-bounds")

def test_delete_n(capsys, monkeypatch):
    """Your program should not delete Madonna Ciccone, 
    and she should show up in the list."""
    run_input_output(capsys, monkeypatch, "delete-n")

def test_delete_name(capsys, monkeypatch):
    """Your program should add Madonna Ciccone to the birthday book. 
    Since your program deletes based on the number, the command 
    'delete Madonna Ciccone'
    should be recognized as an invalid command. When the birthday book is listed, 
    Madonna Ciccone should be listed."""
    run_input_output(capsys, monkeypatch, "delete-name")

def test_delete_neg(capsys, monkeypatch):
    """Your program should report that this is an invalid input."""
    run_input_output(capsys, monkeypatch, "delete-neg")

def test_delete_no_c_y(capsys, monkeypatch):
    """Your program should add Madonna Ciccone to the birthday book, then when 
    it confirms whether or not to delete the entry, it should continue to prompt 
    the user of y/n until the user enters y. The list should be empty at this 
    point."""
    run_input_output(capsys, monkeypatch, "delete-no-c-y")

def test_delete_overbounds(capsys, monkeypatch):
    """Your program should add Madonna Ciccone and Natalie Hershlag to the 
    birthday book. Your program should report that 5 is an invalid entry in 
    the birthday book."""
    run_input_output(capsys, monkeypatch, "delete-overbounds")

def test_delete_y(capsys, monkeypatch):
    """Your program should add, then delete Madonna Ciccone from the birthday book."""
    run_input_output(capsys, monkeypatch, "delete-y")

def test_help(capsys, monkeypatch):
    """Your program should indicate that “help page” is an invalid input. It should 
    output the list of commands when 'help' is processed."""
    run_input_output(capsys, monkeypatch, "help")

def test_list_wrongargs(capsys, monkeypatch):
    """Your program should  report that it is an invalid input."""
    run_input_output(capsys, monkeypatch, "list-wrongargs")

def test_list(capsys, monkeypatch):
    """Your program should report that there are no birthdays in the birthday book."""
    run_input_output(capsys, monkeypatch, "list")

def test_load(capsys, monkeypatch):
    """We do a bunch of adding, saving, and loading."""
    run_input_output(capsys, monkeypatch, "load")
    if os.path.exists(".test-load-bbday-book-entries.txt"):
        os.remove(".test-load-bbday-book-entries.txt")

def test_save(capsys, monkeypatch):
    """We add some, save some, load some."""
    run_input_output(capsys, monkeypatch, "save")
    if os.path.exists(".test-save-bbday-book-entries.txt"):
        os.remove(".test-save-bbday-book-entries.txt")

def test_search_wrongargs(capsys, monkeypatch):
    """We test the search functionality as well as make sure it only takes 1 arg."""
    run_input_output(capsys, monkeypatch, "search-wrongargs")

def test_search(capsys, monkeypatch):
    """We test the search functionality.  Be sure to be case insensitive."""
    run_input_output(capsys, monkeypatch, "search")

def test_wrongcommand(capsys, monkeypatch):
    """Make sure bad commands are rejected."""
    run_input_output(capsys, monkeypatch, "wrongcommand")

def test_input(capsys, monkeypatch):
    """A big sequence of commands that exercises the program."""
    run_input_output(capsys, monkeypatch, "input")
    if os.path.exists(".test-bbday-book-entries.txt"):
        os.remove(".test-bbday-book-entries.txt")


