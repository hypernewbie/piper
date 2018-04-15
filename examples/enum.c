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