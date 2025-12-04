# Attempt at aoc 2025

Advent of code 2025

they cut down the number of problems this time round. hope i can finish this year   B-)

### problem 4

one thing I learned is that for working with 2d arrays, it's typically easier to add a padding wall to the outside so that edge cases are easier to handle

eg. if the matrix is the following

XX<br>
XX

adding a layer of padding would make it something like

....<br>
.XX.<br>
.XX.<br>
....

this is really helpful when you want to check elements at the start and end of rows and columns and avoiding off by one indexing errors.