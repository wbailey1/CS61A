from lab05 import *

## Extra Trees Questions ##

# Q9
def info(t, target):
    """Returns a list of all the information about the song TARGET. If the song
    cannot be found in the tree, return None.

    >>> my_account = tree('inSTRUMental', [
    ...     tree('classical', [
    ...         tree('Tchaikowsky', [
    ...             tree('Piano Concerto No. 1', [
    ...                 tree('Allegro non troppo'),
    ...                 tree('Andantino'),
    ...                 tree('Allegro con fuoco')])]),
    ...         tree('Bruch', [
    ...             tree('Violin Concerto No. 1', [
    ...                 tree('Allegro moderato'),
    ...                 tree('Adagio'),
    ...                 tree('Allegro energico')])])])])
    >>> info(my_account, 'Adagio')
    ['inSTRUMental', 'classical', 'Bruch', 'Violin Concerto No. 1', 'Adagio']
    >>> info(my_account, 'Allegro non troppo')
    ['inSTRUMental', 'classical', 'Tchaikowsky', 'Piano Concerto No. 1', 'Allegro non troppo']
    >>> info(my_account, 'Sandstorm') # Should return None, which doesn't appear in the interpreter
    """
    "*** YOUR CODE HERE ***"

