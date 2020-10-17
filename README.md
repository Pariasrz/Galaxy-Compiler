
# Galaxy-Compiler
Lexical Analyzer and Parser for a programming language named Galaxy based on a LL1 grammar which you can find [Here](https://github.com/Pariasrz/Galaxy-Compiler/blob/main/Parsing%20Table%20(LL1%20Grammar).txt) 


Here are the rules for this programming language:
- Integer:
```
protostar x := 15 %
```
A protostar is a star in it's early stages.
- Float:

```
star x := 15.5 %
```

- String:

```
planet x := ' Hello World ' %
```
- Character: stating a character would be like this:

```
asteroid x := 'Hi' %
```
Note that asteroid is a minor planet.
- Array: we can define a multi-dimensional array of objects with "cluster DataType ArrayName , Size , SizeOfEachElement %":

```
cluster protostar x , 10 , 5 %
```
Note that Star Cluster is a big group of stars. 
- Loop structure:

```
ring ( condition )
	statement1 %
	statement2 %
	...
```
- Conditional structure:

```
nebula ( condition )
	statement1 %
	statement2 %
     ...
```
A Nebula is an interstellar cloud of dust and gases where stars are born, so you can define conditions for the stars you want to create!

- Comment:
	- Single-line comment can be followed by ||:
	```
	|| a comment
	```
	- Multi-line comment block:
	```
	|.
	comment1
	comment2
	...
	.|
	```
- Operators: This is very simple: Expression OPERATOR Expression. For example:
```
x + y 
x // y
```
Each Operator definition can be found in [Delimiters and Operators](https://github.com/Pariasrz/Galaxy-Compiler/blob/main/Reserved%20Words%2C%20Delimiters%20and%20Operators.txt)
