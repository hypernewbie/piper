### Piper

Piper is a simple script designed for template based code generation, named after the Pied Piper of Hamelin. The philosophy is to design a template meta-language for trivial parsing and then write a trivial parser that can be easily extended by the user. As a result, the template metalanguage is rather strict, in order to take a lot of workload off the parser.

Features:
* Under 100 lines of Python code.
* Runs on any platforms that support Python 3.6.
* Easily customisable and extendable.
* Can be used to generate any programming language that supports block comments.

### Dependencies

* Python 3.6 installed on the user's system.

### Examples

Piper relies on block comment features of the target programming language. Piper lines start with || (two pipes).

The following hello.txt example:
```
|| <json>
|| { "T_ARRAY" : [ { "T" : "World" }, { "T" : "Bob" }, { "T" : "Alice" } ] }
|| </json>
|| <template>
|| HELLO_TEMPLATE
|| hello %T%
|| 
|| </template>
|| <eval>
|| HELLO_TEMPLATE(T_ARRAY)
|| </eval>

-------------------------------------------------------
|| <output>
-------------------------------------------------------

-------------------------------------------------------
|| </output>
-------------------------------------------------------
```

When run through the command:
```
py piper.py hello.txt
```

Produces:
```
|| <json>
|| { "T_ARRAY" : [ { "T" : "World" }, { "T" : "Bob" }, { "T" : "Alice" } ] }
|| </json>
|| <template>
|| HELLO_TEMPLATE
|| hello %T%
|| 
|| </template>
|| <eval>
|| HELLO_TEMPLATE(T_ARRAY)
|| </eval>

-------------------------------------------------------
|| <output>
-------------------------------------------------------
hello World
hello Bob
hello Alice
-------------------------------------------------------
|| </output>
-------------------------------------------------------

```

A more complicated example, handling enums, which is a common C code generation usecase:
```
#include <cstdio>

/*
|| <json>
|| {
||     "LIST_ITEMS" : [
||         { "NAME" : "Bunny",    "VALUE" : "2" },
||         { "NAME" : "Cheat",    "VALUE" : "4" },
||         { "NAME" : "Bomb",     "VALUE" : "5" },
||         { "NAME" : "Car",      "VALUE" : "6" }
||     ]
|| }
|| </json>
*/

/*
|| <template>
|| FUNC_TEMPLATE
||     EASTEREGG_%NAME_UPPERCASE%,
|| 
|| </template>
|| <eval>
|| FUNC_TEMPLATE(LIST_ITEMS)
|| </eval>
*/

enum EasterEgg {
/*
|| <output>
*/
    EASTEREGG_BUNNY,
    EASTEREGG_CHEAT,
    EASTEREGG_BOMB,
    EASTEREGG_CAR,
/*
|| </output>
*/
};

/*
|| <template>
|| FUNC_TEMPLATE2
||     "EASTEREGG_%NAME_UPPERCASE%",
|| 
|| </template>
|| <eval>
|| FUNC_TEMPLATE2(LIST_ITEMS)
|| </eval>
*/
const char* EasterEggToStr[] = {
/*
|| <output>
*/
    "EASTEREGG_BUNNY",
    "EASTEREGG_CHEAT",
    "EASTEREGG_BOMB",
    "EASTEREGG_CAR",
/*
|| </output>
*/
};
```
