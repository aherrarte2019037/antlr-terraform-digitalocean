grammar TerraformSubset;

terraform: (block | COMMENT)* EOF;

block: provider | resource | variable | output;

provider: 'provider' STRING '{' body '}';
resource: 'resource' STRING STRING '{' body '}';
variable: 'variable' STRING '{' body '}';
output: 'output' STRING '{' body '}';

body: (keyValue | COMMENT)*;

keyValue: IDENTIFIER '=' expr;

expr: STRING
    | NUMBER
    | BOOLEAN
    | reference;

reference: IDENTIFIER ('.' IDENTIFIER)*;

BOOLEAN: 'true' | 'false';
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' ('\\' . | ~["\\])* '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;

COMMENT: '#' ~[\r\n]* -> skip;

WS: [ \t\r\n]+ -> skip;
